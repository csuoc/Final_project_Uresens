# Import H2O
import h2o

# Load test
test = h2o.import_file("./data/test.csv")

# Load the model
my_model = h2o.load_model("./models/")

# Predict
predictions = my_model.predict(test)