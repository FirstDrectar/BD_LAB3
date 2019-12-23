from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Discipline(Base):
    __tablename__ = 'discipline'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number_of_tests = Column(Integer)
    lessons_per_week= Column(Integer)
    teachers= Column(Integer)
    # def __repr__(self):
    #     return f'List: {self.name}'
    def get_item(self):
        return "{0},{1},{2},{3},{4}".format(self.id,
                                    self.name,
                                            self.number_of_tests,
                                            self.lessons_per_week,
                                    self.teachers)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'name':
            return self.name
        elif column_name == 'number_of_tests':
            return self.number_of_tests
        elif column_name == 'lessons_per_week':
            return self.lessons_per_week
        elif column_name == 'teachers':
            return self.teachers

    @staticmethod
    def create():
        return Discipline()

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    classroom = Column(String)
    name = Column(String)
    school = Column(Integer)


    def get_item(self):
        return "{0},{1},{2},{3}".format(self.id,
                                            self.classroom,
                                            self.name,
                                            self.school)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'classroom':
            return self.classroom
        elif column_name == 'name':
            return self.name
        elif column_name == 'school':
            return self.school

    @staticmethod
    def create():
        return Classes()


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    type = Column(String)

    def get_item(self):
        return "{0},{1},{2},{3}".format(self.id,
                                    self.name,
                                    self.city,
                                    self.type)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'name':
            return self.name
        elif column_name == 'city':
            return self.city
        elif column_name == 'type':
            return self.type

    @staticmethod
    def create():
        return School()


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    number = Column(String)
    classes = Column(Integer)
    school = Column(Integer)

    def get_item(self):
        return "{0},{1},{2},{3},{4}".format(self.id,
                                         self.full_name,
                                         self.classes,
                                         self.number,
                                         self.school)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'full_name':
            return self.full_name
        elif column_name == 'classes':
            return self.classes
        elif column_name == 'number':
            return self.number
        elif column_name == 'school':
            return self.school

    @staticmethod
    def create():
        return Teachers()


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone_number = Column(String)
    cities =Column(String)
    classes =Column(Integer)

    def get_item(self):
        return "{0},{1},{2}".format(self.id,
                                    self.full_name,
                                    self.phone_number,
                                    self.cities,
                                    self.classes)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'full_name':
            return self.full_name
        elif column_name == 'phone_number':
            return self.phone_number
        elif column_name == 'cities':
            return self.cities
        elif column_name == 'classes':
            return self.classes

    @staticmethod
    def create():
        return Students()


class Teachers_discipline(Base):
    __tablename__ = 'teachers_discipline'
    id = Column(Integer, primary_key=True)
    teachers = Column(Integer)
    discipline = Column(Integer)


    def get_item(self):
        return "{0},{1},{2}".format(self.id,
                                    self.teachers,
                                    self.discipline)

    def get_column(self, column_name):
        if column_name == "id":
            return self.id
        elif column_name == 'teachers':
            return self.teachers
        elif column_name == 'discipline':
            return self.discipline

    @staticmethod
    def create():
        return Teachers_discipline()


def get_column_object(table_object, name):
    return table_object.get_column(table_object, name)
