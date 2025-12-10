import pandas as pd

diccionario = [
    {
        "titular": "Noticia 1",
        "fecha": "2025-12-09",
        "contenido": "Este es el contenido de la noticia 1"
    },
    {
        "titular": "Noticia 2",
        "fecha": "2025-12-10",
        "contenido": "Este es el contenido de la noticia 2"
    },
    {
        "titular": "Noticia 3",
        "fecha": "2025-12-11",
        "contenido": "Este es el contenido de la noticia 3"
    }
]

# Convertir a DataFrame
df = pd.DataFrame(diccionario)

# Exportar a Excel
df.to_excel("noticias.xlsx", index=False)

print("Archivo creado: noticias.xlsx")
