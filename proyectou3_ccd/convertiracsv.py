import pandas as pd

# carga el archivo txt, separa las columnas por uno o mas espacios e indica el nombre de las columnas
df = pd.read_csv(r"C:\Users\caroq\OneDrive\Documentos\TecXD\10\cienciadedatos\proyectoU3_ccd\dataset_culiacan.txt", sep=r"\s+", names=["fecha", "precip", "evap", "tmax", "tmin"])

#transforma el archivo txt a csv con la funcion de pandas to_csv
df.to_csv(r"C:\Users\caroq\OneDrive\Documentos\TecXD\10\cienciadedatos\proyectoU3_ccd\25161_GVE01_08052026.csv", index=False)