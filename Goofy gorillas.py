import sys
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = input()
    line = line.split(" ")
    line[0] = str(line[0])
    line[1] = str(line[1])

    if line[0] == "true" and line[1] == "true":
        print("true")
    elif line[0] == "true" and line[1] == "false":
        print("false")
    elif line[0] == "false" and line[1] == "true":
        print("false")
    elif line[0] == "false" and line[1] == "false":
        print("true")