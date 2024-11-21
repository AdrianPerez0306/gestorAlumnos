########################################################################################
################    TRABAJOS KEYWORDS
########################################################################################
trabajo_keywords = {
    "trabaja":['trabajo', 'desarrollador', 'freelance', 'seguro', 'docente', 'ingeniero de datos', 'pasante','comercio', 'administrativo', 'informatica', 'oficina'],
    "no_trabaja":[ 'no trabajo', 'no estoy trabajando', 'busco']
}
trabajos_keywords_all = trabajo_keywords['trabaja'] + trabajo_keywords['no_trabaja']



########################################################################################
################    MATERIAS KEYWORDS
########################################################################################
materia_keyword_pseudonimos = ["pack de 3", "3 materias"]
replacement_pack = ['algoritmos_3', 'seminario', 'base_de_datos']
materia_keywords = {
    "algoritmos_3":["algoritmos 3", "algo 3", "algo3"],
    "seminario":["seminario", "prog. concurrente", "Seminario de Programación"],
    "base_de_datos":["base de datos", "bdd", "bases de datos", "bd"],
    "caso": ["caso"]
}
materias_keywords_all = materia_keyword_pseudonimos + materia_keywords['algoritmos_3'] + materia_keywords['seminario'] + materia_keywords['base_de_datos'] + materia_keywords['caso']



########################################################################################
################    LOCALIDAD KEYWORDS
########################################################################################
localidades_keywords = ["San Martin", "J.L Suarez", "General Pacheco", "Belgrano", "Santos Lugares", "Escobar", "Boedo", "Villa Gesell", "Villa Bosch", "Ciudad Jardin", "CABA", "Laferrere", "Chilavert", "Villa Urquiza", "Loma Hermosa", "San Andres"]



########################################################################################
################    EXPERIENCIA KEYWORDS
########################################################################################
experiencia_keywords = {
    "sql":["sql server", "mysql", "postgresql" , "ms-sql", "sql developer", "sqlserver", "power bi", "access"],
    "nosql":[ "firebase", "dynamodb", "mongodb"]
}
experiencia_keywords_all = experiencia_keywords['sql'] + experiencia_keywords['nosql']



########################################################################################
################    HOBBIES KEYWORDS
########################################################################################
hobbies_keywords = ["guitarra", "viajar", "videojuegos", "mangas", "anime", "cantar", "correr", "natación", "gimnasio", "voley", "fútbol", "ajedrez", "jardinería", "series", "películas", "música", "leer"]



########################################################################################
################    MASCOTAS KEYWORDS
########################################################################################
mascota_keyword = {
    "perro":["perrito", "perro", "perrita", "perra", "canino"],
    "gato":[ "gato", "gata", "gatito", "gatita", "mishisho"],
    "gorrion": ["gorrion", "gorriones"]
}

mascotas_keywords_all = mascota_keyword['perro'] + mascota_keyword['gato'] + mascota_keyword['gorrion']

########################################################################################
################    MUSICA KEYWORDS
########################################################################################
musica_keywords = ["rock nacional", "the beatles", "arctic monkeys", "radiohead", "foofighters", "wos", "queen", "los piojos", "miranda!", "top 50", "the hives", "metal", "electronica", "trap argentino", "tropicales", "bandas sonoras"]


########################################################################################
################    SERIES KEYWORDS
########################################################################################
series_keywords = ["Supernatural", "The Boys", "The Bear", "The Office", "Soy Betty La Fea", "House of the Dragon", "Arcane", "Dark", "Black Mirror", "Better Call Saul"]





