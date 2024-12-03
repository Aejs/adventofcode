import re
with open("input", "r") as f:
    text = f.read()
    text = text.replace("\n", "")
    results = re.findall(
        "^(.*?)(?<=don't\(\))|(?=do\(\))(.*?)(?<=don't\(\))|(?=do\(\))(.*?)$", text)
    summe = 0
    for i in results:
        if i[0] != '':
            analyse = i[0]
        if i[1] != '':
            analyse = i[1]
        if i[2] != '':
            analyse = i[2]

        ergebnis = re.findall("mul\((\d+)\,(\d+)\)", analyse)
        for y in ergebnis:
            # print(y)
            summe = summe + (int(y[0]) * int(y[1]))
print(summe)
