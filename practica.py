# consume los datos del archivo suelo
# almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
# grafico de despersion de los totales de superficie por TIPUSSOL
# grafico de barras de la superficie media de los 10 primeros NOM_ENS
# grafico circular de la superficie de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirInersiones():
    datos = pd.read_csv('suelo.csv')
    #print(datos)
    df = datos[['NOM_ENS','SUPERFICIE','TIPUSSOL','CODI_TIPUSSOL']] # convertir datos en DataFrame
    print(df)

#consumirInersiones()

def consumirDispersion():
    datos = pd.read_csv('suelo.csv')
    #print(datos)
    df = datos[['NOM_ENS','SUPERFICIE','CODI_TIPUSSOL']] # convertir datos en DataFrame
    #print(df)
    df.plot.scatter(x='CODI_TIPUSSOL',y='SUPERFICIE',alpha=0.3)
    plt.show()

#consumirDispersion()

def consumirBarras():
    datos = pd.read_csv('suelo.csv')
    #print(datos)
    df = datos[['NOM_ENS','SUPERFICIE','TIPUSSOL']] # convertir datos en DataFrame
    #print(df)
    valor_por_ciudad = df.groupby('NOM_ENS')['SUPERFICIE'].mean()
    valor_por_ciudad.head(10).plot.barh()
    df.plot.barh()
    plt.show()

#consumirBarras()