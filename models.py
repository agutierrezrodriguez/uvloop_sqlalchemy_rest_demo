from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, \
    DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config

Base = declarative_base()


class Chef(Base):
    __tablename__ = 'Chefs'

    name = Column(String(100))
    email = Column(String(150), primary_key=True)

    def __repr__(self):
        return "<Chef(name='%s', email='%s')>" % (self.name, self.email)


class Student(Base):
    __tablename__ = 'Students'

    name = Column(String(100))
    surname = Column(String(150))
    zip = Column(String(10))
    country = Column(String(2))
    email = Column(String(150), primary_key=True)

    def __repr__(self):
        return "<Student(name='%s', surname='%s', email='%s')>" % (self.name,
                                                                   self.surname,
                                                                   self.email)


class Course(Base):
    __tablename__ = 'Courses'

    name = Column(String(100), primary_key=True)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    chef_id = Column(String(150), ForeignKey('Chefs.email'))
    chef = relationship(Chef)

    def __repr__(self):
        return "<Course(name='%s', start_date='%s', end_date='%s')>" % (
            self.name,
            self.start_date,
            self.end_date
        )


class Registration(Base):
    __tablename__ = 'Registrations'

    course_id = Column(String(100), ForeignKey('Courses.name'),
                       primary_key=True)
    student_id = Column(String(150), ForeignKey('Students.email'),
                        primary_key=True)
    register_date = Column(DateTime, default=datetime.utcnow())
    course = relationship(Course)
    student = relationship(Student)

    def __repr__(self):
        return "<Registration(course='%', student='%s', " \
               "register_date='%s')>" % (self.course, self.student,
                                         self.register_date)


if __name__ == "__main__":
    engine = create_engine(config.DB_ENGINE, echo=True)
    Base.metadata.create_all(engine)
