import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from streamlit_option_menu import option_menu



# model = pickle.load(open('C:/Users/User/Desktop/Stats project/pro/logtrModel.sav','rb'))
def main():
    st.set_page_config(page_title="Cardiovascular Diseas Prediction")



# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected
#header section 

    with st.container():
        st.title("Weclome to Cadiovascular diseases check up")
        st.subheader("Check your health Easily with us")
        st.write("Please, Answer the following honstly")

    #input Var
    Age = st.number_input("Age")
    gender = st.selectbox("Gender",(" ","Male","Female"))
    

    hieght= st.number_input("Height")
    wieght= st.number_input("weight")
    ap_hi= st.number_input("Ap_hi")
    ap_lo= st.number_input("Ap_lo")
    cholestrol =st.selectbox("Cholestrol Level",(" ","Normal","Above Normal","Well Above normal")) 
    glucose=st.selectbox("Glucose Level",(" ","Normal","Above Normal","Well Above normal")) 
    smoke = st.radio("Are You a Smoker",("Yes","No"))
    alco = st.radio("Do you drink Alcohol",("Yes","No"))
    active = st.radio("Do you usually do physical activities",("Yes","No")) 

    if st.button("Check"):
        gender = 1 if gender == 'Male' else 0
        smoke = 1 if smoke == 'Yes' else 0
        alco = 1 if alco == 'Yes' else 0
        active = 1 if active == 'Yes' else 0

if __name__=="__main__":
    main()


    



