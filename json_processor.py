import requests
import pandas as pd
from mapping import *

# URL de la tabla
url = 'https://www.conektate.com.co/med/rest/post.php?Vista=7648372458'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for registro in data:
        if 'CIUDAD' in registro:
            ciudad_id = registro['CIUDAD']
            if ciudad_id in ciudad_mapping:
                registro['CIUDAD'] = ciudad_mapping[ciudad_id]

    for registro in data:
        if 'GENERO' in registro:
            genero_id = registro['GENERO']
            if genero_id in genero_mapping:
                registro['GENERO'] = genero_mapping[genero_id]

    for registro in data:
        if 'GENERACION' in registro:
            generacion_id = registro['GENERACION']
            if generacion_id in generacion_mapping:
                registro['GENERACION'] = generacion_mapping[generacion_id]

    for registro in data:
        if 'NIVEL_EDUCATIVO' in registro:
            nivel_educativo_id = registro['NIVEL_EDUCATIVO']
            if nivel_educativo_id in nivel_educativo_mapping:
                registro['NIVEL_EDUCATIVO'] = nivel_educativo_mapping[nivel_educativo_id]

    for registro in data:
        if 'RETO_ORGANIZACIONAL' in registro:
            reto_org_id = registro['RETO_ORGANIZACIONAL']
            if reto_org_id in reto_organizacional_mapping:
                registro['RETO_ORGANIZACIONAL'] = reto_organizacional_mapping[reto_org_id]

    for registro in data:
        if 'TIPO_DE_CONTRATO' in registro:
            tipo_cont_id = registro['TIPO_DE_CONTRATO']
            if tipo_cont_id in tipo_de_contrato_mapping:
                registro['TIPO_DE_CONTRATO'] = tipo_de_contrato_mapping[tipo_cont_id]

    for registro in data:
        if 'CERTIFICACION_OFRECIDA' in registro:
            certificacion_id = registro['CERTIFICACION_OFRECIDA']
            if certificacion_id in certificacion_ofrecita_mapping:
                registro['CERTIFICACION_OFRECIDA'] = certificacion_ofrecita_mapping[certificacion_id]

    # Crear un DataFrame con los datos
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel('datos_procesados.xlsx', index=False)

else:
    print(f"Error al obtener los datos. Código de estado: {response.status_code}")


"""

    columnas_a_mapear = ['CIUDAD', 'GENERO', 'GENERACION', 'NIVEL_EDUCATIVO', 'RETO_ORGANIZACIONAL', 'TIPO_DE_CONTRATO', 'CERTIFICACION_OFRECIDA']

    def mapeo_automatico(mapeo, columna):
        for registro in data:
            if columna in registro:
                map_id = registro[columna]
                if map_id in genero_mapping:
                    registro[columna] = genero_mapping[map_id]

    for columna in columnas_a_mapear:
        json_out = mapeo_automatico(columna)

    with open('datos_procesados.json', 'w') as json_file:
        json.dump(json_out, json_file, indent=2)

"""