import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    archivo_csv = "datos_categorizados.csv"
    dataframe = pd.read_csv(archivo_csv)

    

    # Eliminar valores faltantes
    dataframe.dropna(inplace=True)

    # Eliminar filas duplicadas
    dataframe.drop_duplicates(inplace=True)

    # Filtrar los valores atípicos usando el método del rango intercuartil (IQR)
    Q1 = dataframe['age'].quantile(0.25)
    Q3 = dataframe['age'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    dataframe = dataframe[(dataframe['age'] >= lower_bound) & (dataframe['age'] <= upper_bound)]

    men_data = dataframe[dataframe['sex'] == 1]
    women_data = dataframe[dataframe['sex'] == 0]

    plt.figure(figsize=(12, 6))
    plt.hist(men_data['age'], bins=20, color='darkblue', alpha=0.5, label='Hombres', edgecolor='black')
    plt.hist(women_data['age'], bins=20, color='darkred', alpha=0.5, label='Mujeres', edgecolor='black')
    plt.title('Distribución de Edades por Sexo')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()

    categories = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
    men_counts = [men_data[category].sum() for category in categories]
    women_counts = [women_data[category].sum() for category in categories]

    x = np.arange(len(categories))  # the label locations

    plt.figure(figsize=(12, 6))
    plt.bar(x - 0.2, men_counts, color='darkblue', width=0.4, label='Hombres', alpha=0.6)
    plt.bar(x + 0.2, women_counts, color='darkred', width=0.4, label='Mujeres', alpha=0.6)
    plt.xticks(x, categories)
    plt.xlabel('Categorías')
    plt.ylabel('Cantidad')
    plt.title('Distribución de Categorías por Sexo')
    plt.legend()
    plt.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")
