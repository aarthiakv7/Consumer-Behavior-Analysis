import pandas as pd
import numpy as np

def process_marketing_data(file_path):
    # 1. Load Data: Handles both CSV and Excel
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # 2. Functional Cleaning: Method to strip symbols and handle NaNs
    def clean_financials(col):
        return pd.to_numeric(col.replace('[\$,]', '', regex=True))

    # Identify financial columns dynamically (adjust these names to match your file)
    financial_cols = ['Spend', 'Revenue', 'Budget'] 
    for col in [c for c in financial_cols if c in df.columns]:
        df[col] = clean_financials(df[col])

    # 3. Business Logic: Methods for KPI calculation
    df['ROI_pct'] = ((df['Revenue'] - df['Spend']) / df['Spend'] * 100).replace([np.inf, -np.inf], 0).fillna(0)
    
    # 4. Insight Generation: Aggregation Methods
    summary = df.groupby('Campaign').agg({
        'Spend': 'sum',
        'Revenue': 'sum',
        'ROI_pct': 'mean'
    }).sort_values(by='ROI_pct', ascending=False)

    return df, summary

# Usage
# df_detailed, business_summary = process_marketing_data('your_uploaded_file.csv')
# print(business_summary)
