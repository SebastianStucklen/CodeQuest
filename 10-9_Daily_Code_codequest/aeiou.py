import sys

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):

    vowels = 0

    line = sys.stdin.readline().rstrip()

    size = len(line)
    
    #line = line.split(" ")

    for i in range(size):

        if line[i] == "a" or line[i] == "e" or line[i] == "i" or line[i] == "o" or line[i] == "u" or line[i] == "A" or line[i] == "E" or line[i] == "I" or line[i] == "O" or line[i] == "U" :

            vowels+=1
    
    print(vowels)