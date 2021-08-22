filename = 'programming.txt'

#写入模式——write mode
with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games!\n")

#追加模式——append mode
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in s browser.\n")
