import os
import zipfile

zip_file_path = '../data/Plant-Dataset.zip'
extract_dir = '../data'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
    
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)
    
    
print('livia')
