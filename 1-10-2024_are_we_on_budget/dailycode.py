import math
cases = int(input())
output = []
average = []
sum = 0


for i in range(cases):
	variance = []
	items = input()
	items = int(items)
	budget = input().split(" ")
	actualPrice = input().split(" ")

	for i in range(items):
		variance.append(float(actualPrice[i])-float(budget[i]))

	output.append(variance)

for i in range(len(output)):
	for j in range(len(output[i])):
		sum += output[i][j]
		#print(output[i][j], end = " ")
	average.append(sum/len(output[i]))
	sum = 0

for i in range(len(average)):
	out = None
	num = str(math.floor(average[i]*100)/100)
	numTable = num.split()
	for i in range(len(numTable)):
		print(numTable[i], ", ")