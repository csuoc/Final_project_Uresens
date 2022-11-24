# Final_project_Uresens

# Models

| Model | Auc | Logloss | Aucpr | Mean_per_class_error | RMSE | MSE |
| --- | --- | --- | --- | --- | --- | --- |
| GLM_1 | 1 | 0.00880955 | 1 | 0 | 0.0430218 | 0.00185088 |
| XRT_1 | 1 | 0.010907 | 1 | 0 | 0.0413726 | 0.00171169 |
| GBM_4 | 1 | 0.00530223 | 1 | 0 | 0.0429478 | 0.00184451 |
| GBM_grid_1 | 1 | 6.93856e-05 | 1 | 0 | 0.000675599 | 4.56434e-07 |
| StackedEnsemble_BestOfFamily | 1 | 0.000694444 | 1 | 0 | 0.00779117 | 6.07023e-05 |
| GBM_3 | 1 | 0.00375537 | 1 | 0 | 0.0369249 | 0.00136345 |
| StackedEnsemble_AllModels | 1 | 0.00020144 | 1| 0 | 0.00131683 | 1.73403e-06 |
| GBM_2 | 1 | 0.00391864 | 1 | 0 | 0.0383041 | 0.00146721 |
| DRF_1 | 1 | 0.0138304 | 1 | 0 | 0.0338753 | 0.00114753 |
| GBM_1 | 1 | 0.00421996 | 1 | 0 | 0.0394954 | 0.00155988 |
| GBM_5 | 1 | 0.0032947 | 1 | 0 | 0.035974 0.00129413 |
| DeepLearning | 0.99968  | 0.0400821 | 0.999805 | 0.00666667 | 0.0947045 | 0.00896894 |

# Model metrics
| Auc | Logloss | Aucpr | Mean_per_class_error | RMSE | MSE |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.00880955 | 1 | 0 | 0.0430218 | 0.00185088 |



# Links and Resources

- Cleaned dataset from: https://www.kaggle.com/datasets/abhia1999/chronic-kidney-disease
- Original dataset: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
- Paper about this: https://www.hindawi.com/journals/cmmm/2021/6141470/

- Kidney stone original paper: https://link-springer-com.sabidi.urv.cat/chapter/10.1007/978-1-4612-5098-2_45

- Urine pH dataset: https://www.kaggle.com/datasets/zfturbo/measurements-of-urine-ph?select=ph_v1_days.csv
  
- pH recognition dataset: https://www.kaggle.com/datasets/robjan/ph-recognition

- H2O tutorial: https://github.com/h2oai/h2o-tutorials/blob/master/h2o-world-2017/automl/Python/automl_binary_classification_product_backorders.ipynb