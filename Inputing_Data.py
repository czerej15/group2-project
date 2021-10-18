f = open('student_data.csv')
contents = f.read().split('\n')
f.close()  # close the file

temp = []
for i in range(len(contents)):
	lst = contents[i].split(';')
	for j in lst:
		l = j.strip(',')
		l = l.strip('"')
		print(l)
		print()