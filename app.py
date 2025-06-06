import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carga tus datos (asegúrate que la ruta sea correcta)
try:
    data = pd.read_csv("celsius.csv")
    print(data.info())
    print(data.head())
except FileNotFoundError:
    print("Error: No se encontró el archivo 'celsius.csv'. Verifica la ruta.")
    exit() # Salir si no se encuentra el archivo


# Crea el gráfico (Seaborn devuelve el objeto Axes de Matplotlib)
print("\nCreando el gráfico...")
try:
    ax = sb.scatterplot(x="celsius", y="fahrenheit", data=data, hue="fahrenheit", palette="coolwarm")
    print("Gráfico generado en memoria.")

    # (Opcional) Añadir un título para claridad
    plt.title('Temperatura Celsius vs Fahrenheit')
    plt.xlabel('Grados Celsius')
    plt.ylabel('Grados Fahrenheit')
    plt.grid(True) # Añadir una cuadrícula

    # 2. Muestra la gráfica en una ventana
    print("Mostrando gráfico...")
    # plt.show()
    print("Ventana de gráfico cerrada.")

except ValueError as e:
    print(f"\n--- ERROR AL CREAR EL GRÁFICO: {e} ---")
    print(f"Verifica que las columnas 'celsius' y 'fahrenheit' existan y no tengan errores.")
except Exception as e: # Captura otros posibles errores
    print(f"\n--- OCURRIÓ UN ERROR INESPERADO: {e} ---")


X= data['celsius']
y= data['fahrenheit']

# [-40 -10   0   8  15  22  38]
print(X.values)


X_processed = X.values.reshape(-1,1)
y_processed = y.values.reshape(-1,1)

# [[-40], [-10], [0], [8], [15], [22], [38]]
# print(X_processed)
# print(y_processed)

# Crear modelo
model = LinearRegression()

# Entrenar modelos
model.fit(X_processed, y_processed)

# Hacer la predicción
celsius=7900
result = model.predict([[celsius]])
print(f"{celsius} grados son { result } grados fahrenheit.")

# Nivel de precisión
score = model.score(X_processed, y_processed)
print(score)
