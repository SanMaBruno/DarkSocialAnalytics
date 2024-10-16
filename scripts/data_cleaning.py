import pandas as pd
import numpy as np
import os
from dateutil import parser

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def handle_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    if 'Watch Time' in df.columns:
        df['Watch Time'] = df['Watch Time'].apply(lambda x: parser.parse(x) if pd.notnull(x) else pd.NaT)
    categorical_columns = ['Gender', 'Location', 'Platform', 'DeviceType', 'OS', 'CurrentActivity', 'ConnectionType']
    df[categorical_columns] = df[categorical_columns].astype('category')
    return df

def detect_and_handle_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    Q1, Q3 = df[column].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    df.to_csv(output_path, index=False)

def clean_data_pipeline(file_path: str, output_path: str) -> None:
    (load_data(file_path)
     .pipe(handle_missing_data)
     .pipe(remove_duplicates)
     .pipe(convert_data_types)
     .pipe(detect_and_handle_outliers, 'Income')
     .pipe(save_cleaned_data, output_path))