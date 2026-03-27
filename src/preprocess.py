import pandas as pd

def clean_data(df):
    df = df.copy()

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    print("Cleaned Columns:", df.columns)

    # Drop missing values
    df.dropna(inplace=True)

    # Convert data types
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])
    df['quantity'] = pd.to_numeric(df['quantity'])
    df['unitprice'] = pd.to_numeric(df['unitprice'])

    # Create Total Price column
    df['totalprice'] = df['quantity'] * df['unitprice']

    return df