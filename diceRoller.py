import random
# Loop
count = 0
while (count == 0):
    print("///////////////////////////////////////////////////////")
    # What sided die and how many
    b = int(input("What sided dice do you want to roll?"))
    if b <= 1:
        print("invalid number making it 2")
        b = 2
    i = int(input("How many dice would you like to roll?"))
    #Genrate n random integers between a and b
    n = i
    a = 1
    ran_nums = [random.randint(a, b) for _ in range(n)]