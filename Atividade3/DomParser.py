from xml.dom.minidom import parse
import time
inicial = time.time()
MapDocument = parse('map.osm')

print("Starting DOM Parser...")
for c in MapDocument.getElementsByTagName("node"):
	isAmenity = False
	for i in c.getElementsByTagName("tag"):
		k = i.getAttribute("k")
		if k == "amenity":
			isAmenity = True
			print('Latitude: ',  c.getAttribute("lat"))
			print('Longitude: ',  c.getAttribute("lon"))
			print('Tipo: ', i.getAttribute("v"))
		if(k == "name" and isAmenity == True): 
			print("Nome: ", i.getAttribute("v"))
			isAmenity = False
			print("\n")
		
	
print('Tempo de execucao: ', time.time() - inicial, '(S)')		
			

		
			