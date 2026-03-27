import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path, encoding='latin1')
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None