import re

with open("input", 'r') as f:
    times = f.readline()
    distance = f.readline()
    
distance = "".join(re.sub("\s+"," ",distance,0).split(" ")[1:])
times = "".join(re.sub("\s+"," ",times,0).split(" ")[1:])
rennen = {}

reise = 0
gewinne = []
for second in range (0,int(times)):
    entfernung = second * (int(times) - second)
    if entfernung > int(distance):
        gewinne.append(second)

print ( len(gewinne))