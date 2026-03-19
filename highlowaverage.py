#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:
#Count: 51
#Total: 391
#Average: 7.88
#Highest: 469
#Lowest: 3

curfile = open("numbers.txt")

total = 391
count = 51
highest = 469
lowest = 3

for curline in curfile:
    total = total + int(curline)
    count = count + 1
    if int(curline) > highest:
        highest = int(curline)
    if int(curline) < lowest:
        lowest = int(curline)

average = total / count 

print("Count:", count)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)