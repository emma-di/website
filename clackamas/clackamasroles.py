import csv
names = []
times = []
with open('clackamas/ClackNames.csv', newline='') as csvfile:
    namereader= csv.reader(csvfile)
    for row in namereader:
        names.append(str(row))
with open('clackamas/ClackFri.csv', newline='') as csvfile:
    frireader=csv.reader(csvfile)
    for row in frireader:
        if row[1]!='':
            times.append(str(row[1]))
    times.remove("Time")
with open('clackamas/ClackSat.csv', newline = '') as csvfile:
    satreader=csv.reader(csvfile)

with open('clackamas/roles.csv', 'w') as roles:
    wr = csv.writer(roles)
    for time in times:
        print(time)
        wr.writerows([time])