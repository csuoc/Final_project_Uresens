# Import H2O
import h2o
h2o.init()

# Load test
test = h2o.import_file("./data/test.csv")

# Load the model
my_model = h2o.load_model("./models/GLM_1_AutoML_1_20221124_124917")

# Predict
predictions = my_model.predict(test)