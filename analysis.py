import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define the Processing Function
def process_marketing_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Clean column names (removes hidden spaces)
    df.columns = df.columns.str.strip()

    # Functional Cleaning: Method to strip symbols from financial columns
    def clean_financials(value):
        if isinstance(value, str):
            return float(value.replace('$', '').replace(',', ''))
        return value

    # Apply cleaning to your specific spend column
    if 'monthly_spend' in df.columns:
        df['monthly_spend'] = df['monthly_spend'].apply(clean_financials)

    return df

# 2. Set the File Path
file_to_open = "Consumer_Shopping_Trends_2026 (6).csv"

# 3. Run the Process
try:
    df = process_marketing_data(file_to_open)
    print("Data loaded successfully!")
    print(df.head())

    # 4. Behavioral Analysis (Correlation)
    behavioral_cols = ['monthly_spend', 'social_media_usage', 'tech_savvy', 
                      'brand_loyalty', 'impulse_buying', 'return_frequency','need_touch_feel_score']

    # Filter only columns that exist in the file to avoid errors
    existing_cols = [c for c in behavioral_cols if c in df.columns]
    corr_matrix = df[existing_cols].corr()

    # 5. Create and Save the Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0, fmt='.2f')
    plt.title('Consumer Behavior Correlation Matrix', fontsize=16, pad=20)
    plt.tight_layout()
    
    plt.savefig('behavior_heatmap.png')
    print("Heatmap saved as 'behavior_heatmap.png'")
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_to_open}' was not found. Please check the filename.")
except Exception as e:
    print(f"An error occurred: {e}")
