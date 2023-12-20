from datasets import load_dataset
import numpy as np
import pandas as pd


dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]


# Extrae la lista de edades del conjunto de datos
ages = data['age']

# Convierte la lista a un arreglo de NumPy
ages_array = np.array(ages)

# Calcula el promedio de las edades
average_age = np.mean(ages_array)

print(f'El promedio de edad de las personas participantes en el estudio es {average_age}')

df = pd.DataFrame(data)

# Separa el DataFrame en dos, uno para las personas que perecieron y otro para las que no
df_dead = df[df['is_dead'] == 1]
df_alive = df[df['is_dead'] == 0]

# Calcula el promedio de las edades para cada DataFrame
average_age_dead = df_dead['age'].mean()
average_age_alive = df_alive['age'].mean()

print(f'El promedio de edad de las personas que perecieron en el estudio es {average_age_dead}')
print(f'El promedio de edad de las personas que sobrevivieron en el estudio es {average_age_alive}')

