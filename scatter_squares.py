import matplotlib.pyplot as plt
# Plotando pontos individuais 

# plt.scatter(2,4,s=200) Podemos plotar tmb uma serie de pontos

# x_values =[1,2,3,4,5]
# y_values =[1,4,9,16,25]
# plt.scatter(x_values,y_values,s=200)
#Podemos melhorar isso 

x_values = list(range(1,1001))
y_values =[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor="none", s=5)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)
plt.tick_params(axis = "both", which = "major", labelsize = 14)


# A funçao axix() exige os valores minimos e maximos para x e y
# X varia de 0 a 1100 e o eixo y de 0 a 1100000
plt.axis([0,1100,0,1100000])
plt.show()
# Para salvar os graficos ao inves de motras apenas
# plt.savefig("nomedografico.png",bbox_inches="tight")
# O segundo argumento apenas remove espaços vazios no grafico pode ser omitido
