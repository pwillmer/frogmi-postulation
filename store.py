from datetime import timedelta
from datetime import datetime
from datetime import date


class Store:
    def __init__(self, incident_list):
        self.incident_list = incident_list
        self.incident_status_value = {}

    def incident_status(self, first_date, second_date):
        #N° de casos abiertos
        open_cases = self.n_open_cases(first_date, second_date)
        solved_cases = self.n_solved_cases(first_date, second_date)
        average_sol_time = self.average_solution_time(first_date, second_date)
        current_max_sol = self.current_max_solution(first_date, second_date)

        result = {
            "open_cases": open_cases,
            "closed_cases": solved_cases,
            "average_solution": average_sol_time,
            "maximum_solution": current_max_sol
        }
        
        self.incident_status_value = result
        self.print_result()
        
    def n_open_cases(self, first_date, second_date):
        print("\t### N° OPEN CASES")
        count_n_cases = 0
        for incident in self.incident_list:
            date_json = datetime.strptime(incident["first_date"], '%d/%m/%Y')            
            if incident['status'] == 'OPEN':
                if date_json.date() > first_date and date_json.date() < second_date: 
                    print(first_date, date_json.date(), second_date)
                    count_n_cases += 1
        return count_n_cases

    def n_solved_cases(self, first_date, second_date):
        print("\t### N° SOLVED CASES")
        count_n_cases = 0
        for incident in self.incident_list:
            date_json = datetime.strptime(incident["first_date"], '%d/%m/%Y')            
            if incident['status'] == 'SOLVED':
                if date_json.date() > first_date and date_json.date() < second_date: 
                    print(first_date, date_json.date(), second_date)
                    count_n_cases += 1
        return count_n_cases

    def average_solution_time(self, first_date, second_date):
        print("\t### MEDIA SOLUTION TIME")
        count_n_cases = 0
        count_n_time = timedelta(hours=0)
        #print(count_n_time)
        for incident in self.incident_list:
            if incident['status'] == 'SOLVED':
                date_json_open = datetime.strptime(incident["first_date"], '%d/%m/%Y')            
                date_json_solved = datetime.strptime(incident["second_date"], '%d/%m/%Y')            
                if first_date < date_json_open.date() and date_json_solved.date() < second_date:
                    print(f'{first_date} < {date_json_open.date()} AND {date_json_solved.date()} <{second_date}')
                    count_n_time += date_json_solved.date()-date_json_open.date()
                    count_n_cases += 1
        if count_n_cases == 0:
            return 0
        else:
            calculo = count_n_time/count_n_cases
            return calculo

    def current_max_solution(self, first_date, second_date):
        print("\t### MAX SOLUTION TIME")
        count_n_time = timedelta(hours=0)
        for incident in self.incident_list:
            if incident['status'] == 'OPEN':
                date_json_open = datetime.strptime(incident["first_date"], '%d/%m/%Y')     
                date_now = datetime.now()
                if date_json_open.date() > first_date and date_json_open.date() < second_date: 
                    print(date_json_open, date_now)       
                    if ((date_now - date_json_open) > count_n_time):
                        count_n_time = date_now - date_json_open
        return count_n_time

    def print_result(self):
        print("------------# TERMINANDO PROGRAMA #------------")
        print("{")
        print(f"\t'open_cases' : {self.incident_status_value['open_cases']}")
        print(f"\t'closed_cases' : {self.incident_status_value['closed_cases']}")
        print(f"\t'average_solution' : {self.incident_status_value['average_solution']}")
        print(f"\t'maximum_solution' : {self.incident_status_value['maximum_solution']}")
        print("}")