

class View(object):

    @staticmethod
    def tables_menu():
        print("Select table")
        print("1 - discipline")
        print("2 - classes")
        print("3 - school")
        print("4 - teachers")
        print("5 - students")
        print("6 - teachers_discipline")

    @staticmethod
    def action_menu():
        print("Select action")
        print("1 - Select")
        print("2 - Insert")
        print("3 - Delete")
        print("4 - Update")


    @staticmethod
    def print_discipline(parameters):
        print("id | name | number of tests | lessons per week | teachers ")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                id, name, numberOfTests,lessonsPerWeek,teachers = column.split(", ")
                print("\t\t", id, "\t  |\t\t", name, "\t\t |\t", numberOfTests,"\t\t |\t",lessonsPerWeek,"\t\t |\t",teachers)
        except:
            print("")

    @staticmethod
    def print_classes(parameters):
        print("id | name | classroom | school")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                id, name, classroom, school = column.split(", ")
                print("\t\t", id, "\t  |\t\t", name, "\t\t |\t", classroom,"\t  |\t\t",school)
        except:
            print("")

    @staticmethod
    def print_school(parameters):
        print("id | name | city | type")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                id, name, city, type = column.split(", ")
                print("\t\t", id, "\t  |\t\t", name, "\t\t |\t", city, "\t  |\t\t", type)
        except:
            print("")

    @staticmethod
    def print_teachers(parameters):
        print("id | full_name | number | school | classes")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                id, full_name, number , school ,classes = column.split(", ")
                print("\t\t", id, "\t  |\t\t", full_name, "\t\t |\t", number, "\t\t |\t",school , "\t\t |\t",classes)
        except:
            print("")

    @staticmethod
    def print_shop(parameters):
        print("shop_id | monthly_profit | address")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                shop_id, monthly_profit, address = column.split(", ")
                print("\t\t", shop_id, "\t  |\t\t", monthly_profit, "\t\t |\t", address)
        except:
            print("")

    @staticmethod
    def print_worker(parameters):
        print("worker_id | shop_id | name | surname | position")
        try:
            result = parameters.split('\n')
            for column in result:
                column = column[1:len(column) - 1]
                worker_id, shop_id, name, surname, position = column.split(", ")
                print("\t\t", worker_id, "\t  |\t\t", shop_id, "\t\t |\t", name, "\t\t |\t", surname, "\t\t |\t",position)
        except:
            print("")