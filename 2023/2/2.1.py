import re
with open("input", 'r') as f:
    sum = 0
    gspiele = {0}
    for line in f.readlines():
        gid = re.findall("Game (\d+):", line)[0]
        line = line.split(":")[1]
        line = line.split(";")
        green = 0
        red = 0
        blue = 0
        for i in line:
            wuerfel = i.split(",")
            for w in wuerfel:
                print(w + " ")
                if re.search("green", w) is not None:
                    if int(re.findall("(\d+) green", w)[0]) > green:
                        green = int(re.findall("(\d+) green", w)[0])
                if re.search("blue", w) is not None:
                    if int(re.findall("(\d+) blue", w)[0]) > blue:
                        blue = int(re.findall("(\d+) blue", w)[0])
                if re.search("red", w) is not None:
                    if int(re.findall("(\d+) red", w)[0]) > red:
                        red = int(re.findall("(\d+) red", w)[0])
        if red <= 12 and green <= 13 and blue <= 14:
            gspiele.add(int(gid))
            print("\n")
print(gspiele)
for i in gspiele:
    sum = sum + i
print(sum)
