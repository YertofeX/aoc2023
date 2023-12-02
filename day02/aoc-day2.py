filename = "in.txt"
# filename = "ex.txt"

# maxCubes = {
#     "red" : 12,
#     "green" : 13,
#     "blue" : 14
# }

out = 0
with open(filename, "r") as f:
    for line in f:
        # valid = True
        # id = int(line.split(":")[0].split(" ")[1])
        maxCubes = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }
        for round in line.split(":")[1].split(";"):
            for cube in round.split(","): 
                cubeData = cube.strip().split(" ")
                maxCubes[cubeData[1]] = max(maxCubes[cubeData[1]], int(cubeData[0]))
        prod = 1
        for key in maxCubes:
            prod *= maxCubes[key]
        out += prod
print(out)