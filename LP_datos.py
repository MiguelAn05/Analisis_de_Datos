import pandas as pd

def process_data(df):
    # Verificar que no existan valores faltantes
    assert df.isnull().sum().sum() == 0, "Existen valores faltantes en el DataFrame"

    # Verificar que no existan filas repetidas
    assert df.duplicated().sum() == 0, "Existen filas duplicadas en el DataFrame"

    # Verificar si existen valores atípicos y eliminarlos
    # Aquí se asume que un valor atípico es cualquier valor que esté a más de 3 desviaciones estándar de la media
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            df = df[(df[column] - df[column].mean()).abs() <= 3*df[column].std()]

    # Crear una columna que categorice por edades
    def categorize_age(age):
        if age <= 12:
            return 'Niño'
        elif age <= 19:
            return 'Adolescente'
        elif age <= 39:
            return 'Jóvenes adulto'
        elif age <= 59:
            return 'Adulto'
        else:
            return 'Adulto mayor'

    df['age_category'] = df['age'].apply(categorize_age)

    # Guardar el resultado como csv
    df.to_csv('processed_data.csv', index=False)

    #print('El DataFrame ha sido procesado y guardado como processed_data.csv')

# Uso de la función
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    process_data(df)
