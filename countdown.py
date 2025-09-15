n = 5             #assigning value to n.
while n > 0:      #creating a loop which is telling while n is greater than 0 the loop will continue. But when the value of n is 0 loop will end.
    print(n)      # this is needed because it will show us the value of n and the value of n after step 4 that is n = n -1. If we don't do this step 3, we won't see the updated value of n form step 4. 
    n = n - 1     # this step does the actual work to change the value of n. Because this step in inside the while loop, it will keep repeating itself until the condition is False. I mean it will do 5 -1 = 4, now 4 is the new value of n. Again this step will take place and now it will be 4 - 1 = 3. And this will go on until 1 - 1 = 0. Now this will make the step 2 which is n > 0 False.
print("Blast off!!")     
