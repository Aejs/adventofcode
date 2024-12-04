import re
with open("input", 'r') as f:
    lines = {}
    ln = 1
    for line in f.readlines():
        lines[ln] = line
        ln += 1
guetige_zahlen = []
for i in range(1, ln):
    if i-1 >= 1:
        last_line = ".." + lines[i-1].strip() + ".."
    else:
        last_line = 144*"."
    cur_line = ".." + lines[i].strip() + ".."
    try:
        next_line = ".." + lines[i+1].strip() + ".."
    except:
        next_line = 142*"."
    print(last_line)
    print(cur_line)
    print(next_line)
    print("\n")
    print("\n")
    zahlen = []
    akt_zahl = []
    position = 1
    for i in cur_line:
        if i.isdigit():
            if akt_zahl == []:
                akt_zahl.append(position)
        else:
            if akt_zahl != []:
                akt_zahl.append(position-1)
                zahlen.append(akt_zahl)
                akt_zahl = []
        position += 1
    for zahl in zahlen:
        werten = False
        zahl_wert = []

        if cur_line[zahl[0]-2] != ".":
            werten = True
        if cur_line[zahl[1]] != ".":
            werten = True

        for i in range(zahl[0]-2, zahl[1]+1):
            # print(zahl[0], zahl[1])
            # print(cur_line[zahl[1]])
            # print(next_line[i])
            if last_line[i] is not ".":
                if last_line[i].isdigit() is False:
                    werten = True
            if next_line[i] is not ".":
                if next_line[i].isdigit() is False:
                    werten = True

        if werten is True:
            for i in range(zahl[0]-1, zahl[1]):
                zahl_wert.append(cur_line[i])
            guetige_zahlen.append(int("".join(zahl_wert)))
            print("".join(zahl_wert))
            zahl_wert = []
    # print(guetige_zahlen)
    # input()
print(guetige_zahlen)
sum = 0
for i in guetige_zahlen:
    sum = sum + i
print(sum)
# input()
