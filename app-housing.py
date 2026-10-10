import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# --- 1. title, with your own name -------------------------------------------
st.title('California Housing Data (1990) by JY Z')

df = pd.read_csv('housing.csv')

# options come from the ORIGINAL dataframe, so the sidebar list never shrinks
all_locations = df.ocean_proximity.unique()

# --- 2. slider: minimal median house value ----------------------------------
value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)

# --- 3. subheader -----------------------------------------------------------
st.subheader('See more filters in the sidebar:')

# --- 4. sidebar multiselect: location type ----------------------------------
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    all_locations,   # options
    all_locations)   # defaults (all selected)

# --- 5. sidebar radio: income level -----------------------------------------
income_filter = st.sidebar.radio('Choose income level', ['Low', 'Medium', 'High'])

# --- apply the filters ------------------------------------------------------
df = df[df.median_house_value >= value_filter]
df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:  # High
    df = df[df.median_income >= 4.5]

# --- 6. map of the filtered districts ---------------------------------------
st.map(df)

# --- 7. histogram below the map, 30 bins ------------------------------------
fig, ax = plt.subplots()
ax.hist(df.median_house_value, bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Number of Districts')
st.pyplot(fig)
