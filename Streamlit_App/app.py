import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(
    page_title="Duplicate Question Checker",
    page_icon="❓",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background-color: #FFE4E1;  
        color: #4B0082; 
        font-family: 'Arial', sans-serif;
    }
    h1, h2 {
        color: #800080; 
    }
    .stButton>button {
        background-color: #FFB6C1;  
        color: black;               
        height: 3em;
        width: 100%;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
    }
    .stTextArea>div>textarea {
        border-radius: 8px;
        border: 5px solid #FFC0CB;  
        padding: 10px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Duplicate Question Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #C71585;'>Check if two questions are duplicates</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    q1 = st.text_area("Enter Question 1", height=120)
with col2:
    q2 = st.text_area("Enter Question 2", height=120)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Check Duplicate"):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.markdown(
                "<h2 style='text-align: center; color: #800080;'>These questions are duplicates</h2>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h2 style='text-align: center; color: #800080;'>These questions are NOT duplicates</h2>",
                unsafe_allow_html=True
            )

st.markdown("---")