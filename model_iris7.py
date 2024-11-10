import pickle
import pandas as pd
import streamlit as st



st.image('http://www.ehtp.ac.ma/images/lo.png')

st.title('MSDE6 Streamlit Lab')
st.header('lab deployment')
st.selectbox('Data', ['Single', 'from file'])

st.sidebar.image('https://cdn.britannica.com/39/91239-004-44353E32/Diagram-flowering-plant.jpg')
st.sidebar.title('User Input Parameters :')
sep_l=st.sidebar.slider('Sepal length', 0, 10)
sep_w=st.sidebar.slider('Sepal width', 0, 6)
pet_l=st.sidebar.slider('Petal length', 0, 10)
pet_w=st.sidebar.slider('Petal width', 0, 6)

data=pd.DataFrame([sep_l,sep_w,pet_l,pet_w]).T
model=pickle.load(open('modeliris6.pkl','rb'))
#model=pickle.load(open(r'C:\Users\Admin\01_ipynb\MSDE_Course\MSDE6\M6_ML\labs_msde6_std\10_deploiement\Streamlit\app build\modeliris6.pkl','rb'))
type=model.predict(data)

st.write(type)
