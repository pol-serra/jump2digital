# jump2digital
# Informe de Análisis de Datos

## Introducción

Este informe se basa en el análisis de datos de alquileres y niveles de ruido en la ciudad de Barcelona. Los datos se han recopilado de diversas fuentes y se han procesado para realizar un análisis exploratorio. El objetivo principal es examinar la relación entre los precios de alquiler y los niveles de ruido en diferentes distritos y barrios de la ciudad.

### Conjunto de datos

El conjunto de datos consta de dos fuentes principales:

1. Datos de alquiler: Este conjunto de datos contiene información sobre los precios de alquiler de viviendas en diferentes distritos y barrios de Barcelona. Se incluyen datos como el año, el trimestre, el distrito, el barrio, el precio mensual y el precio por metro cuadrado.

2. Datos de niveles de ruido: Este conjunto de datos proporciona información sobre los niveles de ruido en diferentes distritos y barrios de Barcelona. Se incluyen datos como el distrito, el barrio, el tipo de concepto y el valor del nivel de ruido.

## Depuración de Datos

Antes de realizar el análisis, se realizaron las siguientes tareas de preprocesamiento de datos:

1. Se fusionaron los datos de alquiler y niveles de ruido en función de los distritos y barrios correspondientes.

2. Se calculo la media de los precios de alquiler medio y por m2 de los 4 trimestres disponibles, decidi no usar filtro de mediana ya que analizando los datos visualmente no aparecían valores altos o desorbitados erroneos.

3. Se eliminaron columnas innecesarias como 'Codi_Districte' y 'Codi_Barri'. 

4. Se transformó la columna 'Valor' en un valor numérico después de eliminar el símbolo '%' y se mapearon los rangos de ruido a valores numéricos calculando luego la media de dB Promedio.

## Resultados

<!-- El análisis de datos reveló una relación entre los precios de alquiler y los niveles de ruido en diferentes distritos y barrios de Barcelona. Se realizaron análisis estadísticos y visualizaciones para comprender mejor esta relación. -->

Se utilizó el análisis de componentes principales (PCA) para reducir la dimensionalidad de los datos y visualizar la distribución de los distritos y barrios en un espacio de dos componentes principales. Se creó un gráfico de dispersión que muestra la ubicación de los distritos y barrios en función de los dos primeros componentes principales. Al hacer clic en un punto en el gráfico, se muestra información detallada sobre el distrito y el barrio correspondientes. Podemos observar como el primer componentes refleja el precio del barrio fusión entre el valor mensual y por m2. Mientras qeu el segundo componente el nivel de ruido de menor a mayor. Perdemos bastante relevancia en la información del tipo de ruido. 

## Conclusiones

El análisis de datos muestra una relación interesante entre los precios de alquiler y los niveles de ruido en Barcelona. Los resultados sugieren que ciertos distritos y barrios pueden tener una correlación entre el precio de alquiler y los niveles de ruido. Hecho el cual se refleja en la existencia en la ultima grafica donde hay niveles superiores para barrios con un valor más assequible de alquiler.

Este informe proporciona una visión general del análisis de datos realizado y puede ser utilizado como punto de partida para análisis y exploraciones más profundas.
