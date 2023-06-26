from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import *
from .constants import *


db = PostgresqlExtDatabase(
    DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = TextField()
    telefone = TextField()
    email = TextField()
    cidade = TextField()
    estado = TextField()

class Login(BaseModel):
    email = TextField()
    senha = TextField()

class Usuario(BaseModel):
    pessoa = ForeignKeyField(Pessoa)
    login = ForeignKeyField(Login)

class Cadastro(BaseModel):
    nome = TextField()
    email = TextField()
    telefone = TextField()
    senha = TextField()

class Publicacao(BaseModel):
    titulo = TextField()
    descricao = TextField()
    data_criacao = DateTimeField()
    usuario = ForeignKeyField(Usuario)
    animal = TextField()
    raca = TextField()
    cidade = TextField()
    bairro = TextField()

db.connect()
db.create_tables([Login, Pessoa, Usuario, Publicacao, Cadastro])