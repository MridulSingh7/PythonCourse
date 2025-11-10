import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

data = pd.read_csv("experience_salary.csv")
X = data[["YearsExperience"]]  
Y = data[["Salary"]]           
model = LinearRegression()
model.fit(X, Y)



#using streamlit
st.title("Salary Predictor based on Experience")
st.write("Enter your years of experience to predict your salary")
years_input = st.number_input("Years of Experience :", min_value=0.0, max_value=40.0, step=0.1)#way to take input


# Prediction block
if years_input:
    predicted_salary = model.predict([[years_input]])[0] #years_input is inside a 2d array so we extract the data like this
    st.success(f"Estimated Salary: ${predicted_salary[0]:,.2f}")

st.subheader("Regression Line:")

# Plotting using matplotlib but display inside Streamlit, iske liye we use subplots
fig, ax = plt.subplots()
ax.scatter(X, Y, color="blue", label="Actual Data")                  # Actual data points
ax.plot(X, model.predict(X), color="red", label="Regression Line")   # Regression line
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Years of Experience")
ax.legend()
st.pyplot(fig)


"""
-----------------------------------------------------------
🧠 COMMENTS / EXPLANATION SECTION
-----------------------------------------------------------

1️⃣ How plotting differs in Streamlit vs. normal Python:
   - In a normal Python script (or Jupyter Notebook), you would use:
       plt.show()
     to render the graph in a window or notebook output cell.
   - In Streamlit, you don’t call plt.show(). Instead, you pass the 
     matplotlib figure object (fig) to:
       st.pyplot(fig)
     Streamlit then handles rendering inside the app interface.

2️⃣ Why we used `fig, ax = plt.subplots()`:
   - This gives more control over the figure and axes, 
     and makes it compatible with Streamlit’s rendering.
   - Avoids global state issues with matplotlib when Streamlit 
     re-runs scripts on input changes.

3️⃣ Key takeaways:
   ✅ Streamlit automatically reruns your script whenever a widget changes, 
      so keep model loading/training outside the dynamic part (as done here).
   ✅ Always use `st.pyplot(fig)` for plotting.
   ✅ Use formatted string output (f-strings) for clear numeric display.
   ✅ Avoid `print()` in Streamlit — use `st.write()`, `st.success()`, etc.
   ✅ The model prediction must be reshaped properly if input is 2D or single value.

4️⃣ Optional improvement ideas:
   - Cache model training with `@st.cache_data` or `@st.cache_resource` 
     to improve performance.
   - Add input validation or allow uploading a CSV file for flexibility.
   - Show prediction history or plot predicted point dynamically on the chart.
-----------------------------------------------------------
"""
