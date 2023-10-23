cases = int(input())

for i in range(cases):

    line = input()
    line = line.split(" ")

    line[0]=int(line[0])
    if line[1] == "true" or line[1] == "True":
        line[0]-=5
    if line[0] <=60:
        print("no ticket")
    if line[0] >= 61 and line[0] <= 80:
        print("small ticket")
    if line[0] >= 81:
        print("big ticket")