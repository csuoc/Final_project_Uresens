import pandas as pd
from functions.functions import rename_columns, remove_columns, integrify
import seaborn as sns
from matplotlib import pyplot as plt

# Import file

df = pd.read_csv("../data/chronic_disease_db.csv")

# Renaming columns

new_name=["Blood Pressure mm/Hg diastolic", "Specific Gravity", "Albumin (0-5)", "Sugar (0-5)", "Eritrocytes Ok/NOk", "Blood Urea mg/dL", "Serum Creatinine mg/dL", "Na mEq/L", "K mEq/L", "Hemoglobin gms", "White Blood Cell Count cell/cumm", "Red blood cell count mill/cmm", "Hypertension Yes/No", "CKD Yes/No"]
for i,j in zip(df.columns, new_name):
    rename_columns(df, i, j)

# General overview
print("\n")
print ("########### DATA TYPES ###########\n")
print(df.dtypes)
print("\n")

# Sum of NaNs

print ("########### SUM OF NANS ###########\n")
print(df.isna().sum())
print(df.isnull().sum())
print("\n")

# Correlation matrix

print ("########### CORRELATION MATRIX ###########\n")
fig, ax = plt.subplots(figsize=(10,10))  
sns.heatmap(df.corr(), annot=True)
#plt.show()
print("\n")

# Deleting useless columns

to_delete=["Eritrocytes Ok/NOk", "Specific Gravity", "Na mEq/L", "K mEq/L", "Hemoglobin gms", "White Blood Cell Count cell/cumm", "Red blood cell count mill/cmm"]

for i in to_delete:
    remove_columns(df,i)

# Integrify

to_integer=["Blood Pressure mm/Hg diastolic", "Albumin (0-5)", "Sugar (0-5)", "Blood Urea mg/dL", "Hypertension Yes/No", "CKD Yes/No"]
for i in to_integer:
    integrify(df, i)

# New column

df.insert(loc=0, column="Patient", value=list(range(1,401)))

# Exporting

df.to_csv("../data/chronic_disease_db_clean.csv", index=False)