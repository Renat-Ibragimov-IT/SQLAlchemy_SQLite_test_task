from sqlalchemy import Column, Table, ForeignKey, Integer, String, Time, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///simple_imdb.db')

movies_genres = Table("movies_genres", Base.metadata,
                      Column("movies_pk", ForeignKey("movies.pk"),
                             primary_key=True),
                      Column("genres_pk", ForeignKey("genres.pk"),
                             primary_key=True))

movies_actors = Table("movies_actors", Base.metadata,
                      Column("movies_pk", ForeignKey("movies.pk"),
                             primary_key=True),
                      Column("actors_pk", ForeignKey("actors.pk"),
                             primary_key=True))


class Movie(Base):
    __tablename__ = 'movies'
    pk = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    release_date = Column(Date, nullable=False)
    duration = Column(Time, nullable=False)
    genres = relationship("Genre", secondary="movies_genres", backref="movies")
    actors = relationship("Actor", secondary="movies_actors", backref="movies")


class Genre(Base):
    __tablename__ = 'genres'
    pk = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Actor(Base):
    __tablename__ = 'actors'
    pk = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    dob = Column(Date, nullable=False)


Base.metadata.create_all(engine)
