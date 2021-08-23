#handle the ZeroDivisionError exception

# print(5/0)
#报错如下：
# Traceback (most recent call last):
#   File "E:/Project/programme/python/pythonProject4/division.py", line 2, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#--------------------------------------------------

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


