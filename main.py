try:
    dictionary_record, id, property, value = input("Input : ").strip().split("|")
except:
    print("Invalid")
    quit()

try:
    dictionary_record = eval(dictionary_record.strip())
    id = id.strip()
    property = property.strip()
    value = value.strip()
    if value == "''" or value.replace("'", "").strip() == "":
        value = ""
except:
    print("Invalid")
    quit()
    
# check dict
for x in dictionary_record:
    if not x.isdigit() or x.startswith("0") or int(x) <= 0:
        print("Invalid")
        quit()  
          
# check id
id = str(id)
if not id.isdigit() or id.startswith("0") or int(id) <= 0:
    print("Invalid")
    quit()
    
# check property
if property not in ["artist", "albumTitle", "tracks"]:
    print("Invalid")
    quit()