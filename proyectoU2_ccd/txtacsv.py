import pandas as pd

# carga el archivo txt, separa las columnas por uno o mas espacios e indica el nombre de las columnas
df = pd.read_csv(r"C:\Users\caroq\OneDrive\Documentos\TecXD\10\cienciadedatos\proyectoU2_ccd\25001.txt", sep=r"\s+", names=["fecha", "precip", "evap", "tmax", "tmin"])

#transforma el archivo txt a csv con la funcion de pandas to_csv
df.to_csv(r"C:\Users\caroq\OneDrive\Documentos\TecXD\10\cienciadedatos\proyectoU2_ccd\25001_GVE01_14052025.csv", index=False)