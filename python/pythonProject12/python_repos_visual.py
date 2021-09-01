import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
result = requests.get(url)
print("Status code:", result.status_code)

# 将API响应存储在一个变量中(response_dict是请求的结果的字典)
response_dict = result.json()
print("Total repositories:", response_dict['total_count'])
# print(response_dict.keys())

# 探索有关仓库的信息(repo_dicts是结果中包含的仓库信息的字典)
repo_dicts = response_dict['items']
# # 这里打印的是请求中返回的stars最高的仓库的数量
# print("Repositories returned:", len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333399', base_style = LCS)
# 设置标题、副标签、主标签字体大小
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_config = pygal.Config()
my_config.style = my_style
# 让标签绕x轴旋转45度
my_config.x_label_rotation = 45
# 隐藏图例
my_config.show_legend = False
# 将较长的项目名缩短为15个字符
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
# add中的第一个参数表示数据的标签(这里不需要)
chart.add('', stars)
chart.render_to_file('python_repos.svg')
