filename = "in.txt"
# filename = "ex.txt"
# filename = "ex2.txt"

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def findDigitFrom(line, i):
    if line[i].isnumeric():
        return None
    for numStr in numbers.keys():
        if line[i:i + len(numStr)] == numStr:
            return str(numbers[numStr])
    return None
    

def getNum(line):
    first = ""
    last = ""
    for i in range(len(line)):
        if line[i].isnumeric():
            if first == "":
                first = line[i]
            last = line[i]
        else:
            d = findDigitFrom(line, i)
            if d != None:
                if first == "":
                    first = d
                last = d
    return int(first + last)

sum = 0
with open(filename, "r") as f:
    for line in f:
        sum += getNum(line)
print(sum)