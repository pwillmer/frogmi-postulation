import json
import datetime
from store import Store
 
#Date parameters must be within the range of the created data
MIN_DATE = datetime.date(2022, 1, 25) 
MAX_DATE = datetime.date(2022, 3, 17)

# Opening JSON file
f = open("data.json")
data = json.load(f)
store_one = Store(data["incidents"])
# Closing file
f.close()

print("------------# INICIANDO PROGRAMA #------------")
print("")
print("")
store_one.incident_status(MIN_DATE, MAX_DATE)
print("")
print("")


#store_one.print_result()

