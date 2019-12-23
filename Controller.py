
import random, string
discipline_str = 'discipline'
classes_str = 'classes'
school_str = 'school'
teachers_str = 'teachers'
students_str = 'students'
teachers_discipline_str = 'teachers_discipline'
Empty_str = ''

tables_number = {1: discipline_str,
                     2: classes_str,
                     3: school_str,
                     4: teachers_str,
                     5: students_str,
                     6: teachers_discipline_str}

tables_columns = {classes_str: ["id", "name", "classroom","school"],
                      discipline_str: ["id", "name", "number_of_tests", "lessons_per_week" , "teachers"],
                      school_str: ["id", "name", "city", "type"],
                      teachers_str: ["id", "full_name", "number", "school", "classes"],
                      students_str: ["id", "full_name", "phone_number", "cities", "classes"],
                      teachers_discipline_str: ["id", "teachers", "discipline" ]}


class Controller:


    current_table = None
    action = None

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.start()

    def print_table(self, parameters):
        tables_print_function = {classes_str: self.view.print_classes,
                                 discipline_str:  self.view.print_discipline,
                                 school_str:   self.view.print_school,
                                 teachers_str: self.view.print_teachers,
                                 students_str: self.view.print_shop,
                                 teachers_discipline_str: self.view.print_worker}
        tables_print_function[self.current_table](parameters)

    def print_columns_titles(self, is_need_primary_key):
        columns = tables_columns[self.current_table]
        start_i = (0 if is_need_primary_key else 1)
        size = len(columns)
        for i in range(start_i, size):
            print("{number} for {column}".format(number=i, column=columns[i]))

    def start(self):
        while True:
            self.view.tables_menu()
            try:
                table = int(input())
                self.current_table = tables_number[table]
                self.view.action_menu()
                action_numbers = {1: self.select_action,
                                  2: self.insert_action,
                                  3: self.delete_action,
                                  4: self.update_action}
                self.action = int(input())
                action_numbers[self.action]()
            except Exception as e:
                print("Please write correct value ", e)
                continue

    def is_correct_parameters(self, parameters):
        current_used_fields = []
        size = len(tables_columns[self.current_table])
        for parameter in parameters:
            field_number = int(parameter[0])
            if int(field_number) not in range(-1, size) and len(parameter) != 3:
                return False
            else:
                for field in current_used_fields:
                    if field_number == field:
                        return False
                current_used_fields.append(field_number)
        return True

    def delete_action(self):
        print("Please write values by which you want to delete from table {table}. "
              "( format must be 1=value|2=value etc )".format(table=self.current_table))
        self.print_columns_titles(True)
        delete_parameters = []
        while True:
            string = input()
            result = string.split('|')
            is_error_data = False
            try:
                if self.is_correct_parameters(result):
                    for column in result:
                        insert_list = column.split('=')
                        delete_parameters.append([tables_columns[self.current_table][int(insert_list[0])],
                                                 insert_list[1]])
                else:
                    is_error_data = True
                    print("Incorrect value")
                status, result_db = self.model.delete_callback(self.current_table,
                                                               delete_parameters)
                print(status)
                if status == 'Ok':
                    break
            except:
                is_error_data = True
                print("Incorrect value")
            if not is_error_data:
                break

    def insert_action(self):
        print("Please write value which you want to insert into table {table}. "
              "( format must be 1=value|2=value etc ). Input order must be followed".format(table=self.current_table))
        self.print_columns_titles(True)
        while True:
            insert_parameters = []
            string = input()
            result = string.split('|')
            is_error_data = False
            try:
                if self.is_correct_parameters(result):
                    for column in result:
                        insert_list = column.split('=')
                        insert_parameters.append(insert_list[1])
                else:
                    is_error_data = True
                    print("Incorrect value")
                status, result_db = self.model.insert_callback(self.current_table,
                                                               insert_parameters,
                                                               tables_columns[self.current_table])
                print(status)
                if status == 'Ok':
                    break
            except:
                is_error_data = True
                print("Incorrect value")
            if not is_error_data:
                break

    def select_action(self):
        print("Please write value by which you want to select from table {table}. "
              "( format must be 1=value 2=value etc )"
              "\nPress Enter for select without parameters".format(table=self.current_table))
        self.print_columns_titles(True)
        select_parameters = []
        while True:
            string = input()
            result = string.split()
            is_error_data = False
            try:
                if self.is_correct_parameters(result):
                    for column in result:
                        insert_list = column.split('=')
                        select_parameters.append([tables_columns[self.current_table][int(insert_list[0])],
                                                 insert_list[1]])
                else:
                    is_error_data = True
                    print("Incorrect value")
            except:
                is_error_data = True
                print("Incorrect value")
            if not is_error_data:
                break
        status, result = self.model.select_callback(self.current_table, select_parameters)
        if status == "Ok":
            self.print_table(result)

    def update_action(self):
        print("Please write value which you want to update in table {table}. "
              "( format must be 1=value|2=value etc ) "
              "\nFirst parameter must be primary key( number 0 )".format(table=self.current_table))
        self.print_columns_titles(True)
        update_parameters = []
        while True:
            string = input()
            result = string.split('|')
            is_error_data = False
            try:
                if self.is_correct_parameters(result):
                    for column in result:
                        insert_list = column.split('=')
                        update_parameters.append([tables_columns[self.current_table][int(insert_list[0])],
                                                  insert_list[1]])
                else:
                    is_error_data = True
                    print("Incorrect value")
                status, result_db = self.model.update_callback(self.current_table,
                                                               update_parameters[0],
                                                               update_parameters[1::])
                print(status)
                if status == 'Ok':
                    break
            except:
                is_error_data = True
                print("Incorrect value")
            if not is_error_data:
                break