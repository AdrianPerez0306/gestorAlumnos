import numpy as np
import pandas as pd

from cleaning_funcs import reemplazar_dni_nan, extract_columns_from_description, clean_materias, fill_empty_with_none, \
    clean_mascotas, clean_trabajo, clean_experiencia, grupo_1fn

df_alumnos_BdD = pd.read_csv('raw-data.csv')

# Convertir todas las columnas de tipo string a minúsculas
df_alumnos_BdD = df_alumnos_BdD.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)

# nombres de columnas sin acento, mayuscula, etc.
column_names = ['dni', 'apellido', 'nombre', 'email', 'grupo', 'rol', 'descripcion']
df_alumnos_BdD.columns = column_names


#ESTO ES PARA RELLENAR LOS DNI vacios que estaban en el excel. Pandas los toma como NaN, y sabemos
# que esos datos existe, solo ue se olvidaron de completarlo. Se podria eliminar los registros, pero
# por comodidad se rellenan con algun dni random entre 41 Y 42 MILLONES
#Luego si algun registro cumple que tiene una determinada cantidad de columnas como NaN , y son PK
# deberian eliminarse. E.g:tiene nombre y/oapellido y/o email y/o grupo con NaN, se elimina.
df_alumnos_BdD['dni'] = reemplazar_dni_nan(df_alumnos_BdD['dni'])

#Me interesa el DNI como tipo int, ya que no hay DNI`s con coma(,). El resto como tipo string, ya que
# labels como nombre, apellido, email.
#DNI sin formato FLOAT
df_alumnos_BdD['dni'] = df_alumnos_BdD['dni'].astype("int32")

#Limpio los grupos para que quede 'N-nombreGrupo' y NO 'N - nombreGrupo'
df_alumnos_BdD['grupo'] = df_alumnos_BdD['grupo'].replace(r'\s*-\s*', '-', regex=True)


extract_columns_from_description(df_alumnos_BdD)

clean_materias(df_alumnos_BdD)

clean_mascotas(df_alumnos_BdD)
# fill_empty_with_none(df_alumnos_BdD)
clean_trabajo(df_alumnos_BdD)
clean_experiencia(df_alumnos_BdD)
grupo_1fn(df_alumnos_BdD)

df_alumnos_BdD['series'] = df_alumnos_BdD['series'].apply(lambda col: [value.lower() for value in col]  )
df_alumnos_BdD['localidad'] = df_alumnos_BdD['localidad'].apply(lambda col: [value.lower() for value in col]  )
df_alumnos_BdD.to_csv(r"/home/the14th/Downloads/database.csv", index=True)

