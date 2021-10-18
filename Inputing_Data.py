f = open('student_data.csv')
contents = f.read().split('\n')
f.close()  # close the file

temp = []
for i in range(len(contents)):
	lst = contents[i].split(';')
	for j in lst:
		l = j.strip(',')
		k = l.split(',')
		temp.append(k)
		if k == ['']:
			temp.remove(k)


print(temp)