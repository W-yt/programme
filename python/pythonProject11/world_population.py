import json
import pygal_maps_world.maps
from country_code import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_poppulations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ": " + str(population))
        code = get_country_code(country_name)
        if code:
            cc_poppulations[code] = population
        else:
            print("ERROR - " + country_name)

# 根据人口数量将所有的国家分程三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_poppulations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# wm_style = RotateStyle('#336699')
wm_style = RotateStyle('#336699', base_style = LightColorizedStyle)
wm = pygal_maps_world.maps.World(style = wm_style)
wm.title = "World Population in 2010, by Country"
# wm.add('2010', cc_poppulations)
wm.add('0 - 10million', cc_pops_1)
wm.add('10million - 1billion', cc_pops_2)
wm.add('1billion - ', cc_pops_3)

wm.render_to_file('world_population.svg')