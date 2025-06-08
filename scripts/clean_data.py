from utils import load_and_clean_raw

df = load_and_clean_raw(raw_path='data/breast-cancer-wisconsin.data')
df.to_csv('data/cleaned_breast_cancer.csv', index=False)
print(" Cleaned dataset saved to data/cleaned_breast_cancer.csv")
