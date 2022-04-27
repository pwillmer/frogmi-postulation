# Documentación

## A continuación algunos puntos a considerar.

- Dentro de la carpeta data_creation se creó el script ``` parameters.py ``` con la finalidad de crear un archivo json para realizar tests y corroborar que el código funcione.
- Dentro de este script, se consideraron valores de parámetros para generar data al azar y guardarlas en ``` data.json```.
```
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
```
- Se creó una clase Store que contiene los siguientes métodos
```
def incident_status(self, first_date, second_date)
def n_open_cases(self, first_date, second_date)
def n_solved_cases(self, first_date, second_date)
def average_solution_time(self, first_date, second_date)
def current_max_solution(self, first_date, second_date)
def print_result(self)
```
- Ejemplo: El método incident_status de Store retorna lo siguiente
```
{
        'open_cases' : 4
        'closed_cases' : 5
        'average_solution' : 2 days, 19:12:00
        'maximum_solution' : 80 days, 22:29:53.655642
}
```

## Ejecución
- Para generar nueva data, correr ```python data_creation/parameters.py```
- Correr archivo main ```python main.py``` y obtener resultado
