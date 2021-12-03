import csv
from datetime import datetime
filename = 'C:\\Users\public\Devo programs\Data_visualization\csv\data\dashin_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs=[],[]
    for row in reader:
        high=int(row[5])
        current_datetime=datetime.strptime(row[2],'%Y-%m-%d')
        highs.append(high)
        dates.append(current_datetime)


