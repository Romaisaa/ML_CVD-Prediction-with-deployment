import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from helper import converter


model = pickle.load(open('./static/model.sav','rb'))
def main():
    st.set_page_config(page_title="Cardiovascular Diseas Prediction")
    with st.container():
        st.title("Weclome to Cadiovascular diseases check up")
        st.subheader("Check your health Easily with us")
        st.write("Please, Answer the following honstly")

    #input Var
    age = int(st.number_input("Age"))
    gender = st.selectbox("Gender",(" ","Male","Female"))
    height= int(st.number_input("Height"))
    weight= int(st.number_input("Weight"))
    ap_hi= int(st.number_input("Systolic blood pressure "))
    ap_lo= int(st.number_input("Diastolic blood pressure"))
    cholestrol =st.selectbox("Cholestrol Level",(" ","Normal","Above Normal","Well Above Normal")) 
    glucose=st.selectbox("Glucose Level",(" ","Normal","Above Normal","Well Above Normal")) 
    smoke = st.radio("Are You a Smoker?",("Yes","No"))
    alco = st.radio("Do you drink Alcohol?",("Yes","No"))
    active = st.radio("Do you usually do physical activities?",("Yes","No")) 

    if st.button("Check"):
        if cholestrol==" " or glucose==" " or gender==" " or age== 0 or height==0 or weight==0 or ap_lo==0 or ap_hi==0 :
            st.write("Please Fill all required data")
        else:
            gender = 1 if gender == 'Male' else 2
            smoke = 1 if smoke == 'Yes' else 0
            alco = 1 if alco == 'Yes' else 0
            active = 1 if active == 'Yes' else 0
            features =np.array([[age,gender,height,weight,ap_hi,ap_lo,converter(cholestrol),converter(glucose),smoke,alco,active]])
            result = model.predict(features)
            if(result == [0]): 
                st.write("Thanks God, You don't need to woory")
            else: 
                st.write("Sorry for news, but you need to see doctor")





if __name__=="__main__":
    main()





