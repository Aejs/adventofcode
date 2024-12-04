import re
with open("input", "r") as f:
    text = f.read()
    results = re.findall("mul\((\d+)\,(\d+)\)", text)
    summe = 0

    for i in results:
        summe = summe + (int(i[0]) * int(i[1]))

print(summe)
