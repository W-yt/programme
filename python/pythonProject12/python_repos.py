import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
result = requests.get(url)
print("Status code:", result.status_code)

# 将API响应存储在一个变量中(response_dict是请求的结果的字典)
response_dict = result.json()
print("Total repositories:", response_dict['total_count'])

print(response_dict.keys())

# 探索有关仓库的信息(repo_dicts是结果中包含的仓库信息的字典)
repo_dicts = response_dict['items']
# 这里打印的是请求中返回的stars最高的仓库的数量
print("Repositories returned:", len(repo_dicts))

# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# # 显示第一个仓库(是一个字典)的keys数量(也就是字典所包含的条目数量)
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# 研究每一个仓库
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print('')
