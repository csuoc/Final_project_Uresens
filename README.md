# UreSens: a diagnosis tool to monitor and predict Chronic Kidney Disease

Chronic kidney disease is a progressive condition that affects >10% of the general population worldwide, amounting to >800 million individuals. Chronic kidney disease is more prevalent in older individuals, women, racial minorities, and in people experiencing diabetes mellitus and hypertension. 

The disease represents an especially large burden in low- and middle-income countries, which are least equipped to deal with its consequences. Chronic kidney disease has emerged as one of the leading causes of mortality worldwide, and it is one of a small number of non-communicable diseases that have shown an increase in associated deaths over the past 2 decades. The high number of affected individuals and the significant adverse impact of chronic kidney disease should prompt enhanced efforts for better prevention and treatment.

<img src="./images/readme/infographic.jpg">

The diagnosis of CKD is made by laboratory testing, most often by estimating glomerular filtration rate (GFR) from a filtration marker, such as serum creatinine or cystatin C, using various formulas, or by testing urine for the presence of albumin or protein (or a combination of these)(**Kidney Int Suppl. 2013; 3: 1-150**)

Most studies have used estimated GFR (eGFR) to determine the presence of CKD (and, therefore, report on the prevalence of CKD stages 3–5), whereas other studies have combined albuminuria (typically defined as an albumin-to-creatinine ratio of >30 mg/g) and decreased eGFR to report on CKD stages 1–5. Finally, to differentiate CKD (which is considered to be a chronic progressive disease) from conditions such as acute kidney injury or from transient fluctuations in kidney function unrelated to kidney damage, the standard definition of CKD includes a so-called “chronicity criterion” (i.e., that the low eGFR or elevated urine albumin should be detectable for at least 90 days, requiring the presence of repeated measurements over time). **There is currently no consensus on the length of time used in the assessment of CKD when applying the chronicity criterion, with epidemiologic studies applying various algorithms, from single measurements to any repeated measurements past 90 days, or limiting the repeated measurement(s) to 90 to 365 days, and from requiring consecutive repeated markers of CKD to accepting CKD markers interspersed with markers not conforming to CKD criteria.**

# 1. Objective

Find, clean and train data from patients with Chronic Kidney Disease to monitor the biomarkers from urine and possibly predict and detect early stages of Chronic Kidney Disease with a single urinanalysis test.

# 2. Repo contents



# 3. Data acquisition

The data was taken from the Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease

A clean version of this dataset was also found on Kaggle: https://www.kaggle.com/datasets/abhia1999/chronic-kidney-disease. This is actually the dataset I took as reference.

This is how the data looked like:

<img src="./images/readme/df.JPG">

The data contains 400 rows and 14 columns. Each column name is the abbreviation of one parameter:

- **Bp:** blood pressure (mm/Hg)
- **Sg:** specific gravity (adimensional)
- **Al:** albumin (level 0-5, adimensional)
- **Su:** glucose (level 0-5, adimensional)
- **Rbc:** red blood cells, 1=good level, 0=bad levels
- **Bu:** blood urea (mg/dL)
- **Sc:** serum creatinine (mg/dL)
- **Sod:** sodium (mEq/L)
- **Pot:** potassium (mEq/L)
- **Hemo:** hemoglobin (gms)
- **Wbcc:** white blood cells count (cells/cumm)
- **Rbcc:** red blood cells count (millions/cmm)
- **Htn:** 1=has hypertension; 0=doesn't have hypertension
- **Class:** 1=has CKD; 0=doesn't have CKD

# 4. Data cleaning

```
You can have a look at the cleaning step in /tools/1-Cleaning.py
```

The first step was to rename the columns in order to properly understand what is our data. This was made by appling the custom function rename_columns().

I also looked for NaNs and nulls, which were 0 in both cases.

In order to understand how variables correlate, it was convenient to calculate the adjusted Pearson correlation coefficent.

<img src="./images/readme/dfcorr.jpeg">

It was clear that there are positive-related variables and negative-related. For the purpose of this work, **only positive parameters and/or parameters that can be detected by a urine test were kept.**

Therefore, the final variables are:

- Blood pressure
- Albumin
- Glucose
- Erythrocytes
- Hypertension
- Class

A new column, "Patient", was added in order to be the Primary Key in the MySQL database. This columns was not taken in order to perform machine learning.

<img src="./images/readme/dfcleancorr.png">

```
The result was exported in data/chronic_disease_db_clean.csv
```

# 5. Machine Learning: modelling the data

The model training was executed with H2O Auto ML

 <p style="text-align:center;"><img src="https://docs.h2o.ai/h2o/latest-stable/h2o-docs/_images/h2o-automl-logo.jpg" width=150></p>

 H2O is an open source, in-memory, distributed, fast, and scalable machine learning and predictive analytics platform that allows to build machine learning models on big data.

H2O AutoML is designed to have as few parameters as possible so that all the user needs to do is point to their dataset, identify the response column and optionally specify a time constraint or limit on the number of total models trained.

The steps to train the data were:

- Initialize H2O service
  ```python
  import h2o
    from h2o.automl import H2OAutoML
    h2o.init()
  ```
- Import the cleaned dataset as a H2O dataframe
  ```python
  h2o.import_file
  ```
- Drop the Patient column
  
- Factorizing the class columns: H2O needs to transform the binary columns into an ENUM class. This is made by applying a .asfactor and ovewritting the column type. The data isn't transformed anyhow, just the column type for internal purposes. This is step is really imporant, it changes the behavior of the model.
  ```python
  df["column"]=df["column"].asfactor()
  ```
- Identify the y_train and x_train columns:
  ```python
    y = "CKD Yes/No"
    x = df.columns
    x.remove(y)
    ```

# Model metrics
| Auc | Logloss | Aucpr | Mean_per_class_error | RMSE | MSE |
| --- | --- | --- | --- | --- | --- |
| 0.963173 | 0.202759 | 0.98234 | 0.0626667 | 0.242937 | 0.00185088 | 0.0590182 |

H2O provides a variety of metrics that can be used for evaluating models:

- **AUC (Are under the ROC curve):** It’s a way of measuring the performance of a binary classifier by comparing the False Positive Rate (FPR x-axis) to the True Positive Rate (TPR y-axis). An AUC of 1 indicates a perfect classifier, while an AUC of .5 indicates a poor classifier, whose performance is no better than random guessing. This is the default measure for the leaderboard.
<br>

- **Logloss:** Logarithmic loss. Measures the performance of a classifier by comparing the class probability to actual value (1 or 0). Unlike AUC which looks at how well a model can classify a binary target, logloss evaluates how close a model’s predicted values (uncalibrated probability estimates) are to the actual target value. Logloss can be any value greater than or equal to 0, with 0 meaning that the model correctly assigns a probability of 0% or 100%.
<br>

- **AUCPR (Area under the Precision-Recall curve):** This model metric is used to evaluate how well a binary classification model is able to distinguish between precision recall pairs or points. The main difference between AUC and AUCPR is that AUC calculates the area under the ROC curve and AUCPR calculates the area under the Precision Recall curve. The Precision Recall curve does not care about True Negatives.
Evaluation metrics for regression models (rmse, mse, …) are also calculated for classification problems.

# Links and Resources

- https://www.kisupplements.org/article/S2157-1716(21)00066-6/fulltext
  
- Cleaned dataset from: https://www.kaggle.com/datasets/abhia1999/chronic-kidney-disease

- Paper about this: https://www.hindawi.com/journals/cmmm/2021/6141470/

- Kidney stone original paper: https://link-springer-com.sabidi.urv.cat/chapter/10.1007/978-1-4612-5098-2_45

- Urine pH dataset: https://www.kaggle.com/datasets/zfturbo/measurements-of-urine-ph?select=ph_v1_days.csv
  
- pH recognition dataset: https://www.kaggle.com/datasets/robjan/ph-recognition

- H2O tutorial: https://github.com/h2oai/h2o-tutorials/blob/master/h2o-world-2017/automl/Python/automl_binary_classification_product_backorders.ipynb

- MySQL Connector: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

- Metrics: https://www.mle.hamburg/_repos/dat_sci/11_ml_perf_meas/