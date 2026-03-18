import random as rd
import streamlit as st

st.title("멈추기 게임")

if st.button("game start"):
  num = rd.random()
  if num < 0.3:
    st.error("멈춰!")
  else:
    st.success("통과!")
