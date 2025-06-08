import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Original Wisconsin Breast Cancer (WBC) columns
COLUMN_NAMES = [
    'id',
    'clump_thickness',
    'uniformity_of_cell_size',
    'uniformity_of_cell_shape',
    'marginal_adhesion',
    'single_epithelial_cell_size',
    'bare_nuclei',
    'bland_chromatin',
    'normal_nucleoli',
    'mitoses',
    'class'   # 2 = benign, 4 = malignant
]

def load_and_clean_raw(raw_path='data/breast-cancer-wisconsin.data'):
    """
    Load the raw WBC dataset, assign proper names, handle missing values,
    drop 'id', map 'class' to 0/1, and return cleaned DataFrame.
    """
    # Read raw file
    df = pd.read_csv(raw_path, header=None, names=COLUMN_NAMES)
    # Convert '?' to NaN, then drop those rows
    df['bare_nuclei'].replace('?', np.nan, inplace=True)
    df = df.dropna(subset=['bare_nuclei'])
    # Convert all columns except 'class' to numeric
    for col in COLUMN_NAMES[1:-1]:
        df[col] = pd.to_numeric(df[col])
    # Drop 'id'
    df = df.drop(columns=['id'])
    # Map class: 2 → 0 (benign), 4 → 1 (malignant)
    df['class'] = df['class'].map({2: 0, 4: 1})
    # Rename target column
    df = df.rename(columns={'class': 'diagnosis'})
    return df

def split_data(df):
    """
    Given a cleaned DataFrame with a 'diagnosis' column,
    split into X/y train/test sets.
    """
    X = df.drop(columns=['diagnosis'])
    y = df['diagnosis']
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
