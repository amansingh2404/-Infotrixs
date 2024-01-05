import time
import argparse
import requests
import json
import os


# Weather class to encapsulate weather-check-related functionalities
class Weather:
    def __init__(self):
        # The API key for the weather API and the json file for storing favorite cities.
        self.__API_KEY = '3115bc9a8bd042be962120133240101'
        self.__FAVORITE_CITIES_FILE = 'favorite_cities.json'

    # Fetch weather data for a given city using the Weather API
    def get_weather_data(self, city):
        # Sends a GET request to the weather API using request module.
        response = requests.get('http://api.weatherapi.com/v1/current.json' +
                                '?key=' + self.__API_KEY+'&q='+city)
        data = response.json()
        # status code is 200 it returns the data = response.json
        # and if status code is not equal to 200 it prints the error code
        if response.status_code == 200:
            return data
        else:
            print(f" \n ERROR CODE {response.status_code} \n")
            return None

    # This function takes weather_data as input parameter and prints weather report in readable formate.
    def display_weather_data(self, weather_data):
        # Prints the weather data if it exists, otherwise prints a message indicating that the list is empty.
        if weather_data:
            print(
                f" \n*** Tempreture of {weather_data['location']['name']} is {weather_data['current']['temp_c']}C ***\n")
            print(
                f"***\n weather condition is {weather_data['current']['condition']['text']} and wind speed is {weather_data['current']['wind_kph']} kph *** \n")
            print(
                f"\n*** Updated on {weather_data['current']['last_updated']} ***\n")

        else:
            print("Weather data list is empty")

    # Return a list of favorite cities.
    def get_favorite_city(self):
        # checks the __FAVORITE_CITIES_FILE exists in the current directory or not if it exists then open it in read mode
        # else return empty list
        if os.path.exists(self.__FAVORITE_CITIES_FILE):
            with open(self.__FAVORITE_CITIES_FILE, 'r') as file:
                return json.load(file)

        else:
            return []

    # saves the favorite_city to the __FAVORITE_CITIES_FILE
    def save_favorite_cities(self, favorite_city):
        # checks whether __FAVORITE_CITIES_FILE exists or not if it exists then open it in write formate and
        # close it aftr writing
        if os.path.exists(self.__FAVORITE_CITIES_FILE):
            with open(self.__FAVORITE_CITIES_FILE, 'w') as file:
                json.dump(favorite_city, file)

        else:
            print("File doesn't exists")

    # It takes city_name as parameter add the city name to __FAVORITE_CITY_FILE by calling
    # save_favorite_cities function
    def add_favorite_city(self, city_name):
        favorite_cities_list = self.get_favorite_city()
        if city_name not in favorite_cities_list:
            favorite_cities_list.append(city_name)
            self.save_favorite_cities(favorite_cities_list)
            print(f"\n{city_name}  added to the favorite city list")

        else:
            print(f" \n{city_name} already present in the favorite coty list\n")

    # takes the city_name as input parameter and removes it form the __FAVORITE_CITY_FILE
    def remove_city(self, city_name):
        favorite_city_list = self.get_favorite_city()
        if city_name in favorite_city_list:
            favorite_city_list.remove(city_name)
            self.save_favorite_cities(favorite_city_list)
            print(f"{city_name} is removed form the favorite city list\n")
        else:
            print(f"\n{city_name} is not there in the city name list\n")

    # Main function to handle command-line arguments and execute corresponding actions
    def main(self):
        # Using argeparse module to take user input from terminal
        parser = argparse.ArgumentParser(
            description="Command-line Weather Checking Application")
        parser.add_argument('--weather', action='store_true',
                            help='Checks the weather conditions of cities in the list')
        parser.add_argument('--add', help='Add city to favorites')
        parser.add_argument('--remove', help='Remove city from favorites')
        parser.add_argument('--list', action='store_true',
                            help='List favorite cities')

        args = parser.parse_args()

        # If statement to check if user want to print weather data of cities.
        if args.weather:
            cities_name_to_check_weather = self.get_favorite_city()
            # Checks if list is not empty
            if cities_name_to_check_weather:
                # if list is not empty then run infinite while loop to print weather data of the given cities
                #  and update it after every 20 sec. Untill user press (ctrl+c) to stop the exectuon.
                while True:
                    for city in cities_name_to_check_weather:
                        weather_data = self.get_weather_data(city)
                        self.display_weather_data(weather_data)

                    time.sleep(20)
            # If list is empty it will print a message.
            else:
                print("\nList is empty please add your favorite city to the list \n")
        # Condition will executed when user tries to add city to the list.
        elif args.add:
            self.add_favorite_city(args.add)
        # Condition will executed when user tries to remove city from the list.
        elif args.remove:
            self.remove_city(args.remove)
        # Prints the list of the city in __FAVORITE_CITIES_FILE on User request.
        elif args.list:
            favorite_cities = self.get_favorite_city()
            if favorite_cities:
                for city in favorite_cities:
                    print(f" - {city} ")
            else:
                print(f"\n List is empty\n")


# Entry point of the script
if __name__ == '__main__':
    # Creating a object of Weather class
    weather_condition = Weather()
    weather_condition.main()
