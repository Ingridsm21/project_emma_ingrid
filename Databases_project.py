from sqlalchemy import CheckConstraint, UniqueConstraint, create_engine, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random
import sys
#from server import exportData


# Emma and Ingrid
#      and i6314966

Base = declarative_base()

class Dialogue(Base):
    __tablename__ = "dialogue"

    id = Column("id", Integer, primary_key = True, autoincrement = True, server_default = "1")
    npc_id = Column("npc_id",Integer, ForeignKey("npc.id"))
    player_id = Column("player_id", Integer, ForeignKey("player.id"))
    text = Column("text", String )

    __table_args__ = (
        CheckConstraint('npc_id != player_id', name='check_npc_player_id'),
    )

    def __init__(self,id,npc_id,player_id,text):
        self.id = id
        self.npc_id = npc_id
        self.player_id = player_id
        self.text = text


class Guild(Base):
    __tablename__ = "guild"

    id = Column("id", Integer, primary_key = True, autoincrement = True, default = "1")
    name = Column("name",String, unique = True)
    leader_id = Column("leader_id", Integer, ForeignKey("player.id"),unique = True)
    founded_date = Column("founded_date", DateTime, nullable = True)
    members = Column("members", Integer )
    
    __table_args__ = (
            UniqueConstraint('name', name='uq_guild_name'),
        )

    def __init__(self,id,name,leader_id,founded_date,members):
        self.id = id
        self.name = name
        self.leader_id = leader_id
        self.founded_date = founded_date
        self.members = members
        


class Player(Base):
    __tablename__ = "player"

    id = Column("id", Integer, primary_key = True,autoincrement=True, server_default = "1")
    first_name = Column("first_name",String )
    last_name = Column("last_name", String)
    class_name = Column("class_name", String )
    guild_id = Column("guild_id", Integer, ForeignKey("guild.id"))
    item_id = Column("item_id", Integer)
    last_login = Column("last_login", DateTime)
    kingdom_id = Column("kingdom_id",Integer, ForeignKey("kingdom.id"))
    experience = Column("experience",Integer)
    health = Column("health",Integer)
    level = Column("level",Integer)
    gold = Column("gold",Integer)

    __table_args__ = (
       UniqueConstraint('first_name', 'last_name', name='uq_first_name_last_name'),
   )

    def __init__(self,id,first_name,last_name,class_name,guild_id,item_id,last_login,kingdom_id,experience,health,level,gold):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name
        self.guild_id = guild_id
        self.item_id = item_id
        self.last_login = last_login
        self.kingdom_id = kingdom_id
        self.experience = experience
        self.health = health
        self.level = level
        self.gold = gold


class Item(Base):
    __tablename__ = "item"

    id = Column("id", Integer, primary_key = True,autoincrement=True, server_default = "1")
    name = Column("name",String, unique = True)
    description = Column("description",String)
    price = Column("price",Integer)
    required_level = Column("required_level",Integer)

    def __init__(self,id,name,description,price,required_level):
        self.id = id
        self.name = name 
        self.description = description
        self.price = price
        self.required_level = required_level


class Enemy(Base):
    __tablename__ = "enemy"

    id = Column("id", Integer, primary_key = True,autoincrement=True, server_default = "1")
    name = Column("name",String,unique =True)
    type = Column("type",String)
    level = Column("level",Integer)
    health = Column("health",Integer)
    attack = Column("attack",Integer)
    defense = Column("defense",Integer)
    drop_items = Column("drop_items",Integer, ForeignKey("item.id"))

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

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String, unique = True)
    leader_id = Column("leader_id",Integer, ForeignKey("player.id"))
    member_count = Column("member_count",Integer)
    kingdom_id = Column("kingdom_id",Integer, ForeignKey("kingdom.id"))

    def __init__(self,id,name,leader_id,memeber_count,kingdom_id):
        self.id = id
        self.name = name 
        self.leader_id = leader_id
        self.member_count = memeber_count
        self.kingdom_id = kingdom_id


class Event(Base):
    __tablename__ = "event"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String, unique = True)
    event_date = Column("event_date", DateTime)

    __table_args__ = (
        UniqueConstraint('name', 'event_date'),  # Enforce unique name and event_date pairs
    )

    def __init__(self,id,name,event_date):
        self.id = id
        self.name = name 
        self.event_date = event_date



class NPC(Base):
    __tablename__ = "npc"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String)
    type = Column("type",String)
    location = Column("location",String)
    dialogue_id = Column("dialogue_id",String, ForeignKey("dialogue.id"))
    quest_id = Column("quest_id",Integer, ForeignKey("quest.id"))

    def __init__(self,id,name,type,location,dialogue_id,quest_id):
        self.id = id
        self.name = name 
        self.type = type
        self.location = location
        self.dialogue_id = dialogue_id
        self.quest_id = quest_id



class Kingdom(Base):
    __tablename__ = "kingdom"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String, unique=True)
    ruler_id = Column("ruler_id",Integer, ForeignKey("ruler.id"))
    population = Column("population",Integer)

    def __init__(self,id,name,ruler_id ,population):
        self.id = id
        self.name = name 
        self.ruler_id = ruler_id
        self.population = population



class Ruler(Base):
    __tablename__ = "ruler"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String)
    kingdom_id = Column("kingdom_id",Integer, ForeignKey("kingdom.id"), unique =True)

    def __init__(self,id,name,kingdom_id):
        self.id = id
        self.name = name 
        self.kingdom_id = kingdom_id



class Combat(Base):
    __tablename__ = "combat"

    id = Column("id", Integer, primary_key = True,autoincrement = True, server_default = "1")
    player_id = Column("player_id",Integer, ForeignKey("player.id"))
    enemy_id = Column("enemy_id",Integer, ForeignKey("player.id"))
    turns = Column("turns",Integer)
    winner_id = Column("winner_id",Integer)

    __table_args__ = (
        CheckConstraint("winner_id IN (player_id, enemy_id)"),
        UniqueConstraint('player_id', 'enemy_id'),  # Enforce unique player_id and enemy_id pairs
    )

    def __init__(self,id,player_id,enemy_id,turns,winner_id):
        self.id = id
        self.player_id = player_id
        self.enemy_id = enemy_id
        self.turns = turns
        self.winner_id = winner_id



class Transaction(Base):
    __tablename__ = "transaction"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    sender_id = Column("sender_id",Integer)
    receiver_id = Column("receiver_id",Integer)
    item_id = Column("item_id",Integer) 
    kingdom_id = Column("kingdom_id",Integer)
    amount = Column("amount",Integer)
    timestamp = Column("timestamp", DateTime, default = datetime.utcnow)

    __table_args__ = (
        CheckConstraint("sender_id != receiver_id"),  # Ensure sender_id is not equal to receiver_id
    )
    
    def __init__(self,id,sender_id,reciever_id,item_id,kingdom_id,amount,timestamp):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = reciever_id
        self.item_id = item_id
        self.kingdom_id = kingdom_id
        self.amount = amount
        self.timestamp = timestamp



class Quest(Base):
    __tablename__ = "quest"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String)
    reward = Column("reward",Integer)
    player_id = Column("player_id",Integer, ForeignKey("player.id"))
    difficulty = Column("difficulty",Integer)
    completition_time = Column("completition_time",Integer)


    def __init__(self,id,name,reward,player_id,difficulty,completition_time):
        self.id = id
        self.name = name
        self.reward = reward
        self.player_id = player_id
        self.difficulty = difficulty
        self.completition_time = completition_time


class Groupchat(Base):
    __tablename__ = "groupchat"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    name = Column("name",String)


    def __init__(self,id,name):
        self.id = id
        self.name = name

class Chat(Base):
    __tablename__ = "chat"

    id = Column("id", Integer, primary_key = True, autoincrement=True, server_default = "1")
    sender_id = Column("sender_id", Integer)
    name = Column("name", String)
    message = Column("message", String)


    def __init__(self,id,sender_id,name,message):
        self.id = id
        self.sender_id = sender_id
        self.name = name
        self.message = message

engine = create_engine("mysql://root:Techsoft21_@localhost:3306/project_mysticquest") #Cambiar
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()

file = open('generated_entities.txt')
Lines = file.readlines()
entities = ["player", "event", "item", "enemy", "team", "npc", "guild", "dialogue","kingdom","ruler","combat","transaction","quest","groupchat","chat"]
currentObj = []

def class_access(classname):
    return getattr(sys.modules[__name__], classname)


def objectcreation(currentObj):
    currentObj[0] = currentObj[0].replace('-', '').replace(' ', '').replace('\n', '')

    session.add(class_access(currentObj[0])(*currentObj[1:]))
    try:
        session.commit()
    except IntegrityError as err:
        session.rollback()
        return print('Duplicated value')
    return currentObj

for line in Lines:
    for entity in entities:
        if "---" in line:
            if len(currentObj) > 0:
                print(objectcreation(currentObj))  
            currentObj.clear()

    if not(line == '\n'):
        if len(currentObj) == 0:
            currentObj.append(line)
        else:
            
            cleaned = line.replace('\n', '').replace('"', '').split('=', 1)[1]
            if cleaned == "null":
                cleaned = None
            currentObj.append(cleaned)

table_classes = [Kingdom, Player, Item, Enemy, Team, NPC, Guild, Dialogue, Ruler, Combat, Transaction, Quest, Groupchat, Chat]

# Iterate through each table class and update the IDs
for table_class in table_classes:
    records = session.query(table_class).all()
    for i, record in enumerate(records):
        record.id = i + 1
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'kingdom_id'):
            record.kingdom_id = random.randint(1, 4)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'npc_id'):
            record.npc_id = random.randint(1, 72)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'player_id'):
            record.player_id = random.randint(1, 161)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'guild_id'):
            record.guild_id = random.randint(1, 36)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'item_id'):
            record.item_id = random.randint(1, 46)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'dialogue_id'):
            record.dialogue_id = random.randint(1, 197)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'quest_id'):
            record.quest_id = random.randint(1, 103)
    session.commit()

for table_class in table_classes:
    records = session.query(table_class).all()
    for record in records:
        if hasattr(record, 'ruler_id'):
            record.ruler_id = random.randint(1, 114)
    session.commit()

combat_entries = session.query(Combat).all()

for combat_entry in combat_entries:
    random_winner = random.choice([combat_entry.player_id, combat_entry.enemy_id])
    combat_entry.winner_id = random_winner

# Commit the updates
session.commit()


