import collections

class PrimaPagina:
    
    def __init__(self, name, height, width) -> None:
        self.name = name
        self.height = height
        self.width = width
        self.area = height*width
        self.data = {}
        
        
    def add_labels(self, name, ident, data_dict):
        
        self.data[ident] = collections.defaultdict(str)
        
        self.data[ident]["name"] = name
        self.data[ident]["data"] = data_dict
        
    def add_relation(self, id_from, id_to):
        
        self.data[id_from]["relation"] = id_to

        
    def __str__(self):
        
        s = f"{self.name}\n\tHEIGHT:\t{self.height}\n\tWIDTH:\t{self.width}\n\tAREA:\t{self.area}\n\n"
        
        for ident, data in self.data.items():
            
            name = data["name"]
            
            # topr = name
            
            bottomr = f"{ident}\t{data['relation']}\t"
            
            s+=f"\t{name}:{ident}\n\t\tRELATION:{data['relation']}\n\t\t"
            
            datalist = list(data["data"].items())
            datalist = [f"{x}:\t{y}" for x, y in datalist]
            
            s+="\n\t\t".join(datalist)
            s+="\n\n"
            
            # if name == "area of interest":
                
            #     dominance = data["data"]["dominance of modality"]
            #     metafora = data["data"]["main article"]
                
            #     tmp = [("dominance of modality", dominance), ("metafora", metafora)]
                
            #     s+= "\n\t\t".join(tmp)
            #     s+= "\n\n"
                
                # tmp_s = "\tAOI:".join(tmp)
                
                
            # if name == "testo":
            #     tipo = data["data"]["tipo"]
            #     metafora = data["data"]["metafora"]
            #     metafora_quot = data["data"]["metafora_quot"]
            #     target_domain = data["data"]["target_domain"]
            #     source_domain = data["data"]["source_domain"]
            #     sentiment = data["data"]["sentiment"]
            #     emotion = ", ".join(data["data"]["emotion"])
            #     metonimia = data["data"]["metonimia"]
                
                
            #     tmp = []
            #     len = 10
                
            # if name == "immagine":
            #     metafora = data["data"]["metafora"]
            #     target_domain = data["data"]["target_domain"]
            #     source_domain = data["data"]["source_domain"]
            #     sentiment = data["data"]["sentiment"]
            #     emotion = ", ".join(data["data"]["emotion"])
            #     cultural_context = data["data"]["cultural context"]
            #     metonimia = data["data"]["metonimia"]
            #     metafora_exp = data["data"]["metafora_exp"]
            #     angle = data["data"]["angle"]
            #     closeness = data["data"]["closeness"]
            #     len = 12

            # if name == "participant":
                
            #     type = data["data"]["type"]
            #     gaze = data["data"]["gaze"]
            #     gesture = data["data"]["gesture"]
            #     posture = data["data"]["posture"]
            #     role = data["data"]["role"]
            #     processo = ", ".join(data["data"]["processo"])
            #     len = 6
                 
            
        return s
            #TODO: name + ident
            #TODO: loop over properties (from list) and print value
            