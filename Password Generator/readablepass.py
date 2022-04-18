#Readable random_password
#Word(min of 5 characters)+Symbol+number
import random,string

wordlist=[]
special_char=['@','#','^','&','!']
with open("wikipediatext.txt","r") as file:
    #to read the number of lines in the paragraph in wikipediatext file
    data=file.readlines()
    #to get all the words by splitting with space
    for each_line in data:
        words= each_line.split()

   #check if the length of the word is greater than 5
   #if it is greater than 5 add it to word list
        for item in words:
            if len(item)>5:
                wordlist.append(item)
#print(wordlist)
#the final readable password is word+special character+random 2 numbers
final_word=random.choice(wordlist)+random.choice(special_char)+str(random.randint(10,99))
print(final_word)
