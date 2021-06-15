
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection


gis = GIS("https://www.arcgis.com","user","password")
print(gis)

layerSearch = gis.content.search(query="teste_script", item_type="Feature Layer")
print(layerSearch)
exportLayer = FeatureLayerCollection.fromitem(layerSearch[0])

for lyr in exportLayer.layers:
    if lyr.attachments:
        query_features = lyr.query(where='1=1')
        oidField = query_features.object_id_field_name
        for f in query_features.features:
            f_id = f.get_value(oidField)
            attach_list = lyr.attachments.get_list(oid=f_id)
            for attach in attach_list:
                attach_id = attach['id']
                lyr.attachments.download(oid=f_id, attachment_id=attach_id, save_path="C:/tmp/attach")

for tbl in exportLayer.tables:
    if tbl.attachments:
        query_features = tbl.query(where='1=1')
        oidField = query_features.object_id_field_name
        for f in query_features.features:
            f_id = f.get_value(oidField)
            attach_list = tbl.attachments.get_list(oid=f_id)
            for attach in attach_list:
                attach_id = attach['id']
                tbl.attachments.download(oid=f_id, attachment_id=attach_id, save_path="C:/tmp/attach")