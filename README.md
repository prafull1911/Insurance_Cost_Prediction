# Insurance Premium Prediction Model

## Contents
- [Introduction](#introduction)
- [Objective](#objective)
- [Concepts Used](#concepts-used)
- [Column Profiling](#column-profiling)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Hypothesis Testing](#hypothesis-testing)
- [Feature Engineering](#feature-engineering)
- [Data Pre-processing](#data-pre-processing)
- [Modeling](#modeling)
- [Model Performance Comparison](#model-performance-comparison)
- [Conclusion](#conclusion)
- [GitHub Repository and Tableau Dashboard](#github-repository-and-tableau-dashboard)
- [Deployment](#deployment)

---

## Introduction
This project implements an **insurance premium prediction model** that leverages various health and demographic features to accurately estimate insurance premiums based on individual health risk factors. Using robust machine learning techniques, this model aids insurers in setting data-driven premium prices while helping customers understand factors affecting their insurance costs.

## Objective
1. **Enhance Pricing Accuracy**: Develop a data-driven pricing strategy, allowing insurers to set competitive and fair premiums based on unique risk profiles.
2. **Support Risk Assessment**: Equip insurers with insights into health risks, improving underwriting and tailoring insurance offerings.
3. **Improve Customer Insights**: Empower customers to understand the impact of health attributes on their premiums, encouraging informed health choices.

The model serves as a powerful tool for both insurers and customers, aligning premium prices with personalized health assessments.

---

## Concepts Used
- **Data Cleaning and Pre-processing**
- **Exploratory Data Analysis (EDA)**
- **Hypothesis Testing** using Scipy for statistical tests
- **Ensembling Techniques** for predictions, including:
  - **Bagging** (Random Forest Regressor)
  - **Boosting** (Gradient Boosting Decision Tree, XGBoost)

---

## Column Profiling
Each feature in the dataset contributes valuable information for predicting insurance premiums:

1. **Age**
   - Type: Numerical
   - Description: Age of the individual in years.

2. **Diabetes**
   - Type: Binary (0 or 1)
   - Description: Indicates if the individual has diabetes (1) or not (0).

3. **BloodPressureProblems**
   - Type: Binary (0 or 1)
   - Description: Indicates if the individual has blood pressure issues (1) or not (0).

4. **AnyTransplants**
   - Type: Binary (0 or 1)
   - Description: Indicates if the individual has undergone any transplants (1) or not (0).

5. **AnyChronicDiseases**
   - Type: Binary (0 or 1)
   - Description: Indicates if the individual has any chronic diseases (1) or not (0).

6. **Height**
   - Type: Numerical
   - Description: Height of the individual in centimeters.

7. **Weight**
   - Type: Numerical
   - Description: Weight of the individual in kilograms.

8. **KnownAllergies**
   - Type: Binary (0 or 1)
   - Description: Indicates if the individual has known allergies (1) or not (0).

9. **HistoryOfCancerInFamily**
   - Type: Binary (0 or 1)
   - Description: Indicates if there is a family history of cancer (1) or not (0).

10. **NumberOfMajorSurgeries**
   - Type: Categorical (Ordinal: 0, 1, 2, 3)
   - Description: Number of major surgeries undergone.

11. **PremiumPrice** (Target Variable)
   - Type: Numerical (Continuous)
   - Description: The predicted insurance premium price.

---

## Exploratory Data Analysis
Conducted thorough EDA to understand data distributions, relationships, and key patterns. Various visualizations were created to gain insights into how each feature impacts the premium price.

## Hypothesis Testing
To evaluate the statistical significance of relationships within the data, the following tests were performed:
- **Independent T-test**: Assessed differences between two independent groups.
- **Kruskal-Wallis Test**: Compared medians across multiple groups.
- **Mann-Whitney U test**: Tested differences between two independent samples.

## Feature Engineering
New features were derived from existing ones to enhance predictive power. This step involved calculating BMI and categorizing several features based on domain insights.

## Data Pre-processing
- **Train-Test Split**: Dataset was divided into training and testing sets.
- **Scaling**: Used **Robust Scaler** to normalize features, making the model more robust against outliers. The scaling parameters were saved in a `.pkl` file to ensure consistency for future data.

## Modeling
The model utilized **Ensembling Techniques** to improve accuracy:
- **Bagging**: Implemented using **Random Forest Regressor**.
- **Boosting**: Applied **Gradient Boosting Decision Tree (GBDT)** and **XGBoost**.
- **Hyperparameter Tuning**: GridSearchCV was used to optimize model parameters for each technique.

## Model Performance Comparison
Each model was evaluated on key metrics to compare performance and select the best-performing model. The tuned models offered insights into which features contributed the most to the premium price prediction.

## Conclusion
The insurance premium prediction model leverages health and demographic data to provide a data-driven pricing strategy. By aligning premiums with individual health profiles, this model assists insurers in creating personalized and fair offerings.

## GitHub Repository and Tableau Dashboard
- Access the code and dataset on [GitHub](https://github.com/prafull1911/Insurance_Cost_Prediction).
- Explore the interactive **Tableau Dashboard** for insights on premium pricing trends and feature impacts: [Insurance Premium Dashboard](https://public.tableau.com/app/profile/prafull.almale/viz/Insurance_sample_17282171342300/Insurance_Premium_Dashboard).

## Deployment
The model was deployed using **Streamlit** for an interactive user interface, allowing users to input health-related attributes and receive premium price predictions in real-time. Check it out here: [Insurance Cost Prediction App](https://prafull1911-insurance-cost-pre-deploymentinsurance-price-9fnwrb.streamlit.app/).
