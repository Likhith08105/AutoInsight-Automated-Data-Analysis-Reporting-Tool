import pandas as pd

def load_csv(file_path):
    """
    Loads CSV file into a pandas DataFrame
    """
    df = pd.read_csv(file_path)
    return df
