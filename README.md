# UreSens: a diagnosis tool to monitor and predict Chronic Kidney Disease



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

- Cleaned dataset from: https://www.kaggle.com/datasets/abhia1999/chronic-kidney-disease
- Original dataset: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
- Paper about this: https://www.hindawi.com/journals/cmmm/2021/6141470/

- Kidney stone original paper: https://link-springer-com.sabidi.urv.cat/chapter/10.1007/978-1-4612-5098-2_45

- Urine pH dataset: https://www.kaggle.com/datasets/zfturbo/measurements-of-urine-ph?select=ph_v1_days.csv
  
- pH recognition dataset: https://www.kaggle.com/datasets/robjan/ph-recognition

- H2O tutorial: https://github.com/h2oai/h2o-tutorials/blob/master/h2o-world-2017/automl/Python/automl_binary_classification_product_backorders.ipynb

- MySQL Connector: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

- Metrics: https://www.mle.hamburg/_repos/dat_sci/11_ml_perf_meas/