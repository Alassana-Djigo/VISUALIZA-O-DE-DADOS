from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))

	#Controla a largura e altura resoluçao e cor do grafico
	plt.figure(figsize=(10,6))

	#Destacar o ponto inicial e final do passeio
	plt.scatter(0,0,c="red",edgecolor="none",s=20)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",edgecolor="none",s=50)

	#Criando a plotagem e estilizando a mesma e os eixos(x,y)
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor="none",s=1)
	plt.xlabel("Cordenadas de X",fontsize = 14)
	plt.ylabel("Cordenadas de Y",fontsize = 14)
	plt.title("Passeio Aleatorio",fontsize = 24)

	#Remover eixos(x,y)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()
	continuar = input("Gerar outro (s/n) ?")
	if continuar == "n":
		break
