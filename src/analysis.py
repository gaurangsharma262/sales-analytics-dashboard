import matplotlib.pyplot as plt

def analyze(df):
    results = {}

    # 💰 Total Revenue
    results['total_sales'] = df['totalprice'].sum()

    # 🌍 Sales by Country
    results['country_sales'] = df.groupby('country')['totalprice'].sum().sort_values(ascending=False)

    # 🛒 Top Products
    results['top_products'] = df.groupby('description')['totalprice'].sum().sort_values(ascending=False).head(10)

    # 📅 Monthly Sales Trend
    df['month'] = df['invoicedate'].dt.to_period('M')
    results['monthly_sales'] = df.groupby('month')['totalprice'].sum()

    return results


def plot_all(results):
    # 🌍 Country Sales
    results['country_sales'].head(10).plot(kind='bar', title='Top Countries by Sales')
    plt.tight_layout()
    plt.savefig('outputs/plots/country_sales.png')
    plt.clf()

    # 🛒 Top Products
    results['top_products'].plot(kind='bar', title='Top Products')
    plt.tight_layout()
    plt.savefig('outputs/plots/top_products.png')
    plt.clf()

    # 📅 Monthly Sales Trend
    results['monthly_sales'].plot(kind='line', marker='o', title='Monthly Sales Trend')
    plt.tight_layout()
    plt.savefig('outputs/plots/monthly_sales.png')
    plt.clf()