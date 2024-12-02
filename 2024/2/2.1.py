with open("input", "r") as f:
    line = "!"
    count = 0
    while line != []:
        text = f.readline()
        line = text.split()
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

            if zahl_now == zahl_last:
                break

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
            # print(pos, len(line)-1)
            if pos == len(line)-1:
                print(
                    f'{differ_1_3}{"increase" if increase else ""} {"decrease" if decrease else ""}: {line}')
                if differ_1_3 and increase:
                    count = count + 1
                if differ_1_3 and decrease:
                    count = count + 1

            pos = pos + 1

        print("---")

print(count)
