from arcgis.gis import GIS
from IPython.display import display

gis = GIS("https://www.arcgis.com", 'user', 'password')
search_result = gis.content.search('calc', item_type='Feature Layer')
ports_item = search_result[0]
ports_layers = ports_item.layers

ports_fset = ports_layers[0].query()
ports_flayer = ports_layers[0]

ports_features = ports_fset.features

for f in ports_features:
    if f.attributes['a'] >= 1:
        valores = f.attributes['a'] + f.attributes['b']
        soma = valores
        sfo_edit = f
        sfo_edit.attributes['c'] = soma
        display(sfo_edit)
        try:
            update_result = ports_flayer.edit_features(updates=[sfo_edit])
        except:
            pass

