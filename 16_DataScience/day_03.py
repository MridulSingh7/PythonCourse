import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Load dataset
data = pd.read_csv("experience_salary.csv")  # Load CSV file into a DataFrame

#Separated independent (X) and dependent (Y) variables
X = data[["YearsExperience"]]  
Y = data[["Salary"]]           

#creating a model of linear
model = LinearRegression()
model.fit(X, Y)

#Predicted salaries using the trained model
data["PredictedSalary"] = model.predict(X)  # Model predictions based on X

#Display model's parameters like slope and base salary
print("Model's coefficient (slope_of_graph) -", round(model.coef_[0][0], 2))
print("Model's intercept (base_Salary) -", round(model.intercept_[0], 2))

# Step 6: Visualize actual vs predicted data
plt.scatter(X, Y, color="blue", label="Actual Data")                  # Actual data points
plt.plot(X, data["PredictedSalary"], color="red", label="Regression Line")  # Predicted line
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
🔹 Explanation of Code Flow and Keywords

1️⃣ import numpy, pandas, matplotlib, sklearn.linear_model:
   - Import essential libraries:
     • numpy → numerical calculations
     • pandas → data handling
     • matplotlib → plotting graphs
     • sklearn.linear_model → machine learning model (LinearRegression)

2️⃣ pd.read_csv("experience_salary.csv"):
   - Loads the CSV file into a pandas DataFrame named 'data'.
   - Each column (YearsExperience, Salary) becomes accessible by name.

3️⃣ X = data[["YearsExperience"]]
   - Extracts the independent variable (feature).
   - Double brackets make sure X remains a 2D DataFrame (not a Series).

4️⃣ Y = data[["Salary"]]
   - Extracts the dependent variable (label/target) for training.

5️⃣ model = LinearRegression()
   - Creates a linear regression model object from sklearn.

6️⃣ model.fit(X, Y)
   - Trains (fits) the model on data — finds the best slope and intercept.

7️⃣ data["PredictedSalary"] = model.predict(X)
   - Uses the trained model to predict salaries for all X values.
   - Stores predicted results in a new column 'PredictedSalary'.

8️⃣ print(model.coef_, model.intercept_)
   - coef_ → slope of the regression line (change in Salary per year)
   - intercept_ → base salary when experience = 0
   - rounded to 2 decimal places for clarity.

9️⃣ Plot Section:
   - plt.scatter(X, Y) → plots actual salary points (blue dots).
   - plt.plot(X, data["PredictedSalary"]) → draws regression line (red).
   - Labels, title, legend, grid, and layout formatting are added.

🎯 Overall Flow:
   Load → Split → Train → Predict → Display → Visualize
   The regression line visually shows how salary increases with experience.
"""
