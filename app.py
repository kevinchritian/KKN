import streamlit as st

# st.title("Hello world")

home = st.Page(
    page = "views/home.py",
    title='Home',
    icon= "🏡",
    default= True
)

about = st.Page(
    page = "views/about.py",
    title='Tentang Kami',
    icon= "👨‍💼",
)

sampah = st.Page(
    page = "views/sampah.py",
    title='Sampah',
    icon= "😎",
)

AI = st.Page(
    page = "views/AI.py",
    title = "AI",
    icon= "🤖"
)

pg = st.navigation(
    pages= [home, about, sampah, AI]
)

# {
#     "info" : [home],
#     "projects" :[about],
#     }



pg.run()


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

