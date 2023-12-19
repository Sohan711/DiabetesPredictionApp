import streamlit as st

import pandas as pd
# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache_resource
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():

    st.subheader("From Exploratory Data Analysis")
    df= load_data("diabetes_data.csv")
    st.dataframe(df)
    

    submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
    if submenu == "Descriptive":
      #     st.dataframe(df)
          with st.expander("Data Types"):
                st.dataframe(df.dtypes)
          with st.expander("Descriptive Summary"):
                st.dataframe(df.describe())
          with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())
          with st.expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())  
    elif submenu == "Plots":
      st.subheader("Plots")
      with st.expander("Dist Plot of Gender"):
                fig = plt.figure()
                sns.countplot(df['Gender'])
                st.pyplot(fig)
      with st.expander("Outlier Detection"):
           fig = plt.figure()
           sns.boxplot(df['Age'])
           st.pyplot(fig)


      # with st.expander("Correlation Plot"):
      #       corr_matrix = df.corr()
      #       fig = plt.figure(figsize=(20,10))               
      #       sns.heatmap(corr_matrix,annot=True)
      #       st.pyplot(fig)
               


         