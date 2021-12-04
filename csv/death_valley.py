import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename='csv\data\death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)
    head_row=next(reader)
        
    highs,lows,dates=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        try:
                high=int(row[4])   
                low=int(row[5])
            
        except ValueError:
            print(f"missing data for {current_date}")
        else:
                highs.append(high)
                lows.append(low)
                dates.append(current_date)

fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)

ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.show()