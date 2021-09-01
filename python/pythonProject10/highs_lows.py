import csv
from matplotlib import pyplot as plt
from datetime import datetime

# csv file dealing
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y.%m.%d")
        dates.append(current_date)
        try:
            high = int(row[8])
            low = int(row[9])
        except:
            print(current_date, "missing data!")
        else:
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'red', linewidth = 1)
plt.plot(dates, lows, c = 'blue', linewidth = 1)
plt.fill_between(dates, highs, lows, facecolor = 'yellow', alpha = 0.5)
plt.title("Daily high and low temperatures - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize = 16)
# axis = 'both'表示对两个坐标轴都进行设置
# which = 'major'表示只对主刻度进行设置
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()