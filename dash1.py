
import streamlit as st
import plotly.express as px
import pandas as pd
import statsmodels.api as sm

# Configuración de la página
st.set_page_config(layout="wide")

# Título del Dashboard
st.title("Dashboard de Análisis de Vehículos Eléctricos")

# Cargar los datos
df = pd.read_csv("D:/Documentos/VALERIA/Documents/Univalle 4 Vale/Proyecto Integrador/ProyectoIntegrador/datos_combinados.csv")

# Sidebar para filtros
st.sidebar.header("Filtros")
select_region = st.sidebar.multiselect("Seleccione la Región", df['region'].unique(), default=df['region'].unique())
select_year = st.sidebar.multiselect("Seleccione el Año", df['year'].unique(), default=df['year'].unique())

# Filtrar datos según selección
df_filtered = df[(df['region'].isin(select_region)) & (df['year'].isin(select_year))]

# Mostrar tabla filtrada
if st.checkbox("Mostrar información del dataset filtrado"):
    st.write(df_filtered)

# División en columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolución de Ventas por Región")
    fig_sales_trend = px.scatter(df_filtered, x='year', y='range_km', color='region', 
                                 title="Tendencia de Ventas por Año y Región")  # Agregar la línea de tendencia
    st.plotly_chart(fig_sales_trend)

# Gráfico 2: Relación entre Precio y Autonomía (km)
with col2:
    st.subheader("Relación entre Precio y Autonomía")
    fig_price_range = px.scatter(df_filtered, x='price', y='range_km', color='battery_capacity',
                                 size='Ventas', hover_data=['motor_power'], 
                                 title="Precio vs Autonomía")
    st.plotly_chart(fig_price_range)

# Gráfico 3: Distribución de la Ganancia
st.subheader("Distribución de la Ganancia")
fig_ganancia = px.histogram(df_filtered, x='Ganancia', nbins=30, color='Rentabilidad', 
                            title="Distribución de la Ganancia por Rentabilidad")
st.plotly_chart(fig_ganancia)

# Gráfico 4: Comparativa de Ventas por Método de Pago
st.subheader("Comparativa de Ventas por Método de Pago")
fig_payment = px.bar(df_filtered, x='Metodo_Pago', y='Ventas', color='Metodo_Pago', title="Ventas por Método de Pago")
st.plotly_chart(fig_payment)

# Gráfico 5: Evolución de Ganancia y Costos
st.subheader("Evolución de Ganancia y Costos")
fig_profit_cost = px.line(df_filtered, x='year', y=['Ganancia', 'Costos'], color='region', title="Ganancia y Costos por Año")
st.plotly_chart(fig_profit_cost)

# Gráfico 6: Relación entre Ventas y CO2 Ahorrado
st.subheader("Relación entre Ventas y CO2 Ahorrado")
fig_co2 = px.scatter(df_filtered, x='Ventas', y='co2_saved', color='region', 
                     title="Ventas vs CO2 Ahorrado", size='battery_capacity')
st.plotly_chart(fig_co2)

# Gráfico 7: Distribución de Volumen de Ventas por Región
st.subheader("Distribución de Volumen de Ventas por Región")
fig_pie = px.pie(df_filtered, values='Ventas', names='Región', title="Distribución de Ventas por Región")
st.plotly_chart(fig_pie)

#Gráfico 8: Ventas Clasificadas por Número de Asientos
st.subheader("Clasificación de Autos por Cantidad de Asientos")
fig_payment_class = px.pie(df_filtered, values='Ventas',names='number_of_seats',
                           title="Ventas Clasificadas por Número de Asientos")
st.plotly_chart(fig_payment_class)

# Gráfico 9: Relación entre Ventas y Costos
st.subheader("Relación entre Ventas y Costos")
fig_sales_cost = px.scatter(df_filtered, x='Ventas', y='Costos', color='region',
                            title="Relación entre Ventas y Costos",
                            labels={'Ventas': 'Ventas Totales', 'Costos': 'Costos Totales'})
st.plotly_chart(fig_sales_cost)


# Gráfico 10: Distribución de Costos
st.subheader("Distribución de Costos")
fig_cost_distribution = px.histogram(df_filtered, x='Costos', nbins=30, color='region',
                                     title="Distribución de Costos",
                                     labels={'Costos': 'Costos Totales'})
st.plotly_chart(fig_cost_distribution)

# Gráfico 11: Promedio de Ganancia por Región
st.subheader("Promedio de Ganancia por Región")
avg_ganancia_region = df_filtered.groupby('region')['Ganancia'].mean().reset_index()
fig_avg_ganancia = px.bar(avg_ganancia_region, x='region', y='Ganancia', color='region',
                          title="Promedio de Ganancia por Región",
                          labels={'Ganancia': 'Promedio de Ganancia'})
st.plotly_chart(fig_avg_ganancia)

# Crear un gráfico de dispersión usando Plotly Express
fig = px.density_heatmap(df, x='range_km', y='battery_capacity',
                         title='Relación entre rango y Capacidad de la Batería',
                         labels={'range_km': 'Rango(km)', 
                                 'battery_capacity': 'Capacidad de la Batería (mAh)'})

st.plotly_chart(fig)


