import random as rd
import streamlit as st
import base64

def set_background(main_bg):
  #if 'bg_set' not in st.session_state:
  with open(main_bg,"rb") as f:
    data = f.read()
  b64 = base64.b64encode(data).decode()
  
  st.markdown(
     f"""
     <style>
     [data-testid="stAppViewContainer"] {{
        background: url(data:image/jpeg;base64,{b64});
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-position: center;
        background-attachnment: fixed;
      }}
      button[kind="secondary"] {{
            background-image: url(data:image/jpeg;base64,{b64_sponge});
            background-size: cover;
            width: 150px;
            height: 150px;
            border-radius: 50%; /* 둥근 버튼 */
      }}
      </style>
      """,
      unsafe_allow_html=True
    )
    #st.session_state.bg_set = True

#배경 이미지 함수 호출
set_background("background.jpg")

if 'game_started' not in st.session_state:
  st.session_state.game_started = False
st.markdown("<h1 style='text-align: center; color: white;'>멈추기게임</h1>", unsafe_allow_html=True)

#게임영역3등분
col1,col2 = st.columns([3,1])

with col2:
  st.image("sponge.jpg")
  
  if st.button('이미지를 클릭하면 게임시작'):
    st.session_state.game_started = True
    num = rd.random()
    if num < 0.3:
      st.error("멈춰!")
    else:
      st.success("통과!")
