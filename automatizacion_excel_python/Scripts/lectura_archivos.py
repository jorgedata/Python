# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:34:22 2023

@author: jorge
"""

import pandas as pd


def main(): #Funcion principal

    df = leer_archivo()
    df = agregar_filtros(df)
    vizualizar_datos(df) 
    exportar_datos(df)

def leer_archivo(): #Funcion para leer el archivo y las columnas a usar
    import os
    print("leyendo archivos....")
    Columnas = [3,4,5,6,7,12] #las columnas que vamos a usar para analizar 
    
    ruta= "..\Input"
    nom_archivo = input("Ingresar el nombre del archivo: ")+"xlsx"
    direccion = os.path.join(ruta, nom_archivo)
    
    df = pd.read_excel("..\Input\supermarket_sales.xlsx",
                     sheet_name ="hoja1",
                     header = 0,
                     usecols = Columnas
                     )
    return df

def agregar_filtros(df):
    print("AGREGANDO FILTROS")
    df= df[df["Payment"]=="Cash"]
    
    return df
    
def vizualizar_datos(df):
    print("VISUALIZANDO LOS PRIMEROS DATOS")    
    df_columnas = df.columns #guardamos los nombres de las columnas

    for col in df_columnas:
        print(df[col].head(5))

def exportar_datos(df):
    print("Exportando archivo procesado...")
    df.to_csv("..\Output\ejemplo.csv",
              sep = ",",
              header= True,
              index=False)
    
    
if __name__ == "__main__":
    main()    
    Input("\tPROCESO FINALIZADO. ´presionar ENTER para salir")