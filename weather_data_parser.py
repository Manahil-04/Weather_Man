import os
import pandas as pd
import numpy as np

class WeatherDataParser:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.weather_reading = self.process_folder()


    def process_folder(self):
        weather_readings = {}

        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            list_from_filename = filename.split('_')
            month = list_from_filename[3][:-4]
            year = int(list_from_filename[2])

            parsed_data = self.parse_file(file_path)
            if year not in weather_readings:
                weather_readings[year] = {}
            if month not in weather_readings[year]:
                weather_readings[year][month] = {}
            
            weather_readings[year][month] = parsed_data
            
        return weather_readings

    def parse_file(self, file_path):
        df = pd.read_csv(file_path)

        numeric_cols = df.select_dtypes(include='number').columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        
        non_numeric_cols = df.select_dtypes(exclude='number').columns
        df[non_numeric_cols] = df[non_numeric_cols].fillna(value=np.nan)


        readings = {}

        for index, row in df.iterrows():
            if 'PKT' in row and pd.notna(row['PKT']):
                date = row['PKT']
            elif 'PKST' in row and pd.notna(row['PKST']):
                date = row['PKST']
            else:
                continue

            readings[date] = {
                "date": date,
                "max_temp": row.get('Max TemperatureC', None),
                "mean_temp": row.get('Mean TemperatureC', None),
                "min_temp": row.get('Min TemperatureC', None),
                "dew_point": row.get('Dew PointC', None),
                "mean_dew_point": row.get('MeanDew PointC', None),
                "min_dew_point": row.get('Min DewpointC', None),
                "max_humidity": row.get('Max Humidity', None),
                "mean_humidity": row.get(' Mean Humidity', None),
                "min_humidity": row.get(' Min Humidity', None),
                "max_sea_level_pressure": row.get(' Max Sea Level PressurehPa', None),
                "mean_sea_level_pressure": row.get(' Mean Sea Level PressurehPa', None),
                "min_sea_level_pressure": row.get(' Min Sea Level PressurehPa', None),
                "max_visibility": row.get(' Max VisibilityKm', None),
                "mean_visibility": row.get(' Mean VisibilityKm', None),
                "min_visibility": row.get(' Min VisibilitykM', None),
                "max_wind_speed": row.get(' Max Wind SpeedKm/h', None),
                "mean_wind_speed": row.get(' Mean Wind SpeedKm/h', None),
                "max_gust_speed": row.get(' Max Gust SpeedKm/h', None),
                "precipitation": row.get('Precipitationmm', None),
                "cloud_cover": row.get(' CloudCover', None),
                "events": row.get(' Events', None),
                "wind_dir_degrees": row.get(' WindDirDegrees', None)
                }
        return readings
        
