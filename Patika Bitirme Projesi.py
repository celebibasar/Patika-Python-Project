def duzliste(x):
  duzlist = []
  
  for element in x:
    if type(element) is list:
      for item in duzliste(element):
        duzlist.append(item)
      
    else:
      duzlist.append(element)
      
  return duzlist
  
  
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print('Liste:', liste)
print('Converted Flat List:', duzliste(liste))



def ters(x):
  sonuc = []
  
  for i in x[::-1]:
    if isinstance (i, list):
      sonuc.append(ters(i))
    else:
      sonuc.append(i)
  return sonuc
  
liste = ters([[1, 2], [3, 4], [5, 6, 7]])
print("Ters Liste: ", liste)
    
    
      