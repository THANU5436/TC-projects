import streamlit as st
import pandas as  pd
import seaborn as sns
import matplotlib.pyplot as plt
#title
st.title("Real-Time movie recommendation using Ai")
# imgload
st.image(r"C:\Users\madap\Downloads\images 2.jpeg", width=700)
#header
st.header("The best movie recommendation")
#subheader
st.subheader("its a AI recommend")
#text
st.text("let's start")
uploadfile=st.file_uploader("upload csv. files only",type=["csv"])

if uploadfile is not None:
    dataFrame=pd.read_csv(uploadfile)
    st.subheader(" uploaded csv sucessfully..😊")
    st.dataframe(dataFrame)
    st.write("File Name is ::",uploadfile.name)
    st.write("File shape ::",dataFrame.shape)
    st.write("coloumns Data ::",dataFrame.columns.tolist())
    st.subheader("lets start the preprocessing.....")
    dataFrame.dropna(inplace=True)
    dataFrame["Type"] = pd.factorize(dataFrame["Type"])[0]
    dataFrame["Title"] = pd.factorize(dataFrame["Title"])[0]
    dataFrame["Genre"] = pd.factorize(dataFrame["Genre"])[0]
    dataFrame["Year"] = dataFrame["Year"].astype(float)
    st.write("data cleaning")
    st.dataframe(dataFrame)
    st.write("first five rows")
    st.dataframe(dataFrame.head())
    st.write("Last five rows")
    st.dataframe(dataFrame.tail())
    st.write("Data:",dataFrame.describe())
    st.write("Data visualization")
    fig1, ax1 = plt.subplots() 
    sns.histplot(dataFrame["Genre"], bins=10, kde=True, ax=ax1, color="purple")
    ax1.set_xlabel("Genre")
    ax1.set_ylabel("Count")
    ax1.set_title("Genre Counts in Movies")
    st.pyplot(fig1)
    st.checkbox("select the checkboxes for accept the dataset")
    st.checkbox("select the checkboxes for accept the Rating data")
    st.checkbox("select the checkboxes for accept the Movie data")
    Sg=st.radio("select the colums:",["Type","Title","Genre","Year"])
    if Sg is not None:
        st.success(Sg)
    dat=st.selectbox("select the Dataset colums:",["Type","Title","Genre","Year"])
    if dat is not None:
        st.success(dat)
    dat=st.multiselect("select the Dataset colums:",["Type","Title","Genre","Year"])
    if dat is not None:
        st.success(len(dat))
        stbutton=st.button("Register")
        if st.button("Login"):
            st.success("Login successfully")
        #14 text_input
        Stname = st.text_input("Enter the name")
        if st.button("Submit"):
            name = Stname.title()
            st.success("Data submitted successfully")
            st.write("your Name ::", name)
else:
    st.warning("you can upload only  .csv file formate ")
    st.error("file was not uploaded..🙁")
    exc=FileNotFoundError()
    st.exception(exc)
#run the program
#streamlit run app.py