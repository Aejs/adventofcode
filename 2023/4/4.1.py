import re
with open("input", 'r') as f:
    sum = 0
    for line in f.readlines():
        cn = (re.findall("Card\s+(\d+)", line)[0])
        line = line.split(":")[1]
        line = line.split("|")
        gz = line[0]
        gz = re.sub("\s+", " ", gz).split(" ")
        pos = 0
        for i in gz:
            if i == "":
                gz.pop(pos)
            pos += 1
        tz = line[1]
        tz = re.sub("\s+", " ", tz).split(" ")
        pos = 0
        for i in tz:
            if i == "":
                tz.pop(pos)
            pos += 1
        anzsieg = 0
        for i in gz:
            if i in tz:
                anzsieg += 1
        if anzsieg >= 1:
            sum = sum + 2**(anzsieg-1)
print(sum)

# print(cn + punkte)
