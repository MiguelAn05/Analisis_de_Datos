import requests
import pandas as pd
import argparse

def download_data(url):
    response = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, 'w') as f:
        f.write(response.text)

    print(f'Datos descargados y guardados en {filename}')
    return filename

def convertir_a_dataframe(filename):
    df = pd.read_csv(filename)
    return df

def categorizar_en_grupos(age):
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
    

def exportar_csv(df, filename):
    df.to_csv(filename, index=False)

def main():
    parser = argparse.ArgumentParser(description='Procesa y categoriza datos desde una URL.')
    parser.add_argument('url', type=str, help="https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")
    args = parser.parse_args()

    filename = download_data(args.url)
    df = convertir_a_dataframe(filename)
    df = categorizar_en_grupos(df)
    exportar_csv(df, 'result.csv')

if __name__ == '__main__':
    main()
