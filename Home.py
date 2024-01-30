import streamlit as st


st.set_page_config(
    layout = 'wide',
    page_title = 'Agro Twin',
    page_icon = 👤,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.agrotwin.com/help',
        'Report a bug': "https://www.agrotwin.com/bug",
        'About': "# Tu Gemelo Digital en la Nube de tu proyecto *Agro*!"
    }
)

st.title("Agro Twin")
st.header("Configuración")
st.header("Diagnóstico")
st.header("Gemelo Digital")
