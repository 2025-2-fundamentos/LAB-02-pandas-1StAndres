"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    import pandas as pd
    from pathlib import Path

    # Construir ruta absoluta a files/input desde la ubicación de este archivo
    data_dir = Path(__file__).resolve().parent.parent / "files" / "input"

    # Leer el archivo tbl0.tsv
    df = pd.read_csv(str(data_dir / "tbl0.tsv"), sep="\t")

    # Contar la cantidad de registros por cada letra en la columna 'c1'
    conteo = df['c1'].value_counts().sort_index()

    return conteo
