H = int(input("Enter the number: "))  # "H" is a variable for how higher should I fill the piggy bank. 
                                      # User will input a number of their choice.
total = 0  # this is the total value of the piggy bank. Since nothing is stored inside now that's why total = 0.

for c in range(1, H + 1): # "c" here is the count in range (1, H + 1). For loop will take each value one 
                          # by one till the end of the range (H + 1). The H + 1 here is taken so the value 
                          # entered by the user should be included. Note:- in a range the last value in 
                          # not included by the python. If you want the value of that last number then add +1 to that number.
        total = total + c # this will change the value of total each time. If total is 0 and c is 1 then 
        print("After adding", c, "in total, the updated total is:", total)                 # it will update to total = 1 and then carry forward with these values every time.
print("Final total is: ", total)  # Here we'll print the total of the above step. ", total" is added here so it 
                            #can print the final value of the total for each item in the range by for loop.