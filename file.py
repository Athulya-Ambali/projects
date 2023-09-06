#1. write a function in python to count and display the total number of words in a text file
#2. write a function to read a text file and find the number of times the "the" word occurance 
#3. write a function name display_words and display those words which are less than 4 character(count)
#4.count the words "this" and "these"
#5.the text file that has the words which are ends with "e"
#6.each character seperated with "#"



#1.

#x = open("count.txt",'x')
"""x = open("count.txt",'w')
x.write("write a function in python to count and display the total number of words in the text file these")
x.close()
x = open("count.txt",'r')
count = 0
for i in x:
    words = i.split()
    count = count+len(words)
print("number of words present in the given file =",count)
x.close()"""


#2.

"""x = open("count.txt",'r')
y = x.read()
count = 0
words = y.split()
for i in words:
    if i=="the":
        count = count+1
print("number of times  the word occurance  = ",count)
x.close()"""


#3.

"""def display_words():
    x = open("count.txt",'r')
    y = x.read()
    words = y.split()
    for i in words:
        if len(i)<=4:
            print(i)
display_words()"""

#4.

"""x = open("count.txt",'r')
y = x.read()
count = 0
words = y.split(" ")
for i in words:
    if i=="the" or i=="these":
        count = count+1
print("number of times   word occurance  = ",count)
x.close()"""


#5.

"""x = open("count.txt",'r')
y = x.read()
words = y.split()
for i in words:
    if i.endswith("e"):
        print(i)
x.close()"""


#6.

"""x = open("count.txt",'r')
y = x.read()
char = y.split()
for i in char:
    for j in i:
        print(j,end="#")"""
