from die import Die
import pygal

die = Die()

results=[]
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
frequencies = []

for value in range(1,die.num_sides + 1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Resultados de girar um D6 1000 vezes"
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Resultados"
hist.y_title = "Frequencia dos resultados"
hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")
#
