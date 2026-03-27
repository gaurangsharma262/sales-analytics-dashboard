from data_loader import load_data
from preprocess import clean_data
from analysis import analyze, plot_all
import os

def main():
    # Create folders
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('outputs/plots', exist_ok=True)
    os.makedirs('outputs/reports', exist_ok=True)

    # Base directory
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # File paths
    input_path = os.path.join(base_dir, 'data', 'raw', 'data.csv')
    output_path = os.path.join(base_dir, 'data', 'processed', 'cleaned_data.csv')

    # Load data
    df = load_data(input_path)
    if df is None:
        return

    # Clean data
    df = clean_data(df)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print("✅ Cleaned data saved")

    # Analyze
    results = analyze(df)

    # Print results
    print("\n📊 RESULTS")
    print("Total Revenue:", results['total_sales'])
    print("\nTop Countries:\n", results['country_sales'].head())
    print("\nTop Products:\n", results['top_products'])
    print("\nMonthly Sales Trend:\n", results['monthly_sales'])

    # Save report
    report_path = os.path.join(base_dir, 'outputs', 'reports', 'summary.txt')
    with open(report_path, 'w') as f:
        f.write(f"Total Revenue: {results['total_sales']}\n\n")
        f.write("Top Countries:\n")
        f.write(str(results['country_sales'].head()) + "\n\n")
        f.write("Top Products:\n")
        f.write(str(results['top_products']) + "\n\n")
        f.write("Monthly Sales:\n")
        f.write(str(results['monthly_sales']))

    print("📄 Report saved")

    # Plot graphs
    plot_all(results)
    print("📊 Plots saved")

    print("\n🚀 Project executed successfully!")

if __name__ == "__main__":
    main()