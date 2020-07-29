import json
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

filename = 'json/population_data.json'
with open(filename) as file_object:
    pop_data = json.load(file_object)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 roku'
wm.add('0-10 mln', cc_pops_1)
wm.add('10mln-1mld', cc_pops_2)
wm.add('>1mld', cc_pops_3)
wm.render_to_file('world_population.svg')