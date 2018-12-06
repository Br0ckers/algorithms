import matplotlib.pyplot as plt
import csv

x = []
y = []
data_in = 'set_1.csv'
with open(data_in,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[1]))
        y.append(float(row[2]))
        # y.append(float(row[3]))
        # y.append(float(row[4]))

plt.plot(x,y, label='Loaded file '+data_in)
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.title('Finding Duplicate\n values in array')
plt.legend()
plt.show()
