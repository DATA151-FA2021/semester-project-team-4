# -*- coding: utf-8 -*-
"""Final Demonstration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mYHBK2Z7Dk2UsglF4IHoKJSeRyqxv7be

## Demonstration
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, BaggingRegressor, AdaBoostClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor

"""## Dataframe"""

df = pd.read_csv('https://raw.githubusercontent.com/DATA151-FA2021/semester-project-team-4/main/data/Final_IMDb_ratings.csv', index_col=0)

df

"""## Distribution of Ratings"""

sns.displot(df, x='avg_vote')
plt.title('Histogram of Average Votes');

"""## Heatmap of Correlations"""

fig = plt.figure(figsize = (10,10))
sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='vlag_r');

"""# Model Demonstration"""

features = df[['duration', 'budget', 'usa_gross_income', 'metascore', 'director_avg']]
X_train, X_test, y_train, y_test = train_test_split(features, df['avg_vote'], test_size=0.3)

"""## Linear Regression"""

regressor = LinearRegression()
regressor.fit(X_train, y_train);

coeff_df = pd.DataFrame(regressor.coef_, features.columns, columns=['Coefficient'])
coeff_df

y_pred = regressor.predict(X_test)

df_test = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df_test

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R^2: ', metrics.r2_score(y_test, y_pred))

"""## Bagging"""

X = StandardScaler().fit_transform(df[['duration', 'budget', 'usa_gross_income', 'director_avg']])
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, df['avg_vote'], test_size=0.3)

regressor = BaggingRegressor(base_estimator=SGDRegressor(), n_estimators=1000, max_samples=35, max_features=4)
regressor.fit(X_train2, y_train2);

y_pred2 = regressor.predict(X_test2)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test2, y_pred2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test2, y_pred2))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test2, y_pred2)))
print('R^2: ', metrics.r2_score(y_test2, y_pred2))

