
#
# Task
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for.
# For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for  is not found, print Not found instead.
#
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.


n = int(input())
i = 0
book = dict() #Declare a dictionary
while(i < n):
    name , number = input().split() #Split input for name,number
    book[name] = number #Append key,value pair in dictionary
    i+=1
while True: #Run infinitely
    try:
        #Trick - If there is no more input stop the program
        query = input()
    except:
        break
    val = book.get(query, 0) #Returns 0 is name not in dictionary
    if val != 0:
        print(query + "=" + book[query])
    else:
        print("Not found")
