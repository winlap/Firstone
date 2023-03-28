#program to count the numbers of occurence of a word
sentence = input("Enter a sentence: ")


#convert the sentence into lower case
sentence.lower()
#split the sentence into words
word = sentence.split()

#create a dictionary to count the frequecy of the word
mydict = {}

for x in word:
    if x in mydict:
        mydict[x] += 1
    else:
        mydict[x] = 1

#word frequency
for x,words in mydict.items():
    print(x,":",words)


