import time
import argparse
import requests
import json
import os


class Weather:
    def __init__(self):
        self.__API_KEY = '3115bc9a8bd042be962120133240101'
        self.__FAVORITE_CITIES_FILE = 'favorite_cities.json'

    def get_weather_data(self, city):
        response = requests.get('http://api.weatherapi.com/v1/current.json' +
                                '?key=' + self.__API_KEY+'&q='+city)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f" \n ERROR CODE {response.status_code} \n")
            return None

    def display_weather_data(self, weather_data):
        if weather_data:
            print(
                f" \n*** Tempreture of city is {weather_data['current']['temp_c']}C ***\n")
            print(
                f"***\n weather condition is {weather_data['current']['condition']['text']} and wind speed is {weather_data['current']['wind_kph']} kph *** \n")
            print(
                f"\n*** Updated on {weather_data['current']['last_updated']} ***\n")

        else:
            print("Weather data list is empty")

    def get_favorite_city(self):
        if os.path.exists(self.__FAVORITE_CITIES_FILE):
            with open(self.__FAVORITE_CITIES_FILE, 'r') as file:
                return json.load(file)

        else:
            return []

    def save_favorite_cities(self, favorite_city):
        with open(self.__FAVORITE_CITIES_FILE, 'w') as file:
            json.dump(favorite_city, file)

    def add_favorite_city(self, city_name):
        favorite_cities_list = self.get_favorite_city()
        if city_name not in favorite_cities_list:
            favorite_cities_list.append(city_name)
            self.save_favorite_cities(favorite_cities_list)
            print(f"\n{city_name}  added to the favorite city list")

        else:
            print(f" \n{city_name} already present in the favorite coty list\n")

    def remove_city(self, city_name):
        favorite_city_list = self.get_favorite_city()
        if city_name in favorite_city_list:
            favorite_city_list.remove(city_name)
            self.save_favorite_cities(favorite_city_list)
            print(f"{city_name} is removed form the favorite city list\n")
        else:
            print(f"\n{city_name} is not there in the city name list\n")

    def main(self):
        parser = argparse.ArgumentParser(
            description="Command-line Weather Checking Application")
        parser.add_argument('--weather', action='store_true',
                            help='Specify the city for weather checking')
        parser.add_argument('--add', help='Add city to favorites')
        parser.add_argument('--remove', help='Remove city from favorites')
        parser.add_argument('--list', action='store_true',
                            help='List favorite cities')

        args = parser.parse_args()

        if args.weather:
            cities_name_to_check_weather = self.get_favorite_city()
            if cities_name_to_check_weather:
                while True:
                    for city in cities_name_to_check_weather:
                        weather_data = self.get_weather_data(city)
                        self.display_weather_data(weather_data)

                    time.sleep(20)

            else:
                print("\nList is empty please add your favorite city to the list \n")

        elif args.add:
            self.add_favorite_city(args.add)

        elif args.remove:
            self.remove_city(args.remove)

        elif args.list:
            favorite_cities = self.get_favorite_city()
            if favorite_cities:
                for city in favorite_cities:
                    print(f"\n - {city} \n")
            else:
                print(f"\n List is empty\n")


if __name__ == '__main__':
    weather_condition = Weather()
    weather_condition.main()
