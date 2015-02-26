from sys import argv

scriptname, textfilename = argv 

text = open(textfilename)

print text.read()

textfilename_input = raw_input("enter your filename")

text_input = open(textfilename_input)

print text_input.read()

