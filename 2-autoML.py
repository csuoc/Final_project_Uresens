# Generic

import warnings
warnings.filterwarnings(action='ignore')

# Initialize H2O

import h2o
from h2o.automl import H2OAutoML
h2o.init()

# Import cleaned csv into H2O
df = h2o.import_file("./data/chronic_disease_db_clean.csv")

# Encoding columns

df["Blood Pressure mm/Hg diastolic"] = df["Blood Pressure mm/Hg diastolic"].asfactor()
df["Albumin (0-5)"] = df["Albumin (0-5)"].asfactor()
df["Sugar (0-5)"] = df["Sugar (0-5)"].asfactor()
df["Blood Urea mg/dL"] = df["Blood Urea mg/dL"].asfactor()
#df["Serum Creatinine mg/dL"] = df["Serum Creatinine mg/dL"].asfactor()
df["Hypertension Yes/No"] = df["Hypertension Yes/No"].asfactor()
df["CKD Yes/No"] = df["CKD Yes/No"].asfactor()

# Splitting
y = "CKD Yes/No"
x = df.columns
x.remove(y)

# AUTOML
aml = H2OAutoML(max_models = 10, seed = 1)
aml.train(x = x, y = y, training_frame = df)

# Leaderboard
lb = aml.leaderboard
print(lb.head(rows=lb.nrows))

# Save model

h2o.save_model(aml.leader, path = "./models/XRTh2omodel")

