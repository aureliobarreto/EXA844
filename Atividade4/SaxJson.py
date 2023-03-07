import xml.sax
import time
import json

from numpy import append
inicial = time.time()

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.nodeLat = ""
    self.nodeLon = ""
    self.tipo = None
    self.nome = ""
    self.isAmenity = False
    self.locais = []

  def startElement(self, tag, attributes):    
    self.currentData = tag
    
    if tag =="node":
      self.nome = ""
      self.tipo = None  
      self.nodeLat = attributes.get("lat")
      self.nodeLon = attributes.get("lon")  
    if tag =="tag":

        if attributes.get("k") == "amenity":
          self.tipo =  attributes.get("v")
             
        elif attributes.get("k") == "name":
          self.nome =  attributes.get("v") 

       
  def endElement(self, tag):    
    if tag =="node" and self.tipo:         
      print("Nome: ",self.nome)
      print("Tipo: ",self.tipo)                  
      print("Latitude:", self.nodeLat)
      print("Longitudde:", self.nodeLon)
      self.locais.append((self.nome, self.tipo, self.nodeLon, self.nodeLat))
      print("\n")        

  def characters(self, content):
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
print('Tempo de execucao: ', time.time() - inicial, '(S)')
print(Handler.locais)
geojson = {}
geojson['type'] = 'FeatureCollection'
geojson['features'] = []



for item in Handler.locais:
  feature = {}
  feature['type'] = 'Feature'
  feature['geometry'] = {}
  feature["geometry"]['type'] = 'Point'
  feature["geometry"]['coordinates'] = [float(item[2]), float(item[3])]
  feature["properties"] = {}
  feature["properties"]['nome'] = item[0]
  feature["properties"]['tipo'] = item[1]
  geojson['features'].append(feature)



#jsonStr = json.dumps(livro, indent=4, ensure_ascii=False)
print(geojson)
