import pickle
import streamlit as st
pickle_in=open('SalaryPrediction.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('Enter experience')
if st.button('predict'):
  rs=model.predict([[e]]).squeeze()
  st.success(f'Salary is {rs}')
  
