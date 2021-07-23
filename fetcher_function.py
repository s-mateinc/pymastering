#fetcher function

def field(record,label):
    for (fname,fvalue) in record:
        if fname == label:
            return fvalue
        
#students  in class

isaac = [['name','Isaac Mwesigwa'],['name','Isaac Mwesigwa'],['age',24],['Course','Software Engineeering']]
henry = [['name','Henry Haardman'],['age',20],['Business admin']]
tom = [['name','Tom Matovu'],['age',19],['Course','BIST']]

print(field(isaac,'name'))
print(field(tom,'Course'))


#uncomment this and see what happens
#print(field(henry,'age'))