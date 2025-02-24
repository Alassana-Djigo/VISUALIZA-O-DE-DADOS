from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results=[]
for roll_num in range(50000):
	result = die_1.roll()+die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result + 1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Resultados de girar dois um D6 e outro D10 50000 vezes"

list=[]
for value in range(2,max_result + 1):
	list.append(str(value))
hist.x_labels = list

hist.x_title = "Resultados"
hist.y_title = "Frequencia dos resultados"
hist.add("D6 + D10",frequencies)
hist.render_to_file("die_visual.svg")

