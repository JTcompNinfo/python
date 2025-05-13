import random
#loop
count = 0
while (count == 0):
    print("///////////////////////////////////////////////////////")
	#What sided die and how many
    b = int(input("What sided dice do you want to roll? "))
    if b <= 1:
        print("Invalid number making it 2")
        b = 2
    i = int(input("How many dice do you want to roll? "))

	# generate n random integers between a and b
    n = i
    a = 1
    rand_nums = [random.randint(a, b) for _ in range(n)]
 
	# calculate the sum of the random integers
    rand_sum = sum(rand_nums)
    
	# print the results
    print("Dice rolls:", rand_nums)
    print("Sum of rolls:", rand_sum)
    
	#Crits
    if rand_sum == n* a:
    	print("Womp Womp, You crit fail :(")
    if rand_sum == n* b:
    	print("Yippe you crit :)")
    
    end = int(input("Do you want to end the program? \n1 Yes \n2) No \n"))
    if end == 1:
        count = 1