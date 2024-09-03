import kaggle
import pandas as pd

dataset_name = 'username/dataset-name'
download_path = 'data/dataset.csv'

kaggle.api.dataset_download_file(dataset_name, file_name='filename.csv', path='data', unzip=True)

df = pd.read_csv(download_path)