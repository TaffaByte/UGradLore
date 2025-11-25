import math

# INSTRUCTIONS >> DO NOT MODIFY EXISTING CODE USE the FUNCTIONS MENTIONED IN THE FILE 
# YOU CAN CREATE YOUR OWN FUNCTIONS IF NEEDED

#Takes size as Input
#Returns Empty hast table of 'size'
#DO NOT MODIFY THIS CODE
def create_hashtable(size): # returns list of dictionaries
    htable=[{}]*size
    for i in range(size):
        htable[i]={"ID": None,
                   "DATA": None}
    return htable



#Takes Existing hashtable, size and a bool indicating wether to increase or decrease the size
#Returns a Tuple Containing new Hash Table and its New Size (Hashtable,newsize)
def resize_hashtable(hashtable,size,increase):
    
    #dont recall put function here - Ms Aisha
    pass

#Takes Key and size as parameters
#Returns Original address of type(int) for the Key using the Hash Function Mentioned in the Document
def hash_function(key,size):
  pass


##Takes Key , OldAddress  and size as parameters
#Returns new address of type(int) for the Key using the Key Offset method Mentioned in the Document
def collision_resolver(key,oldAddress,size):
    pass

#Takes hashtable, key, data and size and Insert key and Data into the Hash Table 
# After Insertion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable and its Size as a Tuple (hashtable,size)
def put(hashtable,key, data,size):
   pass
  

#Takes hashtable and size as parameters 
# Returns load factor of type float   
def loadFactor(hashtable,size):
    pass

#Takes in hash table, key, Name of the Column to be updated, 
# size of hash table, Collision Path and Operation Number as Parameters
#Searches for the key in hashtable and update the Column Name of the hashtable also updates the collision path of the key
#Returns Nothing
def Update(hashtable,key, columnName, size,collision_path,opNumber):
    pass
        
# Update the Column Name of the hashtable founf at Index
#Returns Nothing
def UpdateAtIndex(hashtable,index,columnName):
  pass
    
   
#Takes hash table, key, size , Collision path and Operation Number as parameters
# Searches for the key in Hash table update the Collision path and 
#If key is found returns a Tuple Containing 'DATA' part of the Hash table and the index of the key  
# Return format -> (hashtable[index]['DATA],index)  
#If key is not Found return (None,None)
def get(hashtable,key,size,collision_path,opNumber):
    pass


#Takes hashtable, key, size , Collision path and operation Number 
# Delete key and Data from the Hash Table 
# After deletion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable 
def delete(hashtable, key, size,collision_path,opNumber):
    pass