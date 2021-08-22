
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    #去掉字符串前后的空格
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

