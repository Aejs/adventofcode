import re
with open("input", "r") as f:
    list2analyse = []
    lines = {}
    line_laenge = 0
    line_num = 0
    text = f.readlines()
    for i in text:
        i = i.strip()
        line_laenge = len(i)
        pos = 0
        lines[line_num] = {}
        for char in i:
            lines[line_num][pos] = char
            pos = pos + 1
        line_num = line_num + 1

    # print(line_laenge)

line_num = 0
x33 = []
for i in lines:
    pos = 0
    temp = {}
    for num in range(0, 3, 1):
        temp[num] = {}
        for pos in range(0, line_laenge, 1):
            for pos_next in range(0, 3, 1):
                # print(lines[i+num])
                if i+num > len(lines)-1:
                    break
                if pos+pos_next > line_laenge-1:
                    break
                # print(num, pos_next)
                temp[num][pos_next] = lines[i+num][pos+pos_next]
    x33.append(temp)


def checksmax(d):
    print(d)
    if len(d) < 3:
        return False
    if d[1][1] == "A":
        print("check A")
        if (d[0][0] == "S" and d[2][2] == "M") or (d[0][0] == "M" and d[2][2] == "S"):
            print("CHeck 1")
            if (d[2][0] == "S" and d[2][2] == "M") or (d[0][2] == "M" and d[2][2] == "S"):
                print("treffer")


for i in x33:
    checksmax(i)
