import os

print("Hello world")
myList = [1, 2, 3, 'Hello']
print (myList[2])
print (myList[-1])
myList = myList[1:3]
print (myList)
#age = input("Age:")
#name = input("Name:")
#print("Name and age is :", age, name)
userInput = 2
#input('Enter 1 or 2: ')
if userInput == "1": 
    print ("Hello World") 
    print ("How are you?") 
elif userInput == "2": 
    print ("Python Rocks!") 
    print ("I love Python") 
else:
    print ("You did not enter a valid number")
pets = ['dogs', 'rabbits', 'squirrels']
for index, pet in enumerate(pets):
    print(index, pet)
for i in range (3, 10):
    print(i)
#ZeroDivisionError, ValueError - casting, IndexError - sequence (e.g. string, list, tuple) index is out of range, 
# KeyError - dictionary key is not found. TypeError - operation or function is applied to an object of inop type.
def ifPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False 
        else:
             return True

answer = ifPrime(12)
print(answer)
#Files
fw = open('readdoc.txt', 'a')
fw.write('Adding a line \n')
fw.close()

f = open('readdoc.txt', 'r') #binary - rb, wb
#for line in f:
#    print(line, end = '') #specify not to add a \n after each line

fcopy = open('copy.txt', 'w')
readWithLimit = f.read(4)
while len(readWithLimit):
    fcopy.write(readWithLimit)
    readWithLimit = f.read(4)
fcopy.close()
f.close()
os.rename('hello.py', 'brushbasics.py')