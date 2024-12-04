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

line_num = 0
x33 = []
for input_line in range(0, len(lines), 1):
    pos = 0
    while pos < line_laenge:  # Changed this to iterate through all positions
        temp = {}
        for num in range(0, 3, 1):
            temp[num] = {}
            for new_pos in range(0, 3, 1):
                if num + input_line > len(lines) - 1:
                    break
                if pos + new_pos > line_laenge - 1:
                    break
                temp[num][new_pos] = lines[input_line + num][pos + new_pos]
        if (
            len(temp) == 3
            and len(temp[0]) == 3
            and len(temp[1]) == 3
            and len(temp[2]) == 3
        ):
            x33.append(temp)
        pos += 1  # Move one position at a time

def checksmax(d):
    if d[1][1] != "A":
        return False

    # Check both diagonals for MAS or SAM
    left_diagonal = (d[0][0] == "M" and d[2][2] == "S") or (
        d[0][0] == "S" and d[2][2] == "M"
    )
    right_diagonal = (d[0][2] == "M" and d[2][0] == "S") or (
        d[0][2] == "S" and d[2][0] == "M"
    )

    return left_diagonal and right_diagonal

count = 0
for i in x33:
    if checksmax(i):
        count += 1

print(f"Total X-MAS patterns found: {count}")
