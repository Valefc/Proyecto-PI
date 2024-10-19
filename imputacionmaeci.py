import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer

data=st.file_uploader('Subir Archivo CSV',type=['csv'])
if(data is not None):
    df = pd.read_csv(data)
    df_copy2=df.copy()
    # Mostrar el dataset original
    st.write("Datos originales con valores faltantes:")
    st.write(df)
    imputer_mean = SimpleImputer(strategy='mean')
    df_mean = df.copy()
    df_mean[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']]=imputer_mean.fit_transform(df[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']])
    st.write('\nDatos después de la imputación por la media:')
    st.write(df_mean)

    imputer_median = SimpleImputer(strategy='median')
    df_median = df.copy()
    df_median[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']]=imputer_median.fit_transform(df[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']])
    st.write('\nDatos después de la imputación por la mediana:')
    st.write(df_median)

    imputer_mode = SimpleImputer(strategy='most_frequent')
    df_mode = df.copy()
    df_mode[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']]=imputer_mode.fit_transform(df[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']])
    st.write('\nDatos después de la imputación por la moda:')
    st.write(df_mode)
    #Maeci
    df_mice = df_copy2.copy()

    from sklearn.experimental import enable_iterative_imputer  # Necesario para activar el iterador
    from sklearn.impute import IterativeImputer

    imputer_mice = IterativeImputer(max_iter = 10, random_state = 0)

    df_mice[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']]=imputer_mice.fit_transform(df_mice[['price','range_km','charging_time','sales_volume','co2_saved','battery_capacity','energy_efficiency','weight_kg','number_of_seats','motor_power','distance_traveled']])

    st.write('\nDatos después de la imputación por MICE:')
    st.write(df_mice)
    
# Convertir el DataFrame imputado por MICE a CSV
    csv_mice = df_mice.to_csv(index=False)

# Botón para descargar el archivo CSV imputado por MICE
    st.download_button(
        label="Descargar CSV con imputación por MICE",
        data=csv_mice,
        file_name='datos_imputados_mice.csv',
        mime='text/csv')
