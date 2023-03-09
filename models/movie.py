from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

# Hereda de Base para indicarle que va a ser una entidad
class Movie(Base):
    __tablename__ =  'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    overview = Column(String(999))
    category = Column(String(100))
    year = Column(Date)
    disabled = Column(Boolean)
