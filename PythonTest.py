import sys #For errorhandling and exiting

def Assignment1():
	dots = "."
	dotArray = dots*80
	total = 80
	tenArray = "1234567890"
	space = " "
	fillspace = ""
	topNumbers=tenArray*8
	while True:
		try:
			left = float(input("How many inches for the left margin?"))
			assert(left >= 0), 'Number must be bigger than 0'
			break
		except:
			print("Enter an integer 0-13") #Will repeat until proper n
	left = left * 6 #converts the inches to characters
	left = int(round(left)) #makes sure it's a whole number
	total = total - left
	leftDots = dots*left
	while True:
		try:
			right= float(input("How many inches for the right margin?"))
			assert(right >= 0), "Number must be bigger than 0"
					#assert((80 - len(leftDots) - right) >= 0), "Must be less than the remaining characters and at least 0"
			break
			#try:
					#assert(right<= total),"Greater than remaining space"
		except:
			print("Enter an integer 0-13")
	#fileName= str(input("What is the file name?")) #Doesn't work on codio for whatever reason
	fileName = "InputFile.txt"
	right = right * 6 #converts the inches to characters
	right = int(round(right)) #makes sure it's a whole number
	total = total - right
	middle = 80 - (left + right)
	middleSpace = space*middle
	middleUsable = middle
	tempMiddle = middleUsable
	rightDots = dots*right
	
	emptyLine = ""
	outputText = emptyLine
	try:
			if left < 0 or right < 0:
					sys.exit("ERROR ---------- MARGINS ARE NEGATIVE")
			if (left + right) >= 80:
					sys.exit("ERROR ---------- MARGINS ARE TOO BIG")
			inFile = open(fileName, 'r')
			outFile = open('DAT1.txt', 'r+')
			words = inFile.read().split()
			
			outFile.write(topNumbers + "\n") #writes the character counter at the top
			print(topNumbers + "\n") #writes the character counter at the top
			for word in words:
					if len(word) > middle:
							sys.exit("ERROR ---------- WORD IS LONGER THAN AVAILABLE LINE SPACE")
					if len(word) >= middleUsable:
							fillspace = middleUsable*space #Gets spaces for the remaining characters within the margin
							outputText = leftDots+outputText+fillspace+rightDots+'\n'
							outFile.write(outputText)
							print (outputText)
							outputText = emptyLine
							middleUsable = tempMiddle #resets the value
					if outputText.endswith('.'): #adds two spaces if there's a period
						word = '  ' + word
					else: #adds one space between words
						word = ' ' + word
					middleUsable = middleUsable -len(word)
					outputText = outputText + word
			outputText = leftDots + outputText + rightDots + '\n'
			outFile.write(outputText)
			print(outputText)
	except FileNotFoundError: #throws error if the filename is wrong
			sys.exit("ERROR ---------- NO FILE BY THAT NAME")
	inFile.close() #closes the file when it's done
	outFile.close()#closes the file when it's done
Assignment1()
