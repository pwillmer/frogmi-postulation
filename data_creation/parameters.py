import datetime
from secrets import choice
import random
import datetime
import json

N_DATOS = 15

INCIDENTS_NAME = [
    "Robo en el piso 1",
    "Una mujer se cae, necesita asistencia medica",
    "El piso en el area de frutas esta sucio",
    "Hay falta de stock en el pasillo 4",
]

DATE = {
    "MIN": datetime.date(2022, 1, 1), 
    "MAX": datetime.date(2022, 4, 30)
}

STATE = [
    "OPEN",
    "SOLVED"
]

diccionario = dict()
list_incidents = []



#función para crear data
for i in range(N_DATOS):
    # Random name
    name = choice(INCIDENTS_NAME)
    
    # Random date
    time_between_dates = DATE["MAX"] - DATE["MIN"]
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date_start = DATE["MIN"] + datetime.timedelta(days=random_number_of_days)
    
    # Random status
    status = choice(STATE)
    if status == "SOLVED":
        random_date_end = random_date_start + datetime.timedelta(days=random.randint(0,5))
        random_date_end = '{}/{}/{}'.format(random_date_end.day, random_date_end.month, random_date_end.year)
    else:
        random_date_end = None
    
    # print(random_date_start, random_date_end)

    incidente = {
        "name": name,
        "first_date": '{}/{}/{}'.format(random_date_start.day, random_date_start.month, random_date_start.year),
        "second_date": random_date_end,
        "status": status
    }

    list_incidents.append(incidente)

diccionario["incidents"] = list_incidents

# print(diccionario)
jsonString = json.dumps(diccionario)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


     
