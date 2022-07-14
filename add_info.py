from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_database import Base, Movie, Genre, Actor
from datetime import date, time

engine = create_engine('sqlite:///simple_imdb.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
entries = [
    Movie(name='Insidious', release_date=date(2010, 9, 14),
          duration=time(1, 46)),
    Movie(name='Insidious: Chapter 2', release_date=date(2013, 9, 13),
          duration=time(1, 46)),
    Movie(name='Insidious: Chapter 3', release_date=date(2015, 5, 28),
          duration=time(1, 37)),
    Movie(name='Insidious: The Last Key',
          release_date=date(2018, 1, 3), duration=time(1, 43)),
    Genre(name='Horror'),
    Genre(name='Mystery'),
    Genre(name='Thriller'),
    Actor(name='Patrick Wilson', dob=date(1973, 7, 3)),
    Actor(name='Rose Byrne', dob=date(1979, 7, 24)),
    Actor(name='Ty Simpkins', dob=date(2001, 8, 6)),
    Actor(name='Lin Shaye', dob=date(1943, 10, 12)),
    Actor(name='Leigh Whannell', dob=date(1977, 1, 17)),
    Actor(name='Angus Sampson', dob=date(1979, 2, 12)),
    Actor(name='Barbara Hershey', dob=date(1948, 2, 5)),
    Actor(name='Andrew Astor', dob=date(2000, 6, 7)),
    Actor(name='Corbett Tuck', dob=date(1977, 3, 4)),
    Actor(name='Steve Coulter', dob=date(1960, 1, 1)),
    Actor(name='Hank Harris', dob=date(1979, 11, 5)),
    Actor(name='Jocelin Donahue', dob=date(1981, 11, 8)),
    Actor(name='Lindsay Seim', dob=date(1990, 5, 28)),
    Actor(name='Dermot Mulroney', dob=date(1963, 10, 31)),
    Actor(name='Stefanie Scott', dob=date(1996, 12, 6)),
    Actor(name='Tate Berney', dob=date(2003, 5, 17)),
    Actor(name='Michael Reid MacKay', dob=date(1953, 6, 24)),
    Actor(name='Hayley Kiyoko', dob=date(1991, 4, 3)),
    Actor(name='Tom Fitzpatrick', dob=date(1941, 9, 23)),
    Actor(name='Kirk Acevedo', dob=date(1971, 11, 27)),
    Actor(name='Caitlin Gerard', dob=date(1988, 7, 26)),
    Actor(name='Spencer Locke', dob=date(1991, 9, 20)),
    Actor(name='Josh Stewart', dob=date(1977, 2, 6)),
    Actor(name='Tessa Ferrer', dob=date(1986, 3, 30))]

session.bulk_save_objects(entries)
session.commit()

