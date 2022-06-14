mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
z=mydict.values()
print(z)
w=mydict.items()
print(w)
mydict['type']="mamals"
#y= mydict.get("brand")
#x= mydict.keys()
#print(y)
#print(x)
#mydict["color"]="green"
#print(mydict)
mydict.update({"year":2020})
print(mydict)