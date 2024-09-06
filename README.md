# WeatherMan
Weather Man is a Python application that processes weather data files to generate various reports and visualizations. This program can display the highest and lowest temperatures, most humid days, and averages for a given month or year. Additionally, it can create bar charts for daily high and low temperatures.

## Features
1. **Yearly Report**:
    - Displays the highest temperature and day.
    - Displays the lowest temperature and day.
    - Displays the most humid day and humidity.
  
2. **Monthly Averages Report**:
    - Displays the average highest temperature.
    - Displays the average lowest temperature.
    - Displays the average mean humidity.

3. **Monthly Daily High/Low Temperature Bar Charts**:

   Draws horizontal bar charts on the console for the highest and lowest temperatures on each day. Highest in red and
   lowest in blue.
    ```
    March 2011
    01 +++++++++++++++++++++++++ 25C
    01 +++++++++++ 11C
    02 ++++++++++++++++++++++ 22C
    02 ++++++++ 08C
    ```

5. **Monthly Combined High/Low Temperature Bar Chart**:

   Draws horizontal bar charts on the console for the highest and lowest temperatures on each day. Highest in red and lowest in blue.
    ```
    March 2011
    01 11C ++++++++++++++++++++++++++++++++++++ 25C
    02 08C ++++++++++++++++++++++++++++++ 22C
    ```

## Installation
1. Clone the repository:
```
git clone https://github.com/Manahil-04/WeatherMan.git
```
2. Navigate into the project directory:

```
cd weather-man
```
3. Ensure you have Python 3 installed and required libraries installed.
   - pandas
   - numpy

## Usage
1. Place your weather data files in a directory.
2. Run the application with the desired options.
