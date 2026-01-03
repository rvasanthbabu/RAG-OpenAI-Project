import pandas as pd

def ingest_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()

