import re

sum = 0
ln = 1
with open("input", 'r') as f:
    for line in f.readlines():
        rawline = line
        line = re.sub("one", "one1one", line)
        line = re.sub("two", "two2two", line)
        line = re.sub("three", "three3three", line)
        line = re.sub("four", "four4four", line)
        line = re.sub("five", "five5five", line)
        line = re.sub("six", "six6six", line)
        line = re.sub("seven", "seven7seven", line)
        line = re.sub("eight", "eight8eight", line)
        line = re.sub("nine", "nine9nine", line)
        fd = ""
        ld = ""
        for i in line:
            try:
                int(i)
                if fd == "":
                    fd = i
                ld = i
            except:
                pass
        lsum = str(fd) + str(ld)
        sum = sum + int(lsum)
        print(
            f"{ln} - rawine: {rawline.strip()} - line: {line.strip()} - first digit: {fd} - last digit: {ld} - lsum = {lsum} - sum = {sum}")
        if ln == 135:
            inputhum = input()
        ln += 1
        # if inputhum != lsum:
        #     print(lsum, " Missmatch!")
