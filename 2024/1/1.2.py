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
rechts_dict = {}

for i in rechts:
    if i in rechts_dict:
        rechts_dict[i] = rechts_dict[i] + 1
    if i not in rechts_dict:
        rechts_dict[i] = 1
sum_dict = {}
summe = 0
for i in links:
    if i in rechts_dict:
        sum_dict[i] = rechts_dict[i] * i
        print(f"Zahl: {i}")
        print(sum_dict[i])
        summe = summe + (i * rechts_dict[i])
        print(summe)
        print("----")
print(summe)
