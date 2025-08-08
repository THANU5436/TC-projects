import streamlit as st
import pandas as  pd
st.title("student's Registration Form")
st.subheader("Welcome to the MRECW website")
st.image(r"mrecw 2.jpeg",width=600)
name=st.text_input("Enter your name : ")
college=st.text_input("Enter your college name : ")
br=st.selectbox("Select your Branch : ",['CSE','AIML','IT','DS','ECE','EEE'])
if br is not None:
    st.success(br)
year=st.radio("Select your year : ['I st','II nd','III rd','IV th']")
if year is not None:
    st.success(year)
rollNo=st.text_input("Enter your Roll Number : ")
if rollNo is not None:
    st.success(rollNo)
mail=st.text_input("Enter your Email id : ")
num=st.text_input("Enter your mobile number : ")
gpa=st.text_input("Enter your CGPA :")
cert=st.multiselect("Select your Certifications : ",['cisco','infosys','Data Science','Machine Learning','deep learning','Cyber security'])
if cert is not None:
    st.success(cert)
if st.button("Submit"):
    st.success("Thank you for your registration:")