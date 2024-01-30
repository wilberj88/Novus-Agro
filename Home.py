import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from streamlit_echarts import st_echarts
import plotly.figure_factory as ff
import altair as alt


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
st.header("Diagnóstico de Riesgos Climáticos")
    st.write("Probabilidades de ocurrencia en el periodo ", categoria)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Derrumbes", "70%", "40%")
    col2.metric("Sequías", "30%", "-82%")
    col3.metric("Incedios", "16%", "43%")
    col4.metric("Inundaciones", "87%", "78%")
    st.write("Georreferenciación de riesgos climáticos")
    #datos
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [4.2620, -75.13],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=4.26,
        longitude=-75.13,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
        ],
        ))
    st.header("Mitigación requerida")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Movimiento de Tierras", "Motobombas", "Escombros"])
    st.area_chart(chart_data)
    st.write("Financiación necesaria")
        # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['3 meses antes del evento', 'Post evento', '3 meses después del evento']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.header("Plan de Adaptación por zonas")
    chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["emisiones", "flora", "fauna"])
    st.bar_chart(chart_data)

    def render_basic_radar():
        option = {
                "title": {"text": "Transición energética"},
                "legend": {"data": ["Consumo Actual", "Consumo Óptimo"]},
                "radar": {
                    "indicator": [
                        {"name": "Agua", "max": 6500},
                        {"name": "Carbón", "max": 16000},
                        {"name": "Viento", "max": 30000},
                        {"name": "Sol", "max": 38000},
                        {"name": "Petróleo", "max": 52000},
                        {"name": "Gas", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Consumo Actual Vs Óptimo",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Consumo Actual",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Consumo Óptimo",
                            },
                        ],
                    }
                ],
            }
        st_echarts(option, height="500px")
    render_basic_radar()
# Data src:  https://www.kaggle.com/manohar676/hotel-reviews-segmentation-recommended-system
# Credit to: Manohar Reddy
    df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Radar-chart/ExistingHotels_CustomerVisitsdata-1554810038262.csv")
    df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
    print(df.iloc[:20, :8])

    df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                    'Rooms_rating','Checkin_rating',
                                    'Businessservice_rating']].mean().reset_index()
    print(df)

# Convert from wide data to long data to plot radar chart
    df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
                     value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                 'Rooms_rating','Checkin_rating','Businessservice_rating'],
        )
    print(df)

# radar chart Plotly examples - https://plotly.com/python/radar-chart/
# radar chart Plotly docs = https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html#plotly.express.line_polar
    fig = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                                    line_shape='linear',  # or spline
                            hover_name='Hotelid',
                            hover_data={'Hotelid':False},
                            markers=True,
                            # labels={'rating':'stars'},
                            # text='Hotelid',
                            # range_r=[0,10],
                            direction='clockwise',  # or counterclockwise
                            start_angle=45
                            )
        # fig.update_traces(fill='toself')
    fig.show()

st.header("Gemelo Digital")
