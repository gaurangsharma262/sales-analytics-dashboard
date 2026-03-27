import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_sales(df):
    df = df.copy()

    # Prepare data
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])
    df['month'] = df['invoicedate'].dt.to_period('M')

    monthly = df.groupby('month')['totalprice'].sum().reset_index()

    # Convert month to numeric
    monthly['month_num'] = np.arange(len(monthly))

    X = monthly[['month_num']]
    y = monthly['totalprice']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next month
    next_month = np.array([[len(monthly)]])
    prediction = model.predict(next_month)[0]

    return round(prediction, 2)