from weather_data_parser import WeatherDataParser
from calculations import Calculations
from reports import Reports


def show_menu():
    print("Menu:")
    print("1. For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.")
    print("2. For a given month display the average highest temperature, average lowest temperature, average mean humidity.")
    print("3. For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day.")
    print("4. For a given month draw one horizontal bar chart on the console for the highest and lowest temperature on each day on the same line.")
    print("5. Exit")

def number_to_month(month_number):
    month_names = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
        'Sep', 'Oct', 'Nov', 'Dec'
    ]
    
    return month_names[month_number - 1]

def main():
    folder_path = 'Weather_Man/weatherfiles'
    
    parser = WeatherDataParser(folder_path)

    data_dictionary = parser.weather_reading

    calculator = Calculations(data_dictionary)

    report = Reports()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        print("\n")

        if choice == '1':
            try:
                year = int(input("Enter year (from 2004 to 2016): "))
                if 2004 <= year <= 2016:
                    yearly_cal = calculator.yearly_calculations(year)
                    report.yearly_cal_report(yearly_cal, year)
                else:
                    print("Invalid year. Please enter a year between 2004 and 2016.\n")
            except ValueError:
                print("Invalid input. Please enter a valid year.\n")

        elif choice == '2':
            try:
                year = int(input("Enter year (e.g., 2014): "))
                if 2004 <= year <= 2016:
                    month_num = int(input("Enter month (1 for January, 2 for February, ..., 12 for December): "))
                    if 1 <= month_num <= 12:
                        month = number_to_month(month_num)
                        monthly_cal = calculator.monthly_calculations(year, month)
                        report.monthly_cal_report(monthly_cal, month, year)
                    else:
                        print("Invalid month number. Please enter a number between 1 and 12.\n")
                else:
                    print("Invalid year. Please enter a year between 2004 and 2016.\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers for year and month.\n")

        elif choice == '3':
            try:
                year = int(input("Enter year (e.g., 2011): "))
                if 2004 <= year <= 2016:
                    month_num = int(input("Enter month (1 for January, 2 for February, ..., 12 for December): "))
                    if 1 <= month_num <= 12:
                        month = number_to_month(month_num)
                        daily_temp = calculator.daily_high_low_temp(year, month)
                        report.two_temp_bar_charts(daily_temp, month, year)
                    else:
                        print("Invalid month number. Please enter a number between 1 and 12.\n")
                else:
                    print("Invalid year. Please enter a year between 2004 and 2016.\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers for year and month.\n")

        elif choice == '4':
            try:
                year = int(input("Enter year (e.g., 2011): "))
                if 2004 <= year <= 2016:
                    month_num = int(input("Enter month (1 for January, 2 for February, ..., 12 for December): "))
                    if 1 <= month_num <= 12:
                        month = number_to_month(month_num)
                        daily_temp = calculator.daily_high_low_temp(year, month)
                        report.one_bar_chart(daily_temp, month, year)
                    else:
                        print("Invalid month number. Please enter a number between 1 and 12.\n")
                else:
                    print("Invalid year. Please enter a year between 2004 and 2016.\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers for year and month.\n")

        elif choice == '5':
            print("Exit")
            exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
    
main()