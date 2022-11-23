# Import generic
import pandas as pd

# Import training split
from sklearn.model_selection import train_test_split

# Import models
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

# Import scores
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

# Import cleaned csv

df_clean = pd.read_csv("./data/chronic_disease_db_clean.csv")

# Splitting

X=df_clean.drop(["CKD Yes/No"], axis=1)
y=df_clean["CKD Yes/No"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)


# Training

models = {
    "LogisticRegression": LogisticRegression(),
    "Linear Disc Analysis": LinearDiscriminantAnalysis(),
    "KNeighborsClass": KNeighborsClassifier(),
    "GaussianNB" :GaussianNB(),
    "Decision-Tree-classifier": DecisionTreeClassifier(),
    "SVC": SVC(),
    "GradientBoostingClassifier": GradientBoostingClassifier(),
    "RandomForestClassifier" : RandomForestClassifier()
    #"catboostclassifier": CatBoostClassifier()
}

for name, model in models.items():
    print(f"------------------")
    print("Fitting model: ", model)
    model.fit(X_train, y_train)
    print("Predicting model: ", model)
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Precision: {precision_score(y_test, y_pred)}")
    print(f"Recall: {recall_score(y_test, y_pred)}")
    print(f"F1 score: {f1_score(y_test, y_pred)}")