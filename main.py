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
    
def update_records(dictionary_record, id, property, value):
    # create new id
    if id not in dictionary_record:
        dictionary_record[id] = {}
    # delete
    if value == "":
        if property in dictionary_record[id]:
            del dictionary_record[id][property]
            return dictionary_record
        else:
            return "Invalid"
    # add
    if property != "tracks":
        dictionary_record[id][property] = value
        return dictionary_record
    # tracks
    if "tracks" not in dictionary_record[id]:
        dictionary_record[id]["tracks"] = []

    dictionary_record[id]["tracks"].append(value)

    return dictionary_record

print(update_records(dictionary_record, id, property, value))