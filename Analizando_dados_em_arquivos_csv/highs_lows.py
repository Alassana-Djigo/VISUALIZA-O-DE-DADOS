import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "dados_meteorologicos.csv"

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)
	highs,dates,lows = [],[],[]

	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,"Faltando Data")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	# print(highs)
	# print(generos)

fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,c = "red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)
plt.title("Temperaturas do mes de Agosto de 2022")
plt.xlabel("",fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperaturas(F)",fontsize = 16)
plt.tick_params(axis = "both", which ="major",labelsize=16)
plt.show()
