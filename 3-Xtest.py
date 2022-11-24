# Import generic

import pandas as pd

# Import training split

from sklearn.model_selection import train_test_split

# Import cleaned csv

df_clean = pd.read_csv("./data/chronic_disease_db_clean.csv")

# Splitting

X=df_clean.drop(["CKD Yes/No"], axis=1)
y=df_clean["CKD Yes/No"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

try:
    X_train.shape[0]==y_train.shape[0]
    X_test.to_csv("./data/test.csv", index=False)

except:
    print("Something went wrong when splitting")