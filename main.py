import random as rd
import streamlit as st

st.title("stop game")

if st.button("game start"):
  num = rd.random()
    if num num < 0.1:
      st.error("stop")
    else:
      st.success("pass")
