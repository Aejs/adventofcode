import re

with open("input", 'r') as f:
    times = f.readline()
    distance = f.readline()
    
distance = re.sub("\s+"," ",distance,0).split(" ")[1:]
times = re.sub("\s+"," ",times,0).split(" ")[1:]
rennen = {}
for i in range(0,len(distance)):
    rennen[distance[i]] = times[i]

siege = {}
for ii in rennen.keys():
    time = rennen[ii]
    reise = 0
    gewinne = []
    for second in range (0,int(time)):
        entfernung = second * (int(time) - second)
        if entfernung > int(ii):
            gewinne.append(second)
    siege[ii] = len(gewinne)

print (siege)
    