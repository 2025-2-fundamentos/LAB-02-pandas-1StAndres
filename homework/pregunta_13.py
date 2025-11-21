"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd
    from pathlib import Path

    data_dir = Path(__file__).resolve().parent.parent / "files" / "input"

    # Leer los archivos tbl0.tsv y tbl2.tsv
    tbl0 = pd.read_csv(str(data_dir / "tbl0.tsv"), sep="\t")
    tbl2 = pd.read_csv(str(data_dir / "tbl2.tsv"), sep="\t")

    # Hacer el merge de los dos DataFrames usando 'c0' como clave
    merged_df = pd.merge(tbl0, tbl2, on='c0')

    # Calcular la suma de 'c5b' por cada valor en 'c1'
    resultado = merged_df.groupby('c1')['c5b'].sum()

    return resultado

