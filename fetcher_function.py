#fetcher function

def field(record,label):
    for (fname,fvalue) in record:
        if fname == label:
            return fvalue
        
#students  in class

isaac = [['name','Isaac Mwesigwa'],['name','Isaac Mwesigwa'],['age',24],['Course','Software Engineeering']]
henry = [['name','Henry Haardman'],['age',20],['Course','Business admin']]
tom = [['name','Tom Matovu'],['age',19],['Course','BIST']]
people = [isaac,henry,tom]

for rec in people:
    print(field(rec,'name'),field(rec,'Course'), sep=', ')
    


#uncomment this and see what happens
#print(field(henry,'age'))