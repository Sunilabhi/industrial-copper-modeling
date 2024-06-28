import pandas as pd
import numpy as np
import streamlit as st
import pickle
import datetime
from datetime import date
from streamlit_option_menu import option_menu

# Load your models (assuming you have saved them as 'regression_model.pkl' and 'classification_model.pkl')
with open('pickle/model.pkl', 'rb') as file:
    regression_model = pickle.load(file)
with open('pickle/class_model.pkl', 'rb') as file:
    classification_model = pickle.load(file)


# Function to calculate the date difference
def calculate_date_difference(order_date, delivery_date):
    return (delivery_date - order_date).days


# Mapping of country names to country codes
countries = {
    "Albania": 28, "Algeria": 25, "Antigua and Barbuda": 30, "Argentina": 32, 
    "Bahamas": 38, "Belize": 78, "Austria": 27, "Bahrain": 77, "Cabo Verde": 113, 
    "Benin": 79, "Armenia": 26, "Barbados": 39, "Belarus": 40, "Guinea-Bissau": 84, 
    "Bhutan": 80, "Latvia": 107, "Botswana": 89
}

# Status options for the dropdown

status_options={'Lost':0, 'Won':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,
                                 'Wonderful':5, 'Revised':6, 'Offered':7, 'Offerable':8}

# item type dropdown option
item_list={'WI': 1,'W': 2,'IPL': 3,'PL': 4,'S': 5,'Others':6,"SLAWR":6}

# product ref dropdown options
prodect_ref_option=[1670798778,1668701718,628377,640665,611993,
       1668701376,164141591,1671863738,1332077137,640405,
       1693867550,1665572374,1282007633,1668701698,628117,
       1690738206,628112,640400,1671876026,164336407,
        164337175,1668701725,1665572032,611728,1721130331,
       1693867563,611733,1690738219,1722207579,929423819,
       1665584320,1665584662,1665584642]

# SETTING PAGE CONFIGURATIONS

st.set_page_config(page_title="Industrial Copper Modeling | By sunilkumar",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'About': """# This app is created by *sunilkumar!*"""})

with st.sidebar:
    selected = option_menu(None, ["Home","Regression","Classification"], 
                           icons=["house-door-fill","tools","card-text"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#C80101"},
                                   "icon": {"font-size": "30px"},
                                   "container" : {"max-width": "5000px"},
                                   "nav-link-selected": {"background-color": "#F1E419"}})

if selected == "Home":
    st.title("Industrial Copper Modeling")
    st.write("The copper industry deals with less complex data related to sales and pricing. However, this data may suffer from issues such as skewness and noisy data, which can affect the accuracy of manual predictions. Dealing with these challenges manually can be time-consuming and may not result in optimal pricing decisions. A machine learning regression model can address these issues by utilizing advanced techniques such as data normalization, feature scaling, and outlier detection, and leveraging algorithms that are robust to skewed and noisy data.")

if selected == 'Regression':
    # User inputs for regression
    st.subheader('Regression Model Inputs')
    country = st.selectbox('Country', options=list(countries.keys()))
    country_code = countries.get(country)
    status = st.selectbox('Status', options=list(status_options.keys()))
    status = status_options.get(status) 
    item_type = st.selectbox('Item type', options=list(item_list.keys()))
    item_type = item_list.get(item_type)
    application = st.selectbox('Application', options=list(np.linspace(1,100,100)))
    width = np.log(st.number_input('Width', min_value=0.0, format='%f',placeholder="Enter width 1-3000") + 1)
    product_ref =  st.selectbox('Application', options=list(prodect_ref_option))
    quantity_tons = np.log(st.number_input('Quantity (tons)', min_value=0.0, format='%f') + 1)
    thickness = st.number_input('Thickness', min_value=1.0, max_value=2500.0, format='%f', placeholder='Enter thickness 1-2500')
    
    # Date inputs
    order_date_input = st.date_input('Order Date', date.today())
    delivery_date_input = st.date_input('Delivery Date', date.today())
    
    # Extract date components
    order_date = float(order_date_input.day)
    order_month = float(order_date_input.month)
    order_year = float(order_date_input.year)
    delivery_date = float(delivery_date_input.day)
    delivery_month = float(delivery_date_input.month)
    delivery_year = float(delivery_date_input.year)

    # Calculate date difference
    date_difference = calculate_date_difference(order_date_input, delivery_date_input)

    # Create the feature array
    features = np.array([[country_code, status, application, thickness, width, product_ref,
                            quantity_tons, item_type, date_difference,
                            order_date, order_month, order_year, delivery_date,
                            delivery_month, delivery_year]])

    # Make prediction
    if st.button('Predict'):
        y_pred = regression_model.predict(features)
        prediction = round(np.exp(y_pred[0]))
        st.write(f'Predicted Selling Price: {prediction} SGD')


if selected == 'Classification':
    st.subheader('Classification Model Inputs')
    customer_id = st.text_input(label='Customer ID (Min: 12458000 & Max: 2147484000)')
    country = st.selectbox('Country', options=list(countries.keys()))
    country_code = countries.get(country)
    selling_price = np.log(st.number_input(label='Selling Price (Min: 0.1 & Max: 100001000)') +1)
    item_type = st.selectbox('Item type', options=list(item_list.keys()))
    item_type = item_list.get(item_type)
    application = st.selectbox('Application', options=list(np.linspace(1,100,100)))
    width = np.log(st.number_input('Width', min_value=0.0, format='%f',placeholder="Enter width 1-3000") + 1)
    product_ref =  st.selectbox('Application', options=list(prodect_ref_option))
    quantity_tons = np.log(st.number_input('Quantity (tons)', min_value=0.0, format='%f') + 1)
    thickness = st.number_input('Thickness', min_value=1.0, max_value=2500.0, format='%f', placeholder='Enter thickness 1-2500')
    
    # Date inputs
    order_date_input = st.date_input('Order Date', date.today())
    delivery_date_input = st.date_input('Delivery Date', date.today())
    
    # Extract date components
    order_date = float(order_date_input.day)
    order_month = float(order_date_input.month)
    order_year = float(order_date_input.year)
    delivery_date = float(delivery_date_input.day)
    delivery_month = float(delivery_date_input.month)
    delivery_year = float(delivery_date_input.year)

    # Calculate date difference
    date_difference = calculate_date_difference(order_date_input, delivery_date_input)

    # Create the feature array
    features=np.array([[country_code, application, thickness, width, product_ref,
    selling_price,quantity_tons, customer_id, item_type, date_difference,
    order_date, order_month, order_year,delivery_date,
    delivery_month, delivery_year]])


    # Make prediction
    if st.button('Predict'):
        y_pred = classification_model.predict(features)
        predicted_status = list(status_options.keys())[int(y_pred[0])]
        st.write(f'Predicted Status of order is : {predicted_status}')

