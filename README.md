# -Infotrixs
This program will fetch weather data of a city and display it on the terminal.

# Weather Application

## Introduction
This is a command-line Python application that uses the Weather API to fetch and display weather data for a given city. It also allows users to add and remove cities from a list of favourite cities, which are stored in a JSON file.

## Requirements
- Python 3.x
- `requests` library
- `JSON` library
- `os` library
- `argparse` library

## Usage
1. **Fetch Weather Data**: To fetch the weather data for  the city list, use the following command:
    ```
    python weather.py --weather
    ```
    Replace "City Name" with the name of the city you want to fetch the weather data for. It updates after every 20 sec. 

2. **Add Favorite City**: To add a city to your list of favourite cities, use the following command:
    ```
    python weather.py --add "City Name"
    ```
    Replace "City Name" with the name of the city you want to add to your favourites.

3. **Remove Favorite City**: To remove a city from your list of favourite cities, use the following command:
    ```
    python weather.py --remove "City Name"
    ```
    Replace "City Name" with the name of the city you want to remove from your favourites.
4. **Display favourite cities**: To display the favourite cities list, use the following command:
    ```
    python weather.py --list
    ```

## Troubleshooting
If you encounter an error with the status code other than 200 when fetching the weather data, it might be due to an issue with the Weather API or the city name might not be recognized by the API.

If the favourite cities file does not exist in your current directory, the application will return an empty list when trying to fetch your favourite cities.

## Conclusion
This application is a simple and efficient way to check the weather for different cities and manage your favourite cities. Enjoy using the application!

Please note that this is a basic user manual. Depending on the final implementation of your application, some commands or functionalities may vary. If you have any questions or need further assistance, feel free to ask!

