class Calculations:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def yearly_calculations(self, year):
        highest_temp = {'value': -float('inf'), 'month': None, 'date': None}
        lowest_temp =  {'value': float('inf'), 'month': None, 'date': None}
        most_humidity = {'value': -float('inf'), 'month': None, 'date': None}

        all_files_parsed = self.dictionary

        for month in all_files_parsed[year]:
            for date in all_files_parsed[year][month]:
                split_date = date.split('-')

                if all_files_parsed[year][month][date]['max_temp'] > highest_temp['value']:
                    highest_temp['value'] = all_files_parsed[year][month][date]['max_temp']
                    highest_temp['date'] = split_date[2]
                    highest_temp['month'] = month

                if all_files_parsed[year][month][date]['min_temp'] < lowest_temp['value']:
                    lowest_temp['value'] = all_files_parsed[year][month][date]['min_temp']
                    lowest_temp['date'] = split_date[2]
                    lowest_temp['month'] = month

                if all_files_parsed[year][month][date]['max_humidity'] > lowest_temp['value']:
                    most_humidity['value'] = round(all_files_parsed[year][month][date]['max_humidity'], 1)
                    most_humidity['date'] = split_date[2]
                    most_humidity['month'] = month

        
        return {
            'highest_temp': highest_temp,
            'lowest_temp': lowest_temp,
            'most_humidity': most_humidity
        }

    def monthly_calculations(self, year, month):
        sum_highest_temp = 0
        sum_lowest_temp = 0
        sum_mean_humidity = 0

        all_files_parsed = self.dictionary
        total_days = len(all_files_parsed[year][month])

        for date in all_files_parsed[year][month]:
            current_data = all_files_parsed[year][month][date]

            sum_highest_temp += current_data['max_temp']
            sum_lowest_temp += current_data['min_temp']
            sum_mean_humidity += current_data['mean_humidity']

        avg_highest_temp = sum_highest_temp // total_days
        avg_lowest_temp = sum_lowest_temp // total_days
        avg_mean_humidity = sum_mean_humidity // total_days
        
        return {
            'avg_highest_temp': avg_highest_temp,
            'avg_lowest_temp': avg_lowest_temp,
            'avg_mean_humidity': avg_mean_humidity
        }

    def daily_high_low_temp(self, year, month):
        daily_temp_dict = {}

        all_files_parsed = self.dictionary
        for date in all_files_parsed[year][month]:
            max_temp = all_files_parsed[year][month][date]['max_temp']
            min_temp = all_files_parsed[year][month][date]['min_temp']
            split_date = date.split('-')
            
            daily_temp_dict[split_date[2]] = {'high': max_temp, 'low': min_temp}

        return daily_temp_dict