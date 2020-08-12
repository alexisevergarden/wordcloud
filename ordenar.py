import pandas as pd

numero = input("Ingrese una id: ")

datos = pd.read_csv('datosfinales.csv', header=0)
da = datos['id']
print(da)

