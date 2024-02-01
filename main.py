import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\lenovo\\Desktop\\streamlitchartsvehicle\\data\\datasets\cardataprocessed.csv')

st.sidebar.header("Vehicle Dashboard")
st.sidebar.write("This dashboard is using Vehicle dataset from Kaggle for educational purposes.")
st.sidebar.write("Count of Vehicle Ages by Fuel Type:")

chartsoption = st.sidebar.selectbox("Pick one",
                                    ["countplot", "groupby", "boxplot", "violinplot", "pie", "scatterplot", "heatmap"])

# Create an empty list to store the plots
plots = []

if chartsoption == "countplot":
    plt.figure(figsize=(10, 6))
    sns.countplot(x='V_age', hue='Fuel_Type', data=df)
    plt.title('Count of Vehicle Ages by Fuel Type')
    plt.xlabel('Age of Vehicle')
    plt.ylabel('Count')
    plots.append(plt)

elif chartsoption == "groupby":
    plt.figure(figsize=(10, 6))
    df.groupby(['V_age', 'Fuel_Type']).size().unstack().plot(kind='bar', stacked=True)
    plt.title('Count of Vehicle Ages by Fuel Type')
    plt.xlabel('Age of Vehicle')
    plt.ylabel('Count')
    plots.append(plt)

elif chartsoption == "boxplot":
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Fuel_Type', y='V_age', data=df)
    plt.title('Vehicle Age Distribution by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Age of Vehicle')
    plots.append(plt)

elif chartsoption == "violinplot":
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Fuel_Type', y='V_age', data=df)
    plt.title('Vehicle Age Distribution by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Age of Vehicle')
    plots.append(plt)

elif chartsoption == "pie":
    plt.figure(figsize=(8, 8))
    df['Fuel_Type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Vehicle Fuel Types')
    plt.ylabel('')
    plots.append(plt)

elif chartsoption == "scatterplot":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='V_age', y='Fuel_Type', data=df, hue='Fuel_Type', palette='viridis', s=100)
    plt.title('Scatter Plot of Vehicle Ages and Fuel Types')
    plt.xlabel('Age of Vehicle')
    plt.ylabel('Fuel Type')
    plots.append(plt)

else:
    plt.figure(figsize=(10, 6))
    heatmap_data = df.groupby(['V_age', 'Fuel_Type']).size().unstack().fillna(0)
    sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt='g')
    plt.title('Heatmap of Vehicle Ages by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Age of Vehicle')
    plots.append(plt)

# Display each plot individually
for plot in plots:
    st.pyplot(plot)
