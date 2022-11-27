# Generic

import warnings
warnings.filterwarnings(action='ignore')

# Initialize H2O

import h2o
from h2o.automl import H2OAutoML
h2o.init()

# Import cleaned csv into H2O

df = h2o.import_file("data/chronic_disease_db_clean.csv")
df = df.drop("Patient", axis=1)

# Factorizing class columns

df["Eritrocytes Ok/NOk"] = df["Eritrocytes Ok/NOk"].asfactor()
df["Albumin (0-5)"] = df["Albumin (0-5)"].asfactor()
df["Sugar (0-5)"] = df["Sugar (0-5)"].asfactor()
df["Hypertension Yes/No"] = df["Hypertension Yes/No"].asfactor()
df["CKD Yes/No"] = df["CKD Yes/No"].asfactor()

# Defining target and dataframe to train

y = "CKD Yes/No"
x = df.columns
x.remove(y)

# Execute AUTOML

aml = H2OAutoML(max_models = 10, seed = 2, balance_classes = True)
aml.train(x = x, y = y, training_frame = df)

# Leaderboard

lb = aml.leaderboard
print(lb.head(rows=lb.nrows))

# Save first (and best) model

h2o.save_model(aml.leader, path = "./models")
