import json
from country_code import get_country_code
import pygal
from pygal.style import RotateStyle

filename = "populacoes_paises.json"

with open(filename) as f:
	pop_data = json.load(f)

	cc_populations = {}
	for pop_dict in pop_data:

		if pop_dict["Year"]== "2022":

			country_name = pop_dict["Country Name"]
			population = int(float(pop_dict["Value"]))
			code = get_country_code(country_name)

			if code:
				cc_populations[code]=population
				cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}

				for cc, pop in cc_populations.items():
					if pop < 10000000:
						cc_pops_1[cc] = pop
					elif pop < 1000000000:
						cc_pops_2[cc] = pop
					else:
						cc_pops_3[cc] = pop

				wm_style = RotateStyle("#336699")
				wm = pygal.maps.world.World(style=wm_style)
				wm.title = "Populaçao Mundial em 2010, por Paises"
				wm.add("0-10m",cc_pops_1)
				wm.add("10m-1bn",cc_pops_2)
				wm.add(">1bn",cc_pops_3)
				wm.render_to_file("wm.svg")

			else:
				continue
