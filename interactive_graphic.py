import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


noise_level_path = '/Users/polserramontes/Desktop/Hackaton/2017_poblacio_exposada_barris_mapa_estrategic_soroll_bcn_long.csv'
rent_path = '/Users/polserramontes/Desktop/Hackaton/2017_lloguer_preu_trim.csv'

rent = pd.read_csv(rent_path)
noise_level = pd.read_csv(noise_level_path)

df_pivoted = rent.pivot_table(index=['Any', 'Trimestre', 'Codi_Districte', 'Nom_Districte', 'Codi_Barri', 'Nom_Barri'],
                              columns='Lloguer_mitja',
                              values='Preu',
                              aggfunc='first').reset_index()

# Renombrar las columnas
df_pivoted.rename(columns={'Lloguer mitjà mensual (Euros/mes)': 'Precio_Mensual',
                          'Lloguer mitjà per superfície (Euros/m2 mes)': 'Precio_Por_Superficie'},
                 inplace=True)

# Si deseas combinar las dos columnas en un solo DataFrame, puedes hacerlo así
df_combined = df_pivoted[['Any', 'Trimestre', 'Codi_Districte', 'Nom_Districte', 'Codi_Barri', 'Nom_Barri', 'Precio_Mensual', 'Precio_Por_Superficie']]

rent = df_combined

# Computing middle value for Month price and m2 price

price_month=df_pivoted.groupby('Codi_Barri')['Precio_Mensual'].mean()
price_m2=df_pivoted.groupby('Codi_Barri')['Precio_Por_Superficie'].mean()

# Agrupar por distrito y barrio y calcular el promedio de Precio_Por_Superficie
rent_middle = df_pivoted.groupby(['Codi_Districte', 'Nom_Districte', 'Codi_Barri', 'Nom_Barri']).agg(
    Precio_Por_Superficie_Mean=('Precio_Por_Superficie', 'mean'),
    Precio_Mensual_Mean=('Precio_Mensual', 'mean')
).reset_index()

df_joined = rent_middle.merge(noise_level, on = ['Codi_Districte', 'Nom_Districte', 'Codi_Barri', 'Nom_Barri'])
to_drop = ['Codi_Districte', 'Codi_Barri']
for drop in to_drop:
    df_joined=df_joined.drop(drop,axis=1)

def transform_value(x):
    return np.float16(x.replace("%",""))/100
    
df_joined['Valor']=df_joined['Valor'].apply(transform_value)

df = df_joined.copy()

mapeo_rango_db = {
    '<40 dB': 30,
    '40-45 dB': 42.5,
    '45-50 dB': 47.5,
    '50-55 dB': 52.5,
    '55-60 dB': 57.5,
    '60-65 dB': 62.5,
    '65-70 dB': 67.5,
    '70-75 dB': 72.5,
    '75-80 dB': 77.5,
    '>=80 dB': 90 
}

df['Valor_Numerico'] = df['Rang_soroll'].map(mapeo_rango_db)
df['dB_Promig'] = df['Valor_Numerico'] * df['Valor']
df_dB = df.groupby(['Nom_Districte', 'Nom_Barri', 'Precio_Por_Superficie_Mean', 'Precio_Mensual_Mean', 'Concepte'])['dB_Promig'].sum().reset_index()

dum=pd.get_dummies(df_dB, columns=['Concepte'],prefix=['Concepte'])

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Supongamos que tu DataFrame se llama df

# 1. Separar las columnas de características
X = dum.drop(['Nom_Districte', 'Nom_Barri'], axis=1)

# 2. Estandarizar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar PCA a todas las columnas
pca = PCA(n_components=2)  # Especifica el número de componentes principales deseados
pca_result = pca.fit_transform(X)
y=[str(nbh) for nbh in dum['Nom_Barri']]
y= [(str(distric), concept,str(db)) for distric, concept,db in zip(dum['Nom_Barri'], df['Concepte'],dum['dB_Promig'])]
y_district= [str(dist)for dist in zip(dum['Nom_Districte'])]


import matplotlib.pyplot as plt
import mplcursors  # Importa la biblioteca mplcursors

# Supongamos que tienes un DataFrame con los componentes principales en 'pca_result' y los nombres de los barrios en 'y'

# Crear un diccionario para asignar colores a cada barrio
colores = {}
barrios_unicos = set(y_district)
colormap = plt.cm.get_cmap('rainbow', len(barrios_unicos))
for i, barrio in enumerate(barrios_unicos):
    colores[barrio] = colormap(i / len(barrios_unicos))

# Crear un gráfico de dispersión
fig, ax = plt.subplots(figsize=(14, 10))

scatter = ax.scatter(pca_result[:, 0], pca_result[:, 1], c=[colores[barrio] for barrio in y_district], alpha=0.7)

# Agregar información al hacer clic en los puntos
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(y[sel.target.index]))

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=barrio, markersize=10, markerfacecolor=color) for barrio, color in colores.items()]
ax.legend(handles=legend_elements, title='Distritos', loc='upper right')

ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_title('Gráfico de Componentes Principales')
ax.grid(True)

plt.show()