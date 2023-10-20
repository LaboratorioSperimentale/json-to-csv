import ndjson
import collections

import parsers as ap
import classes

with open("data/export-result-full.ndjson") as fin:
    data = ndjson.load(fin)
        
        
fout_PRIMEPAGINE = open("data/export_primepagine.tsv", "w")
fout_ANNOTAZIONI = open("data/export_annotazioni.tsv", "w")
fout_AREASOFINTEREST = open("data/export_areasofinterest.tsv", "w")
fout_IMAGES = open("data/export_images.tsv", "w")
fout_TEXTS = open("data/export_texts.tsv", "w")
fout_PARTICIPANTS = open("data/export_participants.tsv", "w")

head_primepagine = "NAME\tWIDTH\tHEIGTH\tAREA\tIN_CROSSVAL"
print(head_primepagine, file=fout_PRIMEPAGINE)

head_annotazioni = "PRIMA_PAGINA\tANNOTATOR\tTYPE\tID"
print(head_annotazioni, file=fout_ANNOTAZIONI)

head_aois = "ANNOTATOR\tPRIMA_PAGINA\tID\tMAIN_ARTICLE\tCOVID_RELATED\tDOMINANCE\tAREA"
print(head_aois, file=fout_AREASOFINTEREST)

head_images = "ANNOTATOR\tPRIMA_PAGINA\tID\tCLOSENESS\tANGLE\tAREA\tCULTURAL_CONTEXT\tMETAPHOR\tMETAPHOR_EXP\tTARGET\tSOURCE\tSENTIMENT\tEMOTION\tMETONIMIA\tCONTAINED_IN"
print(head_images, file=fout_IMAGES)

head_texts = "ANNOTATOR\tPRIMA_PAGINA\tID\tTYPE\tAREA\tMETAPHOR\tMETAPHOR_QUOT\tTARGET\tSOURCE\tSENTIMENT\tEMOTION\tMETONIMIA\tCONTAINED_IN"
print(head_texts, file=fout_TEXTS)

head_participants = "ANNOTATOR\tPRIMA_PAGINA\tID\tAREA\tTYPE\tGAZE\tGESTURE\tPOSTURE\tROLE\tPROCESS\tCONTAINED_IN"
print(head_participants, file=fout_PARTICIPANTS)
    
for dat in data:
    
    dat_info = dat["data_row"]
    NAME = dat_info["external_id"]
    
    dat_attributes = dat["media_attributes"]
    WIDTH = dat_attributes["width"]
    HEIGTH = dat_attributes["height"]
    
    primaPagina = classes.Image(NAME, HEIGTH, WIDTH)
    
    METADATA = False
    dat_metadata = dat["metadata_fields"]
    if len(dat_metadata) > 0:
        METADATA = True
    

    print(f"{NAME}\t{WIDTH}\t{HEIGTH}\t{WIDTH*HEIGTH}\t{METADATA}", file=fout_PRIMEPAGINE)

    dat_projects = dat["projects"]
    
    for proj_id, proj_data in dat_projects.items():

        labels = proj_data["labels"]        
        for lab in labels:
            
            ANNOTATOR = lab["label_details"]["created_by"]
            
            AOIS = {}
            IMGS = {}
            TXTS = {}
            PRTS = {}
            
            lab_annotations = lab["annotations"]
        
            objects = lab_annotations["objects"]
             
            relationships = lab_annotations["relationships"]
                
            for annotation_object in objects:
                
                annotation_name = annotation_object["name"]
                annotation_id = annotation_object["feature_id"]
                
                print(f"{NAME}\t{ANNOTATOR}\t{annotation_name}\t{annotation_id}", file=fout_ANNOTAZIONI)
            
                if annotation_name == "area of interest":
                    ret = ap.AOI(annotation_object)
                    AOIS[annotation_id] = ret
                    
                if annotation_name == "testo":
                    ret = ap.TESTO(annotation_object)                    
                    TXTS[annotation_id] = ret
                    
                if annotation_name == "immagine":
                    ret = ap.IMMAGINE(annotation_object)
                    IMGS[annotation_id] = ret

                if annotation_name == "partecipante":  
                    ret = ap.PARTECIPANTE(annotation_object)
                    PRTS[annotation_id] = ret
                
            for relationship in relationships:
                
                name = relationship["name"]
                
                id_from = relationship["unidirectional_relationship"]["source"]
                id_to = relationship["unidirectional_relationship"]["target"]
                
                if id_from in AOIS:
                    AOIS[id_from]["contained_in"] = id_to
                    
                if id_from in TXTS:
                    TXTS[id_from]["contained_in"] = id_to
                    
                if id_from in IMGS:
                    IMGS[id_from]["contained_in"] = id_to
                    
                if id_from in PRTS:
                    PRTS[id_from]["contained_in"] = id_to
                    
            
            # UPDATE MISSING RELATIONSHIPS 
            for prt, prt_data in PRTS.items():
                # print(prt_data)
                if not "contained_in" in prt_data:
                    if len(IMGS) == 1:
                        prt_data["contained_in"] = list(IMGS.keys())[0]
                        # print(prt_data)
                    else:
                        print(NAME)
                        print("UNABLE TO ADD CONTAINED RELATION FOR PARTICIPANT", prt, ANNOTATOR)
                        
            for img, img_data in IMGS.items():
                if not "contained_in" in img_data:
                    if len(AOIS) == 1:
                        img_data["contained_in"] = list(AOIS.keys())[0]
                    else:
                        print(NAME)
                        print("UNABLE TO ADD CONTAINED RELATION FOR IMAGE", img, ANNOTATOR)
            
            for txt, txt_data in TXTS.items():
                if not "contained_in" in txt_data:
                    if len(AOIS) == 1:
                        txt_data["contained_in"] = list(AOIS.keys())[0]
                    else:
                        print(NAME)
                        print("UNABLE TO ADD CONTAINED RELATION FOR TEXT", txt, ANNOTATOR)
            
            
            for aoi_id, aoi_data in AOIS.items():
                
                s = f"{ANNOTATOR}\t{NAME}\t{aoi_id}\t{aoi_data['main article']}\t{aoi_data['covid related']}\t{aoi_data['dominance of modality']}\t{aoi_data['area']}\t{aoi_data['conained_in']}"
                print(s, file=fout_AREASOFINTEREST)
                
                
            for img_id, img_data in IMGS.items():
                
                s = f"{ANNOTATOR}\t{NAME}\t{img_id}\t{img_data['closeness']}\t{img_data['angle']}\t{img_data['area']}\t{img_data['cultural context']}\t{img_data['metafora']}\t{img_data['metafora_exp']}\t{img_data['target domain']}\t{img_data['source domain']}\t{img_data['sentiment']}\t{img_data['emotion']}\t{img_data['metonimia']}\t{img_data['contained_in']}"
                print(s, file=fout_IMAGES)
                
                
            for txt_id, txt_data in TXTS.items():
                s = f"{ANNOTATOR}\t{NAME}\t{txt_id}\t{txt_data['type']}\t{txt_data['area']}\t{txt_data['metafora']}\t{txt_data['metafora_quot']}\t{txt_data['target domain']}\t{txt_data['source domain']}\t{txt_data['sentiment']}\t{txt_data['emotion']}\t{txt_data['metonimia']}\t{txt_data['contained_in']}"
                print(s, file=fout_TEXTS)


            for prt_id, prt_data in PRTS.items():
                s = f"{ANNOTATOR}\t{NAME}\t{prt_id}\t{prt_data['area']}\t{prt_data['gaze']}\t{prt_data['gesture']}\t{prt_data['posture']}\t{prt_data['role']}\t{prt_data['process']}\t{prt_data['contained_in']}"
                print(s, file=fout_PARTICIPANTS)