#main.py
#Create an empty list
myList = []
'''
print(type(myList))
#Append 42 to the list
myList.append(42)
#How many elements are now in the list?
print(len(myList))
#Add five random ints to the list
import random
for i in range (0,5):
    myList.append(random.randint(0,42))
print("Added 5 ints:", myList)

#Indexing. Square Brackets again
#I want the second element in myList
print(myList[1]) #we index from zero
#I want the last element in myList. Assume you don't know how long the list is
print(myList[-1])#Always the last element!
#Print the second and third elements, using slicing
print("Second and third elements:", myList[1:3])

print(myList[-3:-1])
'''
#Make a tuple with 5 numbers from 5 to 9
myTuple = (5,6,7,8,9) #Why use Tuples? with data that will never / should never change (Tuples are faster than lists too)
print(type(myTuple))
#change the 7 to 99
#myTuple[2] = 99 #Tuples are immutable = CANNOT change elements in a tuple after creation
#Convert the tuple to a list
myNewList = list(myTuple)
print(type(myNewList), myNewList)

#I want a 2x3 (2 rows, 3 columns) data structure 
#Use a list of lists. Initialize 1,2,3,4,...
myMatrix = [[1,2,3], 
            [4,5,6]]
print(myMatrix)
#What is len(myMatrix)? 2 elements (each element is a list)
print(len(myMatrix))
#Change the 5 to 99
myMatrix[1][1] = 99
for row in myMatrix:
    print(row)
    
#I want to model a student at UC
#In a list store
#M Number
#GPA
#One element with HS Grad year and Expected UC Grad year
#Major
ucList = [234253, 
          3.65,
          (2018, 2023),
          "IS"]
print(ucList)
for i in ucList:
    print(type(i))