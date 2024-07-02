import os

import pandas as pd
import numpy as np

class DataCleaning:
    def __init__(self, path):
        self.path = path
        self.df = self._read_data()

    def _read_data(self):
        df = pd.read_csv(self.path)
        df.drop(columns=['latitude', 'longitude'], inplace=True)
        return df

    def drop_columns_by_threshold(self, df, threshold=0.8):
        missing_percentage = df.isnull().mean()
        df_cleaned = df.loc[:, missing_percentage <= threshold]
        dropped_columns = [col for col in df.columns if col not in df_cleaned.columns]
        return dropped_columns, df_cleaned
    
    def clean_objects_by_level(df, threshold=100):
        # Select object columns
        object_columns = df.select_dtypes(include=[object]).columns

        # Create a dictionary to store unique counts and their levels
        unique_counts_levels = {}

        # Loop through each object column to get unique counts and levels
        for col in object_columns:
            unique_counts_levels[col] = {
                'unique_count': df[col].nunique(),
                'levels': df[col].unique()
            }
        to_remove_columns = []
        unique_counts_levels
        for key in unique_counts_levels.keys():
            if unique_counts_levels[key]['unique_count'] > threshold:
                to_remove_columns.append(key)

        df_filtered = df.drop(columns=to_remove_columns)
        return df_filtered, to_remove_columns

    def get_cleaned_data():
        pass

if __name__ == '__main__':
    path = '../data/raw/data.csv'
    test_object = DataCleaning(path)