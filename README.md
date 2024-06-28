#  Industrial Copper Modeling Application
## Overview
  This Streamlit application provides predictive modeling for the industrial copper industry. It includes regression and classification models to predict selling prices and order statuses based on various input parameters.

## Features
## Regression Model: 
  Predicts selling prices based on customer, country, item details, and order dates.
## Classification Model: 
  Predicts order status (e.g., Won, Lost) based on customer, country, selling price, and other factors.

  
## Installation and Setup

Clone the repository:

bash
Copy code
git clone <repository-url>

cd industrial-copper-modeling


Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Usage
## Select from the sidebar menu:
## Home: 
  Overview of the application and its purpose.

  
## Regression: 
  Input parameters for regression model predictions.

## Classification: 
  Input parameters for classification model predictions.
  
## Regression Model Inputs

Country: Select the country where the order originates.
Status: Select the current status of the order.
Item Type: Select the type of item being ordered.
Application: Select the application of the item (dropdown from 1 to 100).
Width: Enter the width of the item.
Product Reference: Select the product reference from available options.
Quantity (tons): Enter the quantity in tons.
Thickness: Enter the thickness of the item.
Order Date and Delivery Date: Select the dates for order and delivery.


## Classification Model Inputs

Customer ID: Enter the customer ID (numeric)."\n"
Country: Select the country where the order originates.\n
Selling Price: Enter the selling price of the order.\n
Item Type: Select the type of item being ordered.\n
Application: Select the application of the item (dropdown from 1 to 100).\n
Width: Enter the width of the item.\n
Product Reference: Select the product reference from available options.
Quantity (tons): Enter the quantity in tons.
Thickness: Enter the thickness of the item.
Order Date and Delivery Date: Select the dates for order and delivery.
Predictions
Click on the "Predict" button to see the predicted results based on the chosen inputs.


## Technologies Used
Python
Streamlit
Pandas
NumPy
Scikit-learn
Authors
Sunilkumar A
## License
This project is licensed under the MIT License - see the LICENSE file for details.
