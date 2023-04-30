# make a simple calculator that perfroms +,-,*,/
'''
this is simple calculator that performs 10 operations
Features: 
-- Ask the user for kind of operation
-- Take the no of Operands
-- No of operands always +ve so it takes integer
-- it handles exceptional error like value error 
-- reprompt the user if the user do not type the required input
'''
import math
import statistics
def main():
    print("******* THIS IS SIMPLE CALCULATOR *******")
    print("1. --- ADDITION ---")
    print("2. --- SUBTRACTION ---")
    print("3. --- MULTIPLICATION ---")
    print("4. --- DIVISION ---")
    print("5. --- SQUARE ROOT OF A NUMBER ---")
    print("6. --- POWER OF A NUMBER ---")
    print("7. --- PERCENT OF A NUMBER ---")
    print("8. --- AVERAGE OF NUMBER ---")
    print("9. --- PERCENTAGE OF MARKS ---")
    print("10.--- FACTORIAL OF NUMBER ---")

    operation = 0
    # list_of = ["1","1","2","3","4","5","6","7","8","9","10"]
    operlist = []
    # while list_of.count(operation) == 0:
    #     operation = input("Type Relevant No For Operation\n")
    # operation = operation.lstrip()
    operation = handler_int("Type Relevant No For Operation\n")

    if operation==1:
        operands = handler_int("Enter the No of Operands \n")
        for o in range(operands):
            ui = handler_float("Enter operand " + str(o+1) + " ")
            operlist.append(ui)
        print("The sum is ", add(operlist), sep="") 
        
    elif operation==2:
        sub1 = handler_float("Subtract From : ")
        sub2 = handler_float("Subtract with : ")
        difference = (sub1 - sub2)
        print("The difference is", difference)
       
    elif  operation==3:
        operands = handler_int("Enter the No of Operands \n")
        for o in range(operands):
            ui=handler_float("Enter operand " + str(o+1) + ":" + " ")
            operlist.append(ui)
        product = math.prod(operlist)
        print(f"The product is :{product:.2f}")
        
    elif operation ==4:
        divident = handler_float("Enter Divident: ")
        divisor = handler_float("Enter Divisor: ")
        answer  = float((divident/divisor))
        print("The division is:", answer)
        
    elif operation ==5:
        number = float(input("Enter number to get the square root : "))
        print(f"The square root of {number} is ",math.sqrt(number))

    elif operation==6:
        base = handler_float("Enter Base : ")
        expo = handler_float("Enter Exponent : ")
        r = 1
        i = 0
        while i < expo:
            r = r * base
            i+=1
        print(f"The power of {base} is {r:.1f}")
    elif operation==7:
        n1 = handler_float("Enter Number ")
        p1 = handler_float("Enter Percent ")
        percent_of_n = n1 * (p1/100)
        print(f"The {p1}% of {n1} is : {percent_of_n:.2f}")
    
    elif operation==8:
        operands = handler_int("Enter the No of Operands \n")
        for o in range(operands):
            ui = float(input(" Enter operand : " + str(o+1) + " "))
            operlist.append(ui)
        print(f"The average of a Number : {average(operlist, operands):.2f}")
        # print(statistics.mean(operlist)) # Statistic module mean function
        
    elif operation==9:
       operands = handler_int("Enter the No of Subjects\n")
       for o in range(operands):
            ui = handler_float("Enter Marks of Subject" + str(o+1) + " ")
            operlist.append(ui)
       total = handler_int("Enter Total Marks : ")
       print("The percentage is", str(percentage(operlist, total)) + "%")
    
    elif operation==10:
       num_f = handler_int(prompt="Enter number : ")
       print(f"The factorial of {num_f} is {factorial(num_f)}")
    
            
def add(n):  # My function to Add the list of numbers
    addition = sum(n)
    return addition

def average(listofN,opr):   # My function to Calculate average of numbers
    s_for_avg = (add(listofN))/opr
    return s_for_avg

def percentage(listofNum, total_m,): # function to calculate percentage of marks
    result = (sum(listofNum))/total_m * 100 # logic for percentage
    return result

def factorial(n): # My func to calculate factorial
    x=1
    for i in range(1,n+1):
      x = x * i  
    return x      
    
# this is my function that take integer as strings input and 
# convert that into integers if not provided that req input it will
# reprompt the user again and again
def handler_int(prompt):  
    while True:  
        try:  
            x=int(input(prompt))
            break
        except ValueError:
            pass
    return x
# this is my function that take float as strings input and 
# convert that into float, if the user not provided that req input it will
# reprompt the user again and again
def handler_float(prompt):
    while True:
        try:
            x = (input(prompt))
            x = x.replace("%", "")
            x = float(x)
            break
        except ValueError:
            pass
    return x
    
    
main()