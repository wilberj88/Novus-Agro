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
    page_icon="🤖",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.agrotwin.com/help',
        'Report a bug': "https://www.agrotwin.com/bug",
        'About': "# Tu Gemelo Digital en la Nube de tu proyecto *Agro*!"
    }
)

colx, coly, colz = st.columns(3)
with coly:
    st.title("🌽 Agro Twin 👨‍🌾")

st.header("Configuración")
col1, col2, col3 = st.columns(3)
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
        ("Toledo", "Ciudad Real", "Albacete", "Santander"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

colx, coly, colz = st.columns(3)
with coly:
    a=  st.button("Calcular Diagnóstico", type="primary")

if a:
    st.header("Diagnóstico")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Costo", "15M €", "40%")
    col2.metric("Rentabilidad", "30%", "-82%")
    col3.metric("Financiación", "16%", "43%")
    col4.metric("Inflación", "7%", "78%")
    
    st.subheader("Cronograma de cultivo 📅")
    
    def render_heatmap_cartesian():
        hours = [
            "12a",
            "1a",
            "2a",
            "3a",
            "4a",
            "5a",
            "6a",
            "7a",
            "8a",
            "9a",
            "10a",
            "11a",
            "12p",
            "1p",
            "2p",
            "3p",
            "4p",
            "5p",
            "6p",
            "7p",
            "8p",
            "9p",
            "10p",
            "11p",
        ]
        days = [
            "Saturday",
            "Friday",
            "Thursday",
            "Wednesday",
            "Tuesday",
            "Monday",
            "Sunday",
        ]
    
        data = [
            [0, 0, 5],
            [0, 1, 1],
            [0, 2, 0],
            [0, 3, 0],
            [0, 4, 0],
            [0, 5, 0],
            [0, 6, 0],
            [0, 7, 0],
            [0, 8, 0],
            [0, 9, 0],
            [0, 10, 0],
            [0, 11, 2],
            [0, 12, 4],
            [0, 13, 1],
            [0, 14, 1],
            [0, 15, 3],
            [0, 16, 4],
            [0, 17, 6],
            [0, 18, 4],
            [0, 19, 4],
            [0, 20, 3],
            [0, 21, 3],
            [0, 22, 2],
            [0, 23, 5],
            [1, 0, 7],
            [1, 1, 0],
            [1, 2, 0],
            [1, 3, 0],
            [1, 4, 0],
            [1, 5, 0],
            [1, 6, 0],
            [1, 7, 0],
            [1, 8, 0],
            [1, 9, 0],
            [1, 10, 5],
            [1, 11, 2],
            [1, 12, 2],
            [1, 13, 6],
            [1, 14, 9],
            [1, 15, 11],
            [1, 16, 6],
            [1, 17, 7],
            [1, 18, 8],
            [1, 19, 12],
            [1, 20, 5],
            [1, 21, 5],
            [1, 22, 7],
            [1, 23, 2],
            [2, 0, 1],
            [2, 1, 1],
            [2, 2, 0],
            [2, 3, 0],
            [2, 4, 0],
            [2, 5, 0],
            [2, 6, 0],
            [2, 7, 0],
            [2, 8, 0],
            [2, 9, 0],
            [2, 10, 3],
            [2, 11, 2],
            [2, 12, 1],
            [2, 13, 9],
            [2, 14, 8],
            [2, 15, 10],
            [2, 16, 6],
            [2, 17, 5],
            [2, 18, 5],
            [2, 19, 5],
            [2, 20, 7],
            [2, 21, 4],
            [2, 22, 2],
            [2, 23, 4],
            [3, 0, 7],
            [3, 1, 3],
            [3, 2, 0],
            [3, 3, 0],
            [3, 4, 0],
            [3, 5, 0],
            [3, 6, 0],
            [3, 7, 0],
            [3, 8, 1],
            [3, 9, 0],
            [3, 10, 5],
            [3, 11, 4],
            [3, 12, 7],
            [3, 13, 14],
            [3, 14, 13],
            [3, 15, 12],
            [3, 16, 9],
            [3, 17, 5],
            [3, 18, 5],
            [3, 19, 10],
            [3, 20, 6],
            [3, 21, 4],
            [3, 22, 4],
            [3, 23, 1],
            [4, 0, 1],
            [4, 1, 3],
            [4, 2, 0],
            [4, 3, 0],
            [4, 4, 0],
            [4, 5, 1],
            [4, 6, 0],
            [4, 7, 0],
            [4, 8, 0],
            [4, 9, 2],
            [4, 10, 4],
            [4, 11, 4],
            [4, 12, 2],
            [4, 13, 4],
            [4, 14, 4],
            [4, 15, 14],
            [4, 16, 12],
            [4, 17, 1],
            [4, 18, 8],
            [4, 19, 5],
            [4, 20, 3],
            [4, 21, 7],
            [4, 22, 3],
            [4, 23, 0],
            [5, 0, 2],
            [5, 1, 1],
            [5, 2, 0],
            [5, 3, 3],
            [5, 4, 0],
            [5, 5, 0],
            [5, 6, 0],
            [5, 7, 0],
            [5, 8, 2],
            [5, 9, 0],
            [5, 10, 4],
            [5, 11, 1],
            [5, 12, 5],
            [5, 13, 10],
            [5, 14, 5],
            [5, 15, 7],
            [5, 16, 11],
            [5, 17, 6],
            [5, 18, 0],
            [5, 19, 5],
            [5, 20, 3],
            [5, 21, 4],
            [5, 22, 2],
            [5, 23, 0],
            [6, 0, 1],
            [6, 1, 0],
            [6, 2, 0],
            [6, 3, 0],
            [6, 4, 0],
            [6, 5, 0],
            [6, 6, 0],
            [6, 7, 0],
            [6, 8, 0],
            [6, 9, 0],
            [6, 10, 1],
            [6, 11, 0],
            [6, 12, 2],
            [6, 13, 1],
            [6, 14, 3],
            [6, 15, 4],
            [6, 16, 0],
            [6, 17, 0],
            [6, 18, 0],
            [6, 19, 0],
            [6, 20, 1],
            [6, 21, 2],
            [6, 22, 2],
            [6, 23, 6],
        ]
        data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]
    
        option = {
            "tooltip": {"position": "top"},
            "grid": {"height": "50%", "top": "10%"},
            "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
            "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
            "visualMap": {
                "min": 0,
                "max": 10,
                "calculable": True,
                "orient": "horizontal",
                "left": "center",
                "bottom": "15%",
            },
            "series": [
                {
                    "name": "Punch Card",
                    "type": "heatmap",
                    "data": data,
                    "label": {"show": True},
                    "emphasis": {
                        "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                    },
                }
            ],
        }
        st_echarts(option, height="500px")
    
    
    ST_HEATMAP_DEMOS = {
        "Heatmap: Heatmap Cartesian": (
            render_heatmap_cartesian,
            "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
        ),
    }
    
    render_heatmap_cartesian()
    
    st.write("Georreferenciación de riesgos climáticos")
    #datos
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-4.0226300, 39.8581000],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-4.0226300,
        longitude=39.8581000,
        zoom=2,
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
    st.header("Flujo de Caja Requerido 💰")
    chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["Gestión de Plagas", "Prevención y Cura de Enfermedades", "Riego de Agua", "Kit Agro Twin"])
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


