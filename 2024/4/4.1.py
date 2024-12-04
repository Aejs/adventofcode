import re
with open("input", "r") as f:
    list2analyse = []
    lines = {}
    line_laenge = 0
    line_num = 0
    text = f.readlines()
    for i in text:
        line_laenge = len(i)
        i = i.strip()
        pos = 0
        lines[line_num] = {}
        for char in i:
            lines[line_num][pos] = char
            pos = pos + 1
        line_num = line_num + 1

    # print(line_laenge)

summe = 0
# Grade von Links nach Rechts

for line in lines:
    row = []
    temp = []
    for char in lines[line]:
        temp.append(lines[line][char])
    list2analyse.append("".join(temp))

# Von Oben nach Unten
for i in range(0, line_laenge, 1):
    line_num = 0
    temp = []
    for line in lines:
        temp.append(lines[line_num][i])
        line_num = line_num + 1
    list2analyse.append("".join(temp))

# Diagonal /


diag_helper = []
for i in range(line_laenge):
    line_num = i
    pos = 0
    temp = []
    for line in lines:
        print(line_num, pos)
        temp.append(lines[line_num][pos])
        if line_num < len(lines)-1:
            line_num = line_num + 1
        else:
            break
        if pos < line_laenge-1:
            pos = pos + 1
    list2analyse.append("".join(temp))

    temp = []
    pos = i
    line_num = 0
    for line in lines:
        temp.append(lines[line_num][pos])
        if line_num < len(lines)-1:
            line_num = line_num + 1
        else:
            break
        if pos < line_laenge-1:
            pos = pos + 1
        else:
            break
    diag_helper.append("".join(temp))
diag_helper.pop(0)
list2analyse = list2analyse + diag_helper

# Diagonal \


diag_helper = []
for i in range(line_laenge):
    line_num = i
    pos = line_laenge-1
    temp = []
    for line in lines:
        print(line_num, pos)
        temp.append(lines[line_num][pos])
        if line_num < len(lines)-1:
            line_num = line_num + 1
        else:
            break
        if pos > 0:
            pos = pos - 1
    list2analyse.append("".join(temp))

for i in range(line_laenge):
    line_num = 0
    pos = i
    temp = []
    for line in lines:
        print(line_num, pos)
        temp.append(lines[line_num][pos])
        if line_num < len(lines)-1:
            line_num = line_num + 1
        else:
            break
        if pos > 0:
            pos = pos - 1
        else:
            break
    diag_helper.append("".join(temp))

diag_helper.pop(len(diag_helper)-1)
list2analyse = list2analyse + diag_helper


count = 0
for i in list2analyse:
    ergebnis = re.finditer(("(?=XMAS)|(?=SAMX)"), i)
    for match in ergebnis:
        count = count + 1


print(count)
