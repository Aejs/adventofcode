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
    position = 1
    positionen = []
    for i in cur_line:
        if i == "*":
            positionen.append(position)
        position += 1
    for i in positionen:
        mzahlen = 0
        for i in range(i-2, i+1):
            if cur_line[i].isdigit():
                mzahlen += 1
            if next_line[i].isdigit():
                mzahlen += 1
            if last_line[i].isdigit():
                mzahlen += 1
            print(mzahlen)
            # addition = 0
            # zahl1 = []
            # zahl2 = []
            # while cur_line[i+addition].isdigit() == True:
            #     print(cur_line[i+addition])
            #     addition += 1
            #     zahl.append(cur_line[i+addition])

            # while cur_line[i-addition].isdigit() == True:
            #     print(cur_line[i-addition])
            #     addition += 1

            #     # if str(cur_line(i)).isdigit() is True:
            #     #     print(str(cur_line(i)).isdigit())
