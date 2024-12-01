import re
links = []
rechts = []
with open("input", "r") as f:
    text = f.read()
    ergebnis = re.findall("(\d+)\s+(\d+)", text)
    for i in ergebnis:
        links.append(int(i[0]))
        rechts.append(int(i[1]))
links.sort()
rechts.sort()
ele = 0
summe = 0
for i in links:
    if links[ele] > rechts[ele]:
        calcu = (links[ele] - rechts[ele])
        print(calcu)
    else:
        calcu = rechts[ele] - links[ele]
        print(calcu)
    summe = summe + calcu
    ele = ele + 1
print(summe)
