list = [22,33,44,55,66,44,4,44,66,66] #first created a list

count = 0 #count variable
temp = 0 #temporary variable
index = 0
for x in range (0,len(list)): #run from 0 to the length of the list
    temp = list.count(list[x]) # (chekcs frequency of the number)(so if appears 3 time the temp would be 3)

    if (temp>count): #1>0
        count = temp #count=1 (counts the one thats most appeared in the list)
        index = x #index=0

mostFrequentNumber = list[index]
print("The most frequent number of list is: ", mostFrequentNumber) #what is that most frequent number
print("The number appeared", count, "time in list") #how many times it appeared
