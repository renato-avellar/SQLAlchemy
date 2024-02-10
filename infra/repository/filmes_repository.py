from sqlalchemy.orm.exc import NoResultFound
from infra.entities.filmes import Filmes


class FilmesRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler
    
    def select(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_drama_filmes(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.genero == "ablue").one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, titulo, genero, ano):
        with self.__ConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo = titulo, genero = genero, ano = ano)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def delete(self, titulo):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def update(self, titulo, ano):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update({ "ano" : 2000})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception