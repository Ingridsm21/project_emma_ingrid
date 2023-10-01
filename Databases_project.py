from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Dialogue(Base):
    __tablename__ = "dialogue"

    id = Column("id", Integer, primary_key = True)
    npc_id = Column("npc_id",Integer )
    player_id = Column("player_id", Integer)
    text = Column("text", String )


def __init__(self,id,npc_id,player_id,text):
    self.id = id
    self.npc_id = npc_id
    self.player_id = player_id
    self.text = text

def __repr__(self):
    return f"({self.id}) {self.npc_id} ({self.player_id} {self.text})"