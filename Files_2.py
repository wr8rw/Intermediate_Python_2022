#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# open a file and perform some functions against the file

from string import punctuation #punctuation from the string library is a string that contains all punctuation marks
#you can run print(punctuation) to see what this looks like

print(punctuation)

punctuation_list = list(punctuation) #convert string of punctuation marks to list

#open up a copy of Edgar Allen Poe's The Raven
f = open("/Users/rwebst1/Downloads/sample1.txt","r")

### Let's take all the lines in The Raven and store them in a list!

lines = f.readlines()

### Close the file
f.close()



clean_lines = [] #empty list for lines stripped of newline characters and all characters converted to lowercase

for line in lines: #go through every line in the file
    clean_line = line.strip("\n") #get rid of new-line characters
    clean_line = clean_line.lower() #convert everything to lowercase
    clean_lines.append(clean_line) #add cleaned line to clean_lines

words={} #create empty dictionary for words

for line in clean_lines: #go through every line in the file
    for mark in punctuation_list: #go through every punctuation mark 
        line=line.replace(mark,"") #use replace method to replace each possible punctuation mark with an empty string
    line_words=line.split(" ") #we're using the string split() method to separate each line by space character
    #this converts the line to a list
    #for example: "This is a sentence.".split(" ") --> ['This', 'is', 'a', 'sentence.']
    for word in line_words: #iterate over every word in the line
        if word not in words: # if we haven't seen this word yet
            words[word]=1 #add it to the words dictionary, and mark the count as 1
        else:
            words[word]+=1 #we've already seen this word, so increment the count by 1

new_file = open("/Users/rwebst1/Downloads/sample1_lowercase.txt", "w") #write new file to Documents folder

for line in lines:
    new_file.write(line.lower())

new_file.close()
