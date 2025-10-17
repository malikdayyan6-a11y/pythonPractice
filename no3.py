num = int(input("Enter a number: "))
original_num = num
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num = num // 10
if original_num % digit_sum == 0:
    print(f"{original_num} is a Harshad Number")
else:
    print(f"{original_num} is not a Harshad Number")