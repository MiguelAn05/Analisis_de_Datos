import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

try:
    archivo_csv = "datos_categorizados.csv"
    dataframe = pd.read_csv(archivo_csv)

    
    X = dataframe.drop(columns=['DEATH_EVENT', 'age', 'Grupo de Edad'])

    
    y = dataframe['age']

    
    model = LinearRegression()
    model.fit(X, y)

          
    y_pred = model.predict(X)

    
    mse = mean_squared_error(y, y_pred)

    print(f" El error medio es: {mse}")

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")