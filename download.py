from arcgis.gis import GIS
import time

gis = GIS('', '','')
print("Conexão realizada com sucesso!",gis)
inicio = time.time()
parameters= str({"0":{"where": "objectid <= 1"}, "1":{"where": "objectid <= 1"},"2":{"where": "objectid <= 1"}})

conteudo = gis.content.get('aacf59f8d68c459fa4af1ae266b09270')
layer = conteudo.layers
cont_exp = layer[0]

output_file = conteudo.export(title=cont_exp,export_format="File Geodatabase",parameters=parameters)
output_file.download(r'C:\tmp')
fim = time.time()
print(fim - inicio)