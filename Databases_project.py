from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import sys


Base = declarative_base()

class Dialogue(Base):
    __tablename__ = "dialogue"

    id = Column("id", Integer, primary_key = True)
    npc_id = Column("npc_id",Integer)#,ForeignKey("npc.id"))
    player_id = Column("player_id", Integer)#,ForeignKey("player.id"))
    text = Column("text", String )

    def __init__(self,id,npc_id,player_id,text):
        self.id = id
        self.npc_id = npc_id
        self.player_id = player_id
        self.text = text


class Guild(Base):
    __tablename__ = "guild"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    leader_id = Column("leader_id", Integer)#,ForeignKey("player.id"))
    members = Column("members", Integer )
    founded_date = Column("founded_date", Integer)
    max_members = Column("max_members", Integer)
    


    def __init__(self,id,name,leader_id,members,founded_date,max_members):
        self.id = id
        self.name = name
        self.leader_id = leader_id
        self.members = members
        self.founded_date = founded_date
        self.max_members = max_members


class Player(Base):
    __tablename__ = "player"

    id = Column("id", Integer, primary_key = True)
    first_name = Column("first_name",String )
    last_name = Column("last_name", String)
    class_name = Column("class_name", String )
    guild_id = Column("guild_id", Integer)#,ForeignKey("guild.id"))
    last_login = Column("last_login", DateTime)
    kingdom_id = Column("kingdom_id",Integer)#,ForeignKey("kingdom.id"))
    experience = Column("experience",Integer)
    health = Column("health",Integer)
    level = Column("level",Integer)
    gold = Column("gold",Integer)


    def __init__(self,id,first_name,last_name,class_name,guild_id,last_login,kingdom_id,experience,health,level,gold):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name
        self.guild_id = guild_id
        self.last_login = last_login
        self.kingdom_id = kingdom_id
        self.experience = experience
        self.health = health
        self.level = level
        self.gold = gold


class Item(Base):
    __tablename__ = "item"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    description = Column("description",String)
    price = Column("price",Integer)
    required_level = Column("required_level",Integer)
    consumable = Column("consumable", Integer) 

    def __init__(self,id,name,description,price,required_level,consumable):
        self.id = id
        self.name = name 
        self.description = description
        self.price = price
        self.required_level = required_level
        self.consumable = consumable


class Enemy(Base):
    __tablename__ = "enemy"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    type = Column("type",String)
    level = Column("level",Integer)
    health = Column("health",Integer)
    attack = Column("attack",Integer)
    defense = Column("defense",Integer)
    drop_items = Column("drop_items",String)#,ForeignKey("item.id"))

    def __init__(self,id,name,type,level,health,attack,defense,drop_items):
        self.id = id
        self.name = name 
        self.type = type
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.drop_items = drop_items


class Team(Base):
    __tablename__ = "team"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    leader_id = Column("leader_id",Integer)#, ForeignKey("player.id"))
    member_count = Column("member_count",Integer)
    kingdom_id = Column("kingdom_id",Integer)#,ForeignKey("kingdom.id"))

    def __init__(self,id,name,leader_id,memeber_count,kingdom_id):
        self.id = id
        self.name = name 
        self.leader_id = leader_id
        self.member_count = memeber_count
        self.kingdom_id = kingdom_id


class Event(Base):
    __tablename__ = "event"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    description = Column("description",String)
    event_time = Column("event_time", DateTime)

    def __init__(self,id,name,description,event_time):
        self.id = id
        self.name = name 
        self.description = description
        self.event_time = event_time



class NPC(Base):
    __tablename__ = "npc"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    type = Column("type",String)
    location = Column("location",String)
    dialogue = Column("dialogue",String)#,ForeignKey("dialogue.id"))
    quest = Column("quest_id",Integer)#,ForeignKey("quest.id"))

    def __init__(self,id,name,type,location,dialogue,quest):
        self.id = id
        self.name = name 
        self.type = type
        self.location = location
        self.dialogue = dialogue
        self.quest = quest



class Kingdom(Base):
    __tablename__ = "kingdom"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    description = Column("description",String)
    ruler_id = Column("ruler_id",Integer)#,ForeignKey("ruler.id"))
    population = Column("population",Integer)

    def __init__(self,id,name,description,ruler_id,population):
        self.id = id
        self.name = name 
        self.description = description
        self.ruler_id = ruler_id
        self.population = population



class Ruler(Base):
    __tablename__ = "ruler"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    title = Column("title",String)
    kingdom_id = Column("kingdom_id",Integer)#,ForeignKey("kingdom.id"))

    def __init__(self,id,name,title,kingdom_id):
        self.id = id
        self.name = name 
        self.title = title
        self.kingdom_id = kingdom_id



class Combat(Base):
    __tablename__ = "combat"

    id = Column("id", Integer, primary_key = True)
    player_id = Column("player_id",Integer)#,ForeignKey("player.id"))
    enemy_id = Column("enemy_id",Integer)#,ForeignKey("player.id"))
    turns = Column("turns",Integer)
    winner_id = Column("winner_id",Integer)

    def __init__(self,id,player_id,enemy_id,turns,winner_id):
        self.id = id
        self.player_id = player_id
        self.enemy_id = enemy_id
        self.turns = turns
        self.winner_id = winner_id



class Transaction(Base):
    __tablename__ = "transaction"

    id = Column("id", Integer, primary_key = True)
    sender_id = Column("sender_id",Integer)
    receiver_id = Column("receiver_id",Integer)
    amount = Column("amount",Integer)
    description = Column("description",String)
    timestamp = Column("timestamp", DateTime, default = datetime.utcnow)

    def __init__(self,id,sender_id,reciever_id,amount,description,timestamp):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = reciever_id
        self.amount = amount
        self.description = description
        self.timestamp = timestamp



class Quest(Base):
    __tablename__ = "quest"

    id = Column("id", Integer, primary_key = True)
    name = Column("name",String)
    description = Column("description",String)
    reward = Column("reward",String)
    player_id = Column("player_id",Integer)#,ForeignKey("kingdom.id"))
    difficulty = Column("difficulty",Integer)


    def __init__(self,id,name,description,reward,player_id,difficulty):
        self.id = id
        self.name = name
        self.description = description
        self.reward = reward
        self.player_id = player_id
        self.difficulty = difficulty

engine = create_engine("mysql://root:Techsoft21_@localhost:3306/project_mysticquest") #Cambiar
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()

file = open('generated_entities.txt')
Lines = file.readlines()

entities = ["player", "event", "item", "enemy", "team", "npc", "guild", "dialogue","kingdom","ruler","combat","transaction","quest"]
currentObj = []

def class_access(classname):
    return getattr(sys.modules[__name__], classname)


def objectcreation(currentObj):
    currentObj[0] = currentObj[0].replace('-', '').replace(' ', '').replace('\n', '')
    if "questions" in currentObj[0]:
        currentObj[0] = "questions"
        print(currentObj)

    session.add(class_access(currentObj[0])(*currentObj[1:]))
    try:
        session.commit()
    except IntegrityError as err:
        session.rollback()
        return print('error')
    return currentObj

for line in Lines:
    print(line)
    for entity in entities:
        print(entity)
        print(currentObj)
        if "---" in line:
            if len(currentObj) > 0:
                print(objectcreation(currentObj))  
            currentObj.clear()

    if not(line == '\n'):
        if len(currentObj) == 0:
            currentObj.append(line)
        else:
            if 'null' in line:
                currentObj.append(line.replace('\n', '').replace('"', '').split('=', 1)[1])
                
            currentObj.append(line.replace('\n', '').replace('"', '').split('=', 1)[1])
    