import pandas as pd
import numpy as np

def predict_sales(df):
    df = df.copy()

    # Prepare data
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])
    df['month'] = df['invoicedate'].dt.to_period('M')

    monthly = df.groupby('month')['totalprice'].sum().reset_index()
    
    if len(monthly) == 0:
        return 0.0

    # Convert month to numeric
    monthly['month_num'] = np.arange(len(monthly))

    X = monthly['month_num'].values
    y = monthly['totalprice'].values

    # Train model (1D Linear Regression via polyfit)
    # deg=1 means a linear fit (y = mx + b)
    # polyfit returns [slope, intercept]
    if len(X) > 1:
        m, b = np.polyfit(X, y, 1)
        # Predict next month
        next_month_num = len(monthly)
        prediction = m * next_month_num + b
    else:
        # If only 1 data point, just return that point
        prediction = y[0]

    return round(prediction, 2)