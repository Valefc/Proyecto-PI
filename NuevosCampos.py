import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

data = st.file_uploader('Subir Archivo CSV', type=['csv'])
if data is not None:
    df = pd.read_csv(data)
    df_copy2 = df.copy()
    # Mostrar el dataset original
    st.write("Datos originales:")
    st.write(df)

    # Generar datos extendidos 
    vendedores = np.random.choice(['Carlos', 'Maria', 'Luis', 'Ana', 'Pedro'], 12654)
    regiones = np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 12654)
    ventas = np.random.randint(100, 500, 12654)
    costos = ventas * np.random.uniform(0.6, 0.9, 12654)

    # Generar fechas aleatorias dentro de un rango específico
    fechas = [datetime.now() - timedelta(days=np.random.randint(0, 30)) for _ in range(12654)]

    # Generar métodos de pago aleatorios
    metodos_pago = np.random.choice(['Efectivo', 'Tarjeta de Crédito', 'Transferencia'], 12654)

    # Crear DataFrame de ejemplo con 50 registros
    df2 = pd.DataFrame({
        'Vendedor': vendedores,
        'Región': regiones,
        'Ventas': ventas,
        'Costos': costos,
        'Fecha_Venta': fechas,
        'Metodo_Pago': metodos_pago,
    })

    # Mostrar el dataset original
    st.write("### Nuevos Campos:")
    st.dataframe(df2)

    #### 1 Agregación Simple
    ventas_por_vendedor = df2.groupby("Vendedor")["Ventas"].sum().reset_index()
    st.write("### Ventas Totales por Vendedor")
    st.dataframe(ventas_por_vendedor)

    ### 2 Agregación Múltiple
    ventas_agrupadas = df2.groupby(["Vendedor", "Región"])["Ventas"].agg(["sum", "mean"]).reset_index()
    st.write("### Suma y Promedio por Vendedor y Región")
    st.dataframe(ventas_agrupadas)

    ### 3 Agregación con Múltiples Funciones 
    ventas_costos = df2.groupby('Vendedor').agg(
        Total_Ventas=('Ventas', 'sum'),
        Total_Costos=('Costos', 'sum'),
        Promedio_Ventas=('Ventas', 'mean')
    ).reset_index()
    st.write("### Suma de Ventas y Costos, y Promedio de Ventas por Vendedor:")
    st.dataframe(ventas_costos)

    #### NUEVOS CAMPOS
    ### 1 Crear nueva variable que sea Ganancia
    df2["Ganancia"] = df2["Ventas"] - df2["Costos"]
    st.write("### Después de Crear el Nuevo Campo 'Ganancia' ")
    st.dataframe(df2)

    ### 2 Creación de Variables Categóricas
    def clasificar_rentabilidad(g):
        if g > 200:
            return "Alta"
        elif g > 100:
            return "Media"
        else:
            return "Baja"

    df2["Rentabilidad"] = df2["Ganancia"].apply(clasificar_rentabilidad)
    st.write("### Crear el Campo Categórico 'Rentabilidad'")
    st.dataframe(df2)

    ### 3 Crear una Variable 'Costo_Por_Venta' (Costos / Ventas)
    df2['Costo_Por_Venta'] = df2['Costos'] / df2['Ventas']
    st.write("### Después de Crear la Variable 'Costo_Por_Venta'")
    st.dataframe(df2)

    ### Nuevos Campos Adicionales
    ### 6 Contar las ventas por método de pago
    ventas_por_pago = df2.groupby('Metodo_Pago')['Ventas'].sum().reset_index()
    st.write("### Ventas Totales por Método de Pago")
    st.dataframe(ventas_por_pago)

    ### 7 Contar las ventas por región y fecha
    ventas_por_region_fecha = df2.groupby(['Región', pd.Grouper(key='Fecha_Venta', freq='D')])['Ventas'].sum().reset_index()
    st.write("### Ventas Totales por Región y Fecha")
    st.dataframe(ventas_por_region_fecha)

    # Juntar los DataFrames añadiendo columnas
    df_combined = pd.concat([df.reset_index(drop=True), df2.reset_index(drop=True)], axis=1)

    # Mostrar el dataset combinado
    st.write("### Datos Combinados:")
    st.dataframe(df_combined)
    
    csv = df_combined.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar CSV",
        data=csv,
        file_name='datos_combinados.csv',
        mime='text/csv',
    )