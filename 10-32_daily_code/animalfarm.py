import sys

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):

    line = sys.stdin.readline().rstrip()

    line = line.split(" ")
    
    print(int(line[0])*2+int(line[1])*4+int(line[2])*4)