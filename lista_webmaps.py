
from arcgis.gis import GIS
from arcgis.gis import Item

online = GIS("","","", verify_cert=False)
srcMap = online.content.search("owner:*", item_type="Web Map",max_items=1000 )

token = online._con.token

txtfile = open("C:/tmp/lista.txt","w")
txtfile.write("Titulo;URL")
txtfile.write("\n")

for webmap in srcMap:
    print("Titulo: " + webmap.title, "\nWebmap.id: " + webmap.id, "\nOwner: " + webmap.owner)
    txtfile.write("\n")
    txtfile.write("Titulo: " + webmap.title)
    txtfile.write("\n")
    txtfile.write("ID:" + webmap.id)
    txtfile.write("\n")
    featdata = webmap.get_data()
    try:
        for layer in featdata['operationalLayers']:
            print(layer['url'])
            txtfile.write("URL Sem TOKEN: " + layer['url'])
            txtfile.write("\n")
            #txtfile.write("URL COM TOKEN: " + layer["url"] + '?token=' + str(token))
            #txtfile.write("\n")
    except:
        print("Web Map sem camadas")
        txtfile.write("Web Map sem camadas")
        txtfile.write("\n")



txtfile.close()
