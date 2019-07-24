import time
d={}#'d' is the dictionary in which we store data
#for create operation use the syntax "create(key_name,key_value,key_timeout)", timeout value is the integer value of seconds for time-to-live property
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #if key exists already with the input key_name, it returns an error
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: the limit of data storage(1GB) is already reached!! Delete any unused items to create new one")#error message after maximum data storage
        else:
            print("error: Invalind key_name! key_name must contain only alphabets")
#for read operation use the syntax "read(key_name)", it returns the value assigned to that respective key_name if any
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message if wrong key is entered
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time to live of",key,"has expired") #error message when tried to access key whose time-to-live was expired
        else:
            stri=str(key)+":"+str(b[0])
            return stri
#for delete operation, use the syntax "delete(key_name)", which will delete the respective key from the database
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message if wrong key is entered
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
            else:
                print("error: time to live of",key,"has expired") #error message when tried to access key whose time-to-live was expired
        else:
            del d[key]

#I have added an additional feature of modify operation in order to change the value of key later after it's creation
#for modify operation, use the syntax "modify(key_name,new_value)"
def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message if wrong key is entered
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time to live of",key,"has expired") #error message when tried to access key whose time-to-live was expired
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message if wrong key is entered
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
        

        
        
    



