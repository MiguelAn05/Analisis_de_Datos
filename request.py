import requests

def download_data(url):
    response = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, 'w') as f:
        f.write(response.text)

    print(f'Datos descargados y guardados en {filename}')

# Uso de la función
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
download_data(url)
