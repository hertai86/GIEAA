import csv
import os
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes

gdp_list = {}
edu_list = {}
interval = 0
normalize_factor = 2e10

firstDSpath = os.getcwd() + "\input\GDP by Country.csv"
secondDSpath = os.getcwd() + "\input\BL2013_MF1599_v2.2.csv"
results_path = os.getcwd() + "\output\_results.csv"

with open(firstDSpath, 'r') as gdp_csv_file:
    gdp_csv_reader = csv.DictReader(gdp_csv_file)
    for line in gdp_csv_reader:
        if line['\ufeff"Country Name"'] == "Austria":
            for count in range(1961, 1966):
                endofinterval = 1965
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0

            for count in range(1966, 1971):
                endofinterval = 1970
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0

            for count in range(1971, 1976):
                endofinterval = 1975
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0

            for count in range(1976, 1981):
                endofinterval = 1980
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(1981, 1986):
                endofinterval = 1985
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(1986, 1991):
                endofinterval = 1990
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(1991, 1996):
                endofinterval = 1995
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(1996, 2001):
                endofinterval = 2000
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(2001, 2006):
                endofinterval = 2005
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor
            interval = 0
            for count in range(2006, 2011):
                endofinterval = 2010
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval] = interval / normalize_factor


with open(secondDSpath, 'r') as edu_csv_file:
    edu_csv_reader = csv.DictReader(edu_csv_file)
    for line in edu_csv_reader:
        for c in range(1965, 2011):
            if line['country'] == "Austria" and '' + str(c) + '' == line['year']:
                edu_list[c] = float(line['lhc']) / float(line['lh']) * 100

names = list(edu_list.keys())
gdp_values = list(gdp_list.values())
edu_values = list(edu_list.values())

f = open(results_path, 'w')
i = 0
f.write("year_intrval,gdp_amount,edu_att_rate \n")
while i < len(gdp_values):
    f.write(str(names[i]) + "," + str(gdp_values[i]) + "," + str(edu_values[i]) + "\n")
    i += 1
f.close()

fig = plt.figure(1)

host = HostAxes(fig, [0.1, 0.1, 0.8, 0.8])
par1 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.set_ylabel("Density")
host.set_xlabel("Distance")

host.axis["right"].set_visible(True)
par1.axis["right"].set_visible(True)
par1.set_ylabel("Temperature")

par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)

fig.add_axes(host)

host.set_xlim(1975, 2010)
host.set_ylim(0, 100)

host.set_xlabel("GDP and Success rate")
host.set_ylabel("GDP per five years (*2*10^10")
par1.set_ylabel("Success Rate (%)")

p1, = host.plot(names, gdp_values, label="GDP")
p2, = par1.plot(names, edu_values, label="Success Rate")

par1.set_ylim(0, 100)

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())

plt.show()
