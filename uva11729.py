class Soldier:
	def __init__(self, brief_time, complete_time):
		self.brief_t = brief_time
		self.complete_t = complete_time

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.complete_t == other.complete_t
		else:
			return False
			
	# only use the lest than function when sorting
	def __lt__(self, other):
		if isinstance(other, self.__class__):
			if self.complete_t < other.complete_t:
				return True
			else:
				return False
		else:
			return False

	def __gt__(self, other):
		if isinstance(other, self.__class__):
			if self.complete_t > other.complete_t:
				return True
			else:
				return False
		else: 
			return False

# record the results
result = []
while True:
	total_time = 0
	total_brief_time = 0

	num_soldiers = input('Enter the number of soldiers:')
	if num_soldiers == 0:
		break

	soldiers = []
	for i in range(num_soldiers):
		b_time, c_time = [int(x) for x in raw_input('Enter the brief time and the complete time of a soldier: ').split()]
		s = Soldier(b_time, c_time)
		soldiers.append(s)

	#Sort
	soldiers.sort()

	for i in range(num_soldiers-1, -1, -1):
		total_brief_time += soldiers[i].brief_t
		if total_brief_time + soldiers[i].complete_t > total_time:
			total_time = total_brief_time + soldiers[i].complete_t
		# for testing
		# print '%d %d' % (total_brief_time, total_time)

	result.append(total_time)

# print the results
for i in range(len(result)):
	print '%d %d' % (i+1, result[i])

