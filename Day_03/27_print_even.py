# Print even numbers upto N

n = int(input("Input a number: ")) 
    
#starting with the first even natural number, which will always be 2
i = 2 

#while loop will continue until we reach user-inputted n times
while i <= n:
        print(i) #will print i (which will be always be 2 for the first round)
        i += 2 #bc you only want even natural numbers, will add 2 to each iteration for even


 