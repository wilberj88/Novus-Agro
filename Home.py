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
col1, col2, col3, col4 = st.columns(4)
with col1:
    cultivo = st.radio(
    "¿Cuál es tu cultivo?",
    ["***Pistacho***", "***Cacao***"],
    captions = ["Kerman", "CNCH-13"])

with col2:
    area = st.slider('Cuántas hectáreas cultivadas?', 0, 100, 5)
    
with col3:
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    ubicacion = st.selectbox(
        "En cuál comunidad?",
        ("Toledo", "Ciudad Real", "Albacete"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
    
with col4:
    st.button("Calcular Diagnóstico", type="primary")
    
st.header("Diagnóstico")
st.header("Gemelo Digital")
