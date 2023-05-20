from lin import InfoCrud
from sqlalchemy import Column, Integer, String

class Prompt(InfoCrud):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(1000), nullable=False)
    scene = Column(String(100), default="normal")
    name = Column(String(100))
    role = Column(String(100))
    request = Column(String(1000))
    language = Column(String(100))