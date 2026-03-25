import random as rd
import streamlit as st
import base64

def set_background(main_bg):
  if 'bg_set' not in st.session_state:
    with open(main_bg,"rb") as f:
      data = f.read()
    b64 = base64.b64encode(data).decode()
  
    st.markdown(
     f"""
     <style>
     div.stbutton > button:first-child{
       gackground_color: transparent;
       border: none:
       padding: 0;
     }
      </style>
      """,
      unsafe_allow_html=True
    )
    st.session_state.bg_set = True

#배경 이미지 함수 호출
set_background('background.jpg')
    
  
#CSS 코드를 이용해 배경색 설정
page_bg_color ="""
<style>
[data-testid="stAppViewContainer"]{
background-color: #F0FFFF;
}
</style>
"""
st.markdown(page_bg_color,unsafe_allow_html=True)
st.title("멈추기 게임")

col1,col2,col3 = st.columns([1,2,1])

with col2:
  st.image("background.jpg")
  if st.button(""):
    num = rd.random()
    if num < 0.3:
      st.error("멈춰!")
    else:
      st.success("통과!")
