horison_lines = [
    "UFDACYGLKP",
    "KABINAQXYV",
    "YLLNGTTAKE",
    "ZMPLWARZNO",
    "GVFAIXAAFY",
    "YMPLPGLSOH",
    "WGVHFPACKW",
    "AFTERTLTHU",
    "TNKIDCBEOS",
    "ZBAMANSWER",
]

input_words = [
    "APPLE",
    "AIRPLANE",
    "ANT",
    "AFTER",
    "ALLIGATOR",
    "ASK",
    "ANSWER",
    "ANY",
]

matris = list(map(list, horison_lines))

topL_downR_diag = []
for row in range(9, 0, -1):
    topL_downR_diag.append((row, 0))
for col in range(0, 10):
    topL_downR_diag.append((0, col))

topR_downL_diag = []
for col in range(0, 10):
    topR_downL_diag.append((0, col))
for row in range(1, 10):
    topR_downL_diag.append((row, 9))


def print_if_find(string, L):
    for word in input_words:
        if word in string:
            print(f"true {L}: " + word)


def check_dia(pos):
    string = ""
    row = pos[0]
    col = pos[1]
    next = True
    while next:
        string += matris[row][col]
        if (row + 1 > 9) or (col + 1 > 9):
            next = False
        else:
            row += 1
            col += 1
    return string


def check_dia2(pos):
    string = ""
    row = pos[0]
    col = pos[1]
    next = True
    while next:
        string += matris[row][col]
        if (row + 1 > 9) or (col - 1 < 0):
            next = False
        else:
            row += 1
            col -= 1
    return string


# check horisontell
H_string = ""
for line in horison_lines:
    H_string += line

print_if_find(H_string, "H")
# reverse
print_if_find(H_string[::-1], "HR")

# check vertical
V_string = ""
for i in range(len(horison_lines)):
    for word in horison_lines:
        V_string += word[i]

print_if_find(V_string, "V")
# reverse
print_if_find(V_string[::-1], "VR")


# check diagonally(from top-L to bot-R)

D_string = ""
for pos in topL_downR_diag:
    D_string += check_dia(pos)


print_if_find(D_string, "D")

# check diagonally(from top-r to bot-L)
D2_string = ""
for pos in topR_downL_diag:
    D2_string += check_dia2(pos)

print_if_find(D2_string, "D2")

# diagonally reverse

print_if_find(D_string[::-1], "DR")
print_if_find(D2_string[::-1], "D2R")


for x in range(10):
    for y in range(10):
        print(matris[x][y], end=" ")
    print()
