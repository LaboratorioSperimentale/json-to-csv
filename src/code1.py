import ndjson
import collections

import parsers as ap
import classes

with open("data/export-result.ndjson") as fin:
    data = ndjson.load(fin)
    
for dat in data:
    
    dat_info = dat["data_row"]
    name = dat_info["external_id"]
    
    dat_attributes = dat["media_attributes"]
    width = dat_attributes["width"]
    height = dat_attributes["height"]
    
    primaPagina = classes.PrimaPagina(name, height, width)

    dat_projects = dat["projects"]
    
    for proj_id, proj_data in dat_projects.items():
        if proj_data["name"] == "Prime Pagine":
            labels = proj_data["labels"]
            
            for lab in labels:
                lab_annotations = lab["annotations"]
                
                objects = lab_annotations["objects"]
                
                # per ora ignoriamo
                classifications = lab_annotations["classifications"]
                
                relationships = lab_annotations["relationships"]
                
                
                for annotation_object in objects:
                    
                    annotation_name = annotation_object["name"]
                    annotation_id = annotation_object["feature_id"]
                    toadd = False
                    
                    if annotation_name == "area of interest":
                        toadd = True
                        ret = ap.AOI(annotation_object)
                        # print("\tAOI:", name, id, ret)
                        
                    if annotation_name == "testo":
                        toadd = True
                        ret = ap.TESTO(annotation_object)
                        # print("\tTESTO", name, id, ret)
                        
                    if annotation_name == "immagine":
                        toadd = True
                        ret = ap.IMMAGINE(annotation_object)
                        # print("\tIMMAGINE", name, id, ret)
                        
                    if annotation_name == "partecipante":
                        toadd = True
                        ret = ap.PARTECIPANTE(annotation_object)
                        # print("\tPARTECIPANTE", name, id, ret)
                    
                    if toadd:
                        primaPagina.add_labels(annotation_name, annotation_id, ret)
                        
                for relationship in relationships:
                    
                    name = relationship["name"]
                    id_from = relationship["unidirectional_relationship"]["source"]
                    id_to = relationship["unidirectional_relationship"]["target"]
                    
                    primaPagina.add_relation(id_from, id_to)
                        
                print(primaPagina)             
                    
                    
