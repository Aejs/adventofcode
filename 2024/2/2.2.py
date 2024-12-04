def linechecker(line):
    pos = 0
    zahl_now = ""
    zahl_last = ""
    decrease = True
    increase = True
    differ_1_3 = True
    for num in range(0, len(line), 1):
        if pos > 0:
            zahl_last = int(zahl_now)
            zahl_now = int(line[pos])
            # print(zahl_now, zahl_last)
        else:
            zahl_now = int(line[pos])
            pos = pos + 1
            continue

        if differ_1_3 is True:
            if int(zahl_last) - int(zahl_now) in [3, 2, 1, -1, -2, -3]:
                differ_1_3 = True
            else:
                differ_1_3 = False

        if increase is True:
            if zahl_now > zahl_last:
                increase = True
            else:
                increase = False

        if decrease is True:
            if zahl_now < zahl_last:
                decrease = True
            else:
                decrease = False
        pos = pos + 1

    if differ_1_3 is True and decrease:
        return True
    elif differ_1_3 is True and increase:
        return True
    else:
        return False


count = 0
id = 1
with open("input", "r") as f:
    for i in f.readlines():
        i = i.split()
        result = linechecker(i)
        if result:
            count = count + 1
        else:
            for y in range(0, len(i), 1):
                line_test = i[:y]+i[y+1:]
                result = linechecker(line_test)
                if result:
                    count = count + 1
                    break
                else:
                    continue

        id = id + 1
print(count)
