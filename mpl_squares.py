import matplotlib.pyplot as plt

#Como ele sempre relaciona os primeiro valor a 0 passamos a entrada
input_values = [1,2,3,4,5]

squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

plt.tick_params(axis = "both", labelsize = 14)

plt.show()
