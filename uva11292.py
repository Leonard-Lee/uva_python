# UVA 11292
# http://uva.onlinejudge.org/external/112/11292.pdf

dragons = []
knights = []

# Input
d_num, k_num = [int(x) for x in raw_input('nter the number of dragons and the number of knights: ').split()]
for i in range(0, d_num):
	dragons.append(input('diameters of the dragon\'s head: '))
for i in range(0, k_num):
	knights.append(input('the heights of the knights: '))

# Sort
dragons.sort()
knights.sort()

# Caculate how much to spend or fails
total = 0
cursor = 0
isSuccessful = False
for i in range(len(dragons)):
	for j in range(cursor, len(knights)):
		if knights[j] >= dragons[i]:
			total += knights[j]
			cursor = j + 1
			break
	if cursor == len(knights)-1 and i == len(dragons)-1:
		isSuccessful = True
		

if not isSuccessful:
	print 'Loowater is doomed!'
else:
	print total