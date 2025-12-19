def cal(x,y):
    op = input("Enter the opeartion ( / , + , - , * ) : ")

    if op == "/":
        print(f"Result is : {x / y}")
        return
    
    if op == "+":
        print(f"Result is : {x + y}")
        return
    
    if op == "-":
        print(f"Result is : {x - y}")
        return
    
    if op == "*":
        if y == 0:
            print('Not divisble by zero')
            return
        
        else:
            print(f"Result is : {x * y}")
            return
    

cal(2 , 5)

# def progress():

#     sub1 = int(input("Enter the score for subject 1: "))
#     sub2 = int(input("Enter the score for subject 2: "))
#     sub3 = int(input("Enter the score for subject 3: "))

#     total = (sub1 + sub2 + sub3) / 3

#     if total > 60:
#         print("Progressed")
    
#     else: 
#         print("Need to work hard !")

