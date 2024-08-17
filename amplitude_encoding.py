import numpy as np
import pandas as pd

def normalize_row(row, selected_columns):
    values = row[selected_columns].values
    norm = np.linalg.norm(values)
    if norm == 0:
        return row
    row[selected_columns] = values / norm
    return row

def amplitude_encoding(df):
    # Automatically select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    
    # Normalize only the numeric data
    normalized_df = numeric_df.apply(lambda row: normalize_row(row, numeric_df.columns), axis=1)
    
    # Replace the original numeric columns with the normalized data
    for col in numeric_df.columns:
        df[col] = normalized_df[col]
    
    return df
