# import json
#
# username = input("What is your name?")
#
# filename = 'user_name.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")

#整合remember_me.py和greet_user.py的功能
import json

'''这是文档字符串'''

filename = 'user_name.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")