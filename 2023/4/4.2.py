import re
with open("input", 'r') as f:
    cards = {}
    sum = 0
    for line in f.readlines():
        cn = int((re.findall("Card\s+(\d+)", line)[0]))
        if cn not in cards.keys():
            cards[cn] = 1
        line = line.split(":")[1]
        line = line.split("|")
        gz = line[0]
        gz = re.sub("\s+", " ", gz).split(" ")
        pos = 0
        for i in gz:
            if i == "":
                gz.pop(pos)
            pos += 1
        tz = line[1]
        tz = re.sub("\s+", " ", tz).split(" ")
        pos = 0
        for i in tz:
            if i == "":
                tz.pop(pos)
            pos += 1
        anzsieg = 0
        for i in gz:
            if i in tz:
                anzsieg += 1
        if anzsieg >= 1:
            for i in range(1, anzsieg+1):
                if cn+i not in cards.keys():
                    cards[cn+i] = 1
                for k in range(1, cards[cn]+1):
                    cards[cn+i] += 1
        print(f"Cards{cards}, siege {anzsieg}")
        # input()

        # print(cards)

for i in cards:
    sum = sum + (cards[i])
print(cards)
print(sum)
# print(cn + punkte)
