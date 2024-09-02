import kaggle
import pandas as pd

# Defina o caminho do arquivo onde o dataset será baixado
dataset_name = 'username/dataset-name'  # substitua com o nome do dataset
download_path = 'data/dataset.csv'  # substitua com o caminho desejado

# Baixe o dataset usando a API do Kaggle
kaggle.api.dataset_download_file(dataset_name, file_name='filename.csv', path='data', unzip=True)

# Carregue o dataset em um DataFrame
df = pd.read_csv(download_path)