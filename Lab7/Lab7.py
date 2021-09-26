input = open('Lab7In.txt','r')
text = input.readlines()

#cheking the file for information
if len(text) == 0:
	print("File is empty")
	exit() 

#counting the number of subjects
count = 0
for i in range(len(text)):
	if text[i].find("subject") > 0:
		count+= 1

#cheking the file for availability of subjects
if count == 0:
	print("Subjects not found")
	exit()

#set variables
subject = {"title": "","type": "", "time": "", "location": "", "room": "","professor": "", "format": ""}
subjects = []
for i in range(count):
	subjects.append(subject.copy())
textstr = []
check = 0

#finding information
number = 0
for i in range(len(text)):
	#finding subject
	if text[i].find('\"subject\"') > 0:
		textstr = text[i].split(':')
		subject = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1
	#finding type
	if text[i].find('\"type\"') > 0:
		textstr = text[i].split(':')
		type = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1
	#finding time
	if text[i].find('\"time\"') > 0:
		textstr = text[i].split('"')
		time = textstr[3]
		check+=1
	#finding location
	if text[i].find('\"location\"') > 0:
		textstr = text[i].split(':')
		location = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1
	#finding room
	if text[i].find('\"room\"') > 0:
		textstr = text[i].split(':')
		room = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1
	#finding professor
	if text[i].find('\"professor\"') > 0:
		textstr = text[i].split(':')
		professor = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1
	#finding format
	if text[i].find('\"format\"') > 0:
		textstr = text[i].split(':')
		format = textstr[1][textstr[1].find('"')+1:textstr[1].rfind('"')]
		check+=1

	if check == 7:
		subjects[number]["title"] = subject
		subjects[number]["type"] = type
		subjects[number]["time"] = time
		subjects[number]["location"] = location
		subjects[number]["room"] = room
		subjects[number]["professor"] = professor
		subjects[number]["format"] = format

		check = 0
		number+= 1
input.close()

#output
output = open("Lab7Out.txt", 'w')
number = 0
for i in range(count):
	output.write("message subject" + str(number+1) + " {\n")
	output.write("\t" + "required string title = " + subjects[number]["title"] + ";\n")
	output.write("\t" + "required string type = " + subjects[number]["type"] + ";\n")
	output.write("\t" + "required string time = " + subjects[number]["time"] + ";\n")
	output.write("\t" + "required string location = " + subjects[number]["location"] + ";\n")
	output.write("\t" + "required int32 room = " + subjects[number]["room"] + ";\n")
	output.write("\t" + "required string professor = " + subjects[number]["professor"] + ";\n")
	output.write("\t" + "required string format = " + subjects[number]["format"] + ";\n")
	output.write("}\n")
	number+=1

output.close()

print("Program was completed")


