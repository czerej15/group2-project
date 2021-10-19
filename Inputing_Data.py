from Classes import Student

f = open('student_data.csv')
contents = f.read().split('\n')
f.close()  # close the file

large = []
temp = []
count = 0
for i in range(len(contents)):
	lst = contents[i].split(';')
	for j in lst:
		count += 1
		l = j.strip(',')
		k = l.split(',')
		temp.append(k)
		if k == ['']:
			temp.remove(k)
			count -= 1
		if count % 7 == 0:
			large.append(temp)
			if temp == []:
				large.remove(temp)
			temp = []
	
# after 7 or 8 appends, append to a whole new list to split between students
#print(large[1][0][0])

searchName = str(input())
for p in range(len(large)):
		if temp[p][0][0] == searchName:
			print(True)
			# Student.get_student_details(temp[p][h][0],temp[p][h][1])