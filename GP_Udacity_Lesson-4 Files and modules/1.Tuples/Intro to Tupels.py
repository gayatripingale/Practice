"""
- It is built in type. They are silmilar to Lists.
- It is used to * store the related piece of information* 
- They are *immutable*

Q: Why tuples if they are like Lists with less features?
Ans: Tuples are usefule when you have two or more values that are 
so closely related that they always be used together.
e.g exp 1
latitude and longitude int the following ex.

- Tuples can be used to assign the multiple variables in compact way.
e.g..see exp 2 below
"""
#Exp 1

AngkorWat = (13.4125,103.866670)
print(type(AngkorWat))
print("Angkor wat is at latitude {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude {}".format(AngkorWat[1]))

#Exp 2
dimentions = 52,40,100
length,width,height = dimentions
print( "\n\nThe dimentions are {} x {} x {}".format(length,width,height))

"""
- There is also a place where the tuple's immutability is a perk. 
- Unlike list, Tuples can be stored in sets 
or useed as the keys of the dictionary as both these data structures 
need immutable keys. So lists aren't an option. 
While creating dictionary from scratch you will need tuples.

In an ex below, create a dict, "world_heritagre_location"
that has tuples of the form (latitude,longitude) as the keys and strings 
denoting the corrosponding palce names as value.

>>> world_heritage_locations = {(13.4125,103.86667): "Angkor Wat",(25.7333, 32.6):"Anciant Thebes",
30.3330556,35.4433330:"Petra",(-13.116667,-72.58333):"Machu Picchu"}



