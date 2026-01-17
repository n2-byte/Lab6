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