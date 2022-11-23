# Generic

import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd

# SKlearn
from sklearn.feature_selection import f_classif, SelectKBest
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import classification_report

# Import file

df_clean=pd.read_csv("./data/chronic_disease_db_clean.csv")


# Initialize H2O

from h2o.sklearn import H2OAutoMLClassifier


# Splitting
X=df_clean.drop(["CKD Yes/No"], axis=1)
y=df_clean["CKD Yes/No"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

pipeline = Pipeline([
    ('polyfeat', PolynomialFeatures(degree=2)),
    ('featselect', SelectKBest(f_classif, k=5)),
    ('classifier', H2OAutoMLClassifier(max_models=10, seed=2, sort_metric='aucpr'))
])


# Fitting
pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)

# Accuracy
print(classification_report(y_test, preds))

# Leaderboard
automl = pipeline.named_steps.classifier.estimator
print(automl.leaderboard)
