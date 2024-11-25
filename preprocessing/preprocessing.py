import pandas as pd

from cleaning_funcs import reemplazar_dni_nan, extract_columns_from_description, clean_materias, fill_empty_with_none, \
    clean_mascotas, clean_trabajo, clean_experiencia, clean_grupos, pipeline_inicial, trabajo, limpiar_no_trabajo

path = '/home/the14th/Downloads/'
df_alumnos_BdD = pd.read_csv('raw-data.csv')

df_alumnos_BdD = pipeline_inicial(df_alumnos_BdD)


# LIMPIO LA COLUMNA DESCRIPCION
extract_columns_from_description(df_alumnos_BdD)
# Aplico LOWER a series y localidad
df_alumnos_BdD['series'] = df_alumnos_BdD['series'].apply(lambda col: [value.lower() for value in col]  )
df_alumnos_BdD['localidad'] = df_alumnos_BdD['localidad'].apply(lambda col: [value.lower() for value in col]  )

# LImpieza y estandarizacion
clean_materias(df_alumnos_BdD)
clean_mascotas(df_alumnos_BdD)
clean_trabajo(df_alumnos_BdD)
clean_experiencia(df_alumnos_BdD)
clean_grupos(df_alumnos_BdD)

# LOS VALORES QUE PUEDAN ESTAR VACIOS, SERAN VACIOS
fill_empty_with_none(df_alumnos_BdD)
df_alumnos_BdD[trabajo['label']] = df_alumnos_BdD[trabajo['label']].apply(lambda row: limpiar_no_trabajo(row))
df_alumnos_BdD.rename(columns={"rol": "nombre_rol"}, inplace=True)



# EXPORTAR ARCHIVOS A CSV

# TABLA GRUPOS
df_grupo = df_alumnos_BdD['nombre_grupo'].drop_duplicates()
df_grupo.to_csv(f'{path}grupos.csv', index=False)

# TABLA ROL
df_rol = df_alumnos_BdD['nombre_rol'].drop_duplicates()
df_rol.to_csv(f'{path}roles.csv', index=False)


###################################################################
################ TABLAS PARA  MATERIAS
###################################################################
# TABLA MATERIAS-UNIQUE
df_materias = df_alumnos_BdD.explode('materias').reset_index(drop=True)
df_materias.rename(columns={"materias": "nombre_materia"}, inplace=True)
df_materias_unique = df_materias['nombre_materia'].drop_duplicates()
df_materias_unique.to_csv(f'{path}materias.csv', index=False)


###################################################################
###################################################################

######################################################################################################################################
######################################################################################################################################

###################################################################
################ TABLA PROFESION (1 a n de alumno a mascota)
###################################################################
df_trabajos = df_alumnos_BdD['trabajo'].explode().unique()
df_profesiones_unique = pd.DataFrame({'nombre_profesion': df_trabajos})
# df_profesiones_unique = df_profesiones_unique[df_profesiones_unique['nombre_profesion'] != 'docente']
df_profesiones_unique = df_profesiones_unique[df_profesiones_unique['nombre_profesion'] != 'trabajo']
df_profesiones_unique = df_profesiones_unique[df_profesiones_unique['nombre_profesion'] != 'no trabajo']
df_profesiones_unique = df_profesiones_unique.dropna()
df_profesiones_unique.to_csv(f'{path}profesiones.csv', index=False)
###################################################################
###################################################################

######################################################################################################################################

###################################################################
################ TABLA LOCALIDAD (n a 1 de alumno a localidad)
###################################################################
localidades_unicas = df_alumnos_BdD['localidad'].explode().unique()
df_localidades_unique = pd.DataFrame({'nombre_localidad': localidades_unicas})
df_localidades_unique = df_localidades_unique[ 'nombre_localidad']
df_localidades_unique.to_csv(f'{path}localidades.csv', index=False)
###################################################################
###################################################################

######################################################################################################################################

###################################################################
################ TABLA HOBBIES (n a n)
###################################################################
# TABLA HOBBIES-UNIQUE
df_hobbies = df_alumnos_BdD.explode('hobbies').reset_index(drop=True)
df_hobbies.rename(columns={"hobbies": "nombre_hobbie"}, inplace=True)
df_hobbies_unique = df_hobbies['nombre_hobbie'].drop_duplicates().dropna()
df_hobbies_unique.to_csv(f'{path}hobbies.csv', index=False)

###################################################################
###################################################################

######################################################################################################################################

###################################################################
################ TABLA SERIES (n a n)
###################################################################
# TABLA MATERIAS-UNIQUE
df_series = df_alumnos_BdD.explode('series').reset_index(drop=True)
df_series.rename(columns={"series": "nombre_serie"}, inplace=True)
df_series_unique = df_series['nombre_serie'].drop_duplicates().dropna()
df_series_unique.to_csv(f'{path}series.csv', index=False)

# TABLA RECOMIENDA
# df_series = df_series[['id_serie', 'nombre_serie', 'id_alumno']].dropna()
# df_series = df_series[['id_serie', 'id_alumno']]
# df_series.to_csv(r"/home/the14th/Downloads/interr_binaria_alumno_serie.csv", index=False)
###################################################################
###################################################################

######################################################################################################################################

###################################################################
################ TABLA MUSICA (n a n)
###################################################################
# TABLA MUSICA-UNIQUE
df_musica = df_alumnos_BdD.explode('musica').reset_index(drop=True)
df_musica.rename(columns={"musica": "nombre_musica"}, inplace=True)
df_musica_unique = df_musica['nombre_musica'].drop_duplicates().dropna()
df_musica_unique.to_csv(f'{path}musica.csv', index=False)

###################################################################
###################################################################

######################################################################################################################################

#

# Nota:Alumnos depende de tener las tablas de localidad y profesiones ya armadas. Asi se aplica ETL
###################################################################
################ TABLA ALUMNOS
###################################################################
#Alumno
df_alumno = df_alumnos_BdD[['dni', 'nombre', 'apellido', 'email', 'exp_sql','exp_no_sql', 'trabajo', 'localidad', 'materias']].copy()
df_alumnos_BdD['hobbies'] = df_alumnos_BdD['hobbies'].apply(lambda row: row if row is None else set(row))
df_alumnos_BdD['musica'] = df_alumnos_BdD['musica'].apply(lambda row: row if row is None else set(row))
df_alumnos_BdD['series'] = df_alumnos_BdD['series'].apply(lambda row: row if row is None else set(row))
df_alumnos_BdD['mascotas'] = df_alumnos_BdD['mascotas'].apply(lambda row: row if row is None else set(row))
df_alumnos_BdD['localidad'] = df_alumnos_BdD['localidad'].apply(lambda row: row[0])
df_alumnos_BdD['trabajo'] = df_alumnos_BdD['trabajo'].apply(lambda row: row if row is None else row[0])
df_alumnos_BdD.to_csv(f'{path}alumno.csv', index=False)
###################################################################
###################################################################
