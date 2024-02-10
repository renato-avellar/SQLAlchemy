from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:jones666@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Filmes(Base):
    __tablename__ = 'filmes'
    
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f'Filme [titulo = {self.titulo}, ano = {self.ano}]'
    
#INSERT
#data_insert = Filmes(titulo="teste", genero='teste', ano = 2024)
#session.add(data_insert)
#session.commit()

#DELETE
session.query(Filmes).filter(Filmes.titulo == "teste").delete()
session.commit()

#UPDATE
session.query(Filmes).filter(Filmes.genero == "Drama").update({ "ano" : 2000})
session.commit()

#SELECT
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

