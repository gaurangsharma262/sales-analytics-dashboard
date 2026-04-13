from flask import Flask, render_template, request
import pandas as pd
import os
from src.model import predict_sales

app = Flask(__name__)

def load_data():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, 'data', 'processed', 'cleaned_data.csv')
    df = pd.read_csv(path)
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])
    return df

@app.route('/', methods=['GET', 'POST'])
def home():
    df = load_data()

    # Get the unique countries before filtering happens so the dropdown always has every country
    countries_list = ["All"] + sorted(df['country'].dropna().unique().tolist())

    selected_country = request.form.get('country')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    # Filters
    if selected_country and selected_country != "All":
        df = df[df['country'] == selected_country]

    if start_date:
        df = df[df['invoicedate'] >= start_date]

    if end_date:
        df = df[df['invoicedate'] <= end_date]

    # Metrics
    total_revenue = df['totalprice'].sum()

    country_sales = df.groupby('country')['totalprice'].sum().sort_values(ascending=False).head(5)

    df['month'] = df['invoicedate'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('month')['totalprice'].sum()

    # 🔥 ML Prediction
    predicted_sales = predict_sales(df)

    return render_template(
        'index.html',
        total_revenue=total_revenue,
        predicted_sales=predicted_sales,
        country_labels=list(country_sales.index),
        country_values=list(country_sales.values),
        months=list(monthly_sales.index),
        monthly_values=list(monthly_sales.values),
        country_list=countries_list,
        selected_country=selected_country
    )

if __name__ == '__main__':
    app.run(debug=True)