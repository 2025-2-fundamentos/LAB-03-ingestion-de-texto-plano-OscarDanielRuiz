"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import pandas as pd

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    registros = []
    i = 4
    while i < len(lines):
        line = lines[i].strip()
        if line and line.split()[0].isdigit():
            partes = line.split()
            cluster = int(partes[0])
            cantidad = int(partes[1])
            porcentaje = partes[2] + ("" if len(partes) < 4 else " " + partes[3])
            palabras = " ".join(partes[4:]) if len(partes) > 4 else ""
            j = i + 1
            while (
                j < len(lines)
                and not (lines[j].strip().split()[0].isdigit() if lines[j].strip() else False)
            ):
                palabras += " " + lines[j].strip()
                j += 1
            palabras = (
                palabras.replace("\n", " ")
                .replace(".", "")
            )
            lista_palabras = [
                p.strip() for p in palabras.split(",") if p.strip()
            ]
            palabras_limpias = ", ".join(lista_palabras)
            registros.append([
                cluster,
                cantidad,
                porcentaje,
                palabras_limpias
            ])
            i = j
        else:
            i += 1
    df = pd.DataFrame(
        registros,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )
    df["porcentaje_de_palabras_clave"] = (
        df["porcentaje_de_palabras_clave"]
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    ).astype(float)
    df["principales_palabras_clave"] = (
      df["principales_palabras_clave"]
      .str.replace(r"\s+", " ", regex=True)
      .str.strip()
    )
    return df


if __name__ == "__main__":
    print(pregunta_01())