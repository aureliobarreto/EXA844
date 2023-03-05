import xml.sax
import time
inicial = time.time()

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.nodeLat = ""
    self.nodeLon = ""
    self.tipo = None
    self.nome = ""
    self.isAmenity = False

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
        #print("Tipo: ",attributes.get("k"))
       
  def endElement(self, tag):    
    if tag =="node" and self.tipo:         
      print("Nome: ",self.nome)
      print("Tipo: ",self.tipo)                  
      print("Latitude:", self.nodeLat)
      print("Longitudde:", self.nodeLon)
      print("\n")        

  def characters(self, content):
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
print('Tempo de execucao: ', time.time() - inicial, '(S)')