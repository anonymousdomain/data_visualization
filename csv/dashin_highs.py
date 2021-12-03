import csv
from datetime import datetime
import matplotlib.pyplot as plt
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

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red')

plt.title('daily high temprature',fontsize=16)
plt.xlabel('dates',fontsize=16)
#avoid datetime overlaping in the label
fig.autofmt_xdate()
plt.ylabel('Temprature in(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=10)
plt.show()
