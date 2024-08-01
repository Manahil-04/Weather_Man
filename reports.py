def generate_symbol(num, color_code):
    result = ''
    for n in range(num):
        result += f'\033[{color_code}m+\033[0m'
    return result


class Reports:
    def __init__(self):
        pass

    def yearly_cal_report(self, yearly_cal, year):
        print("Weather report for: ", year)
        print("Highest Temperature:", yearly_cal['highest_temp']['value'],"C on", yearly_cal['highest_temp']['month'], yearly_cal['highest_temp']['date'])
        print("Lowest Temperature:", yearly_cal['lowest_temp']['value'],"C on", yearly_cal['lowest_temp']['month'], yearly_cal['lowest_temp']['date'])
        print("Most Humidity:", yearly_cal['most_humidity']['value'],"% on", yearly_cal['most_humidity']['month'], yearly_cal['most_humidity']['date'], '\n')

    def monthly_cal_report(self, monthly_cal, month, year):
        print("Weather report for: ", month, year)
        print("Highest Average Temperature: ", monthly_cal['avg_highest_temp'], "C")
        print("Lowest Average Temperature: ", monthly_cal['avg_lowest_temp'], "C")
        print("Average Mean Humidity: ", monthly_cal['avg_mean_humidity'], "%")

    def two_temp_bar_charts(self, daily_temp, month, year):
        print(month, year)
        for key in daily_temp.keys():
            print(key, generate_symbol(int(daily_temp[key]['high']), 31) , daily_temp[key]['high'])
            print(key, generate_symbol(int(daily_temp[key]['low']), 34) , daily_temp[key]['low'])

    def one_bar_chart(self, daily_temp, month, year):
        print(month, year)
        for key in daily_temp.keys():
            low_temp = daily_temp[key]['low']
            high_temp = daily_temp[key]['high']
            low_symbols = generate_symbol(int(low_temp), 34)
            high_symbols = generate_symbol(int(high_temp), 31) 
            print(f"{key} {low_temp:.1f}{low_symbols}{high_symbols}{high_temp:.1f}")