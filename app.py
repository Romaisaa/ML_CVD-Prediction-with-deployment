import pickle
import streamlit as st
import numpy as np
from helper import converter

model = pickle.load(open("./static/model.sav",'rb'))
def main():
    st.set_page_config(page_title="Cardiovascular Disease Prediction")
    col1, col2 =  st.columns([20, 30])
    with st.container():
            with col1:
                st.title(" Weclome to CVD Check-up")
            with col2:
                st.image("./static/logo.png", width=400)
    c1,c2= st.columns([40,15])
    with st.container():
        with c1:
            st.subheader("Check your health Easily with us")
            st.write("Please, Answer the following honstly")
        with c2:
            case = st.selectbox("",(" Choose Case","Case 1","Case 2")) 
    #input VarS
        x=0
        y=0
        aph=0
        apl=0
        in1=0
        in2=0
        in3=0

    if (case=="Case 1"):
        x=25
        y=70
        aph=120
        apl=80
        in1=1
        in2=3
        in3=2

    elif (case =="Case 2"):
        x=65
        y=90
        aph=130
        apl=90
        in1=3
        in2=2
        in3=1


    age = int(st.number_input("Age", min_value=0,step=1, value = x,format="%d"))
    gender = st.selectbox("Gender",(" ","Male","Female"), index=in3)
    weight= int(st.number_input("Weight", min_value=0,step=1, value = y,format="%d"))
    col3,col5 =  st.columns([30,30])
    with st.container():
            with col3:
                ap_hi= int(st.number_input("Systolic blood pressure ", min_value=0,step=1, value =aph, format="%d"))
            with col5:
                ap_lo= int(st.number_input("Diastolic blood pressure", min_value=0,step=1,value =apl, format="%d"))
    cholestrol =st.selectbox("Cholestrol Level",(" ","Normal","Above Normal","Well Above Normal"),index =in1) 
    glucose=st.selectbox("Glucose Level",(" ","Normal","Above Normal","Well Above Normal"),index =in2) 
    smoke = st.radio("Are You a Smoker?",("Yes","No"))
    col6,col7 =  st.columns([100,10])
    with st.container():
            with col7:
                check =st.button("Check")


 
    if check:
        if cholestrol==" " or glucose==" " or gender==" " or age== 0 or weight==0 or ap_lo==0 or ap_hi==0 :
            st.write("**Please Fill all required data**")
        else:
            gender = 1 if gender == 'Male' else 2
            smoke = 1 if smoke == 'Yes' else 0
            features =np.array([[age,gender,weight,ap_hi,ap_lo,converter(cholestrol),converter(glucose),smoke]])
            result = model.predict(features)
            if(result == [0]): 
                st.markdown("<h1 style='text-align: center; color: #187498;'>Thanks God, You don't need to worry ✅ </h1>", unsafe_allow_html=True) 
            else: 
                st.markdown("<h1 style='text-align: center; color: #FF5D5D;'>Sorry for news, but you need to see a doctor 🚨</h1>", unsafe_allow_html=True) 


if __name__=="__main__":
    main()





