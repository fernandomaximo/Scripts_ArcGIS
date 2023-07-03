from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

#Script utilizado para capturar o keywords das imagens

gis = GIS("https://arcgis.com/","usuario","senha")
print("Conexão realizada com sucesso!",gis)

txtfile = open("C:/tmp/itens.txt","w")
txtfile.write("Lista de conteudo:")
txtfile.write("\n")

conteudo = gis.content.get('')
tabela = conteudo.layers[0]
valor = 0
while (valor <= 2):
    att = tabela.attachments.get_list(oid=valor)
    # print(att)
    valor = valor + 1
    for x in att:
        print(x)
        txtfile.write("ID: " + str(x['id']) + " ")
        txtfile.write("globalId: " + x['globalId'] + " ")
        txtfile.write("keywords: " + x['keywords'] + " ")
        txtfile.write("\n")



