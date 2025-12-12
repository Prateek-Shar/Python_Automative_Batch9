num = int(input("Enter the number : "))
original_num = num
sum_of_cubes = 0

while(num!=0):
    rem = num%10
    sum_of_cubes = sum_of_cubes + (rem**3)
    num = num // 10

if(sum_of_cubes == original_num):
    print("It is an armstrong number")

else:
    print("It's not an armstrong number")