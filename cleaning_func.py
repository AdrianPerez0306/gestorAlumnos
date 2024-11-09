import numpy as np
import pandas as pd

from palabras_clave import trabajos_keywords_all, materias_keywords_all, localidades_keywords, experiencia_keywords_all, \
    hobbies_keywords, mascotas_keywords_all, musica_keywords, series_keywords, materia_keywords, replacement_pack, \
    mascota_keyword, experiencia_keywords

trabajo = {
    "label": "trabajo",
    "keywords": trabajos_keywords_all,
    "default_value": ['no trabajo']
}

materias = {
    "label": "materias",
    "keywords": materias_keywords_all,
    "default_value": ['']
}

localidad = {
    "label": "localidad",
    "keywords": localidades_keywords,
    "default_value": ['no especifica']
}

experiencia = {
    "label": "experiencia",
    "keywords": experiencia_keywords_all,
    "default_value": ['']
}

hobbies = {
    "label": "hobbies",
    "keywords": hobbies_keywords,
    "default_value": None
}

mascotas = {
    "label": "mascotas",
    "keywords": mascotas_keywords_all,
    "default_value": None
}

musica = {
    "label": "musica",
    "keywords": musica_keywords,
    "default_value": None
}

series = {
    "label": "series",
    "keywords": series_keywords,
    "default_value": None
}

def reemplazar_dni_nan(col):
    return col.apply(lambda x: np.random.uniform(41000000, 42000000) if pd.isna(x) else x)




def clean_materias(dataframe):
    dataframe[materias['label']] = dataframe[materias['label']].apply(lambda row: limpiar_materias_names(row))
    dataframe[materias['label']] = dataframe[materias['label']].apply(lambda row: limpiar_materias_pseudonimos(row))
    dataframe[materias['label']] = dataframe[materias['label']].apply(lambda row: materia_default(row))
    dataframe[materias['label']] = dataframe[materias['label']].apply(lambda row: list(set(row)))


def limpiar_materias_names(materias):
    materias_reemplazadas = []
    for materia in materias:
        # Buscamos en el diccionario para ver si 'materia' está en las palabras clave
        reemplazo = next((key for key in materia_keywords.keys() if materia in materia_keywords[key]), materia)
        # Si encontramos una coincidencia, usamos el 'key'; si no, mantenemos el valor original
        materias_reemplazadas.append(reemplazo)
    return materias_reemplazadas


def limpiar_materias_pseudonimos(materias):
    if "pack de 3" in materias or "3 materias" in materias:
        return replacement_pack
    return materias

def materia_default(materias):
    #TODOS CURSAN BASE DE DATOS POR DEFAULT, EN ESTE CASO
    return materias if "base_de_datos" in materias else materias + ["base_de_datos"]

def empty_to_null(lista):
    if len(lista) == 0:
        return None
    else:
        return lista


def replace_keywords(description, keywords):
    return [keyword for keyword in keywords if keyword.lower() in description.lower()]


def extract_columns_from_description(dataframe):
    new_columns = [trabajo, materias, localidad, experiencia, hobbies, mascotas, musica, series]
    for column in new_columns:
        dataframe[column['label']] = dataframe['descripcion'].apply(lambda row: replace_keywords(row, column['keywords']))

    # Una vez obtengo los datos extraidos de "descripcion", procedo a eliminar la columna
    dataframe.drop(columns=['descripcion'], inplace=True)


def fill_empty_with_none(dataframe):
    set_null_if_empty = lambda value, default_value: default_value if value == [] else value
    columns = [trabajo, materias, localidad, experiencia, hobbies, mascotas, musica, series]
    for column in columns:
        dataframe[column['label']] = dataframe[column['label']].apply(lambda row: set_null_if_empty(row, column['default_value']))


def clean_mascotas(dataframe):
    dataframe[mascotas['label']] = dataframe[mascotas['label']].apply(lambda row: limpiar_mascotas_names(row))


def limpiar_mascotas_names(mascotas):
    # Creamos una lista nueva con las materias reemplazadas
    mascotas_reemplazadas = []
    for mascota in mascotas:
        # Buscamos en el diccionario para ver si 'materia' está en las palabras clave
        reemplazo = next((key for key in mascota_keyword.keys() if mascota in mascota_keyword[key]), mascota)
        # Si encontramos una coincidencia, usamos el 'key'; si no, mantenemos el valor original
        mascotas_reemplazadas.append(reemplazo)
    return mascotas_reemplazadas



def clean_trabajo(dataframe):
    dataframe[trabajo['label']] = dataframe[trabajo['label']].apply(lambda row: limpiar_trabajo_incoherencia(row))

def limpiar_trabajo_incoherencia(trabajos):
    # Si tengo 'trabajo' y 'no trabajo' -> 'no trabajo'
    if "trabajo" in trabajos and "no trabajo" in trabajos:
        return ['no trabajo']
    return trabajos


def clean_experiencia(dataframe):
    dataframe['exp_sql'] = dataframe[experiencia['label']].apply(lambda row: any(exp in experiencia_keywords['sql'] for exp in row))
    dataframe['exp_no_sql'] = dataframe[experiencia['label']].apply(lambda row: any(exp in experiencia_keywords['nosql'] for exp in row))
    dataframe.drop(columns=[experiencia['label']], inplace=True)

def grupo_1fn(dataframe):
    dataframe[['id_grupo', 'nombre_grupo']] = dataframe['grupo'].str.split('-', expand=True)
    dataframe['id_grupo'] = dataframe['id_grupo'].apply(lambda value: 0 if value == 'docente' else value)
    dataframe['nombre_grupo'] = dataframe['nombre_grupo'].apply(lambda value: 'docente' if value is None else value)
    dataframe['id_grupo'] = dataframe['id_grupo'].astype("int32")
    dataframe.drop(columns=['grupo'], inplace=True)
