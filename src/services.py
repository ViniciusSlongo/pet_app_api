from .repository import *
from loguru import logger
import datetime
import json

class Services:
    def __init__(self):
        self.publicacao_repository = PublicacaoRepository()
        self.cadastro_repository = CadastroRepository()
        self.usuario_repository = UsuarioRepository()
        self.pessoa_repository = PessoaRepository()
        self.login_repository = LoginRepository()

        self.payload = {
            "nome" : "",
            "telefone" : "",
            "email" : "",
            "senha" : "",
            "cidade" : "",
            "estado" : "",
        }

        self.payload_publicacao = {
            "titulo" : "",
            "descricao" : "",
            "data_criacao" : "",
            "animal" : "",
            "titulo" : "",
            "bairro" : "",
            "cidade" : "",
            "imagem" : ""
        }

    def __parse(self, body):
        try:
            self.payload["nome"] = body.get("nome")
            self.payload["telefone"] = body.get("telefone")
            self.payload["email"] = body.get("email")
            self.payload["senha"] = body.get("senha")
            self.payload["cidade"] = body.get("cidade")
            self.payload["estado"] = body.get("estado")
            return True
        
        except Exception as e:
            return False

    def __parse_publicacao(self, body):
        try:
            self.payload_publicacao["titulo"] = body.get("titulo")
            self.payload_publicacao["descricao"] = body.get("descricao")
            self.payload_publicacao["data_criacao"] = datetime.datetime.strptime(body.get("data_criacao"), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
            self.payload_publicacao["animal"] = body.get("animal")
            self.payload_publicacao["raca"] = body.get("raca")
            self.payload_publicacao["bairro"] = body.get("bairro")
            self.payload_publicacao["cidade"] = body.get("cidade")
            self.payload_publicacao["usuario"] = body.get("usuario")
            self.payload_publicacao["imagem"] = body.get("imagem")

            print(self.payload_publicacao)
            return True
        except Exception as e:
            return False


    @logger.catch
    def get_posts(self, id=None):
        if id:
            cursor = self.publicacao_repository.get_by_usuario_id(id)
        else:
            cursor = self.publicacao_repository.get_all()
        publicacoes = []
        for r in cursor:
            publicacoes.append(self.publicacao_to_dict(r))

        return publicacoes
    
    @logger.catch
    def login(self, body):
        cursor = self.login_repository.login(body)
        for r in cursor:
            return self.get_usuario_by_login_id(r)
            
    def get_usuario_by_login_id(self, id):
        cursor = self.usuario_repository.get_by_login_id(id)
        for r in cursor:
            return self.usuario_to_dict(r)

    def get_pessoa_by_id(self, id):
        cursor = self.pessoa_repository.get_by_id(id)
        for r in cursor:
            return r

    def create_publicacao(self, body):

        if self.__parse_publicacao(body):
            return self.publicacao_repository.post(self.payload_publicacao)

        return None

    def create_cadastro(self, body):

        if self.__parse(body):
            self.cadastro_repository.post({"nome": self.payload["nome"], "telefone": self.payload["telefone"], "email" : self.payload["email"], "senha" : self.payload["senha"]})
            pessoa_id = self.pessoa_repository.post({"nome": self.payload["nome"], "telefone": self.payload["telefone"], "email" : self.payload["email"], "cidade": self.payload["cidade"], "estado" : self.payload["estado"]} )
            login_id = self.login_repository.create_login({"email": self.payload["email"], "senha": self.payload["senha"]})

            return self.usuario_repository.post({"pessoa_id":pessoa_id, "login_id" : login_id})

    def pessoa_to_dict(self, row):
        return {
            "nome" : row.nome,
            "telefone" : row.telefone,
            "email" : row.email,
        }
    
    def usuario_to_dict(self, row):

        pessoa = self.get_pessoa_by_id(row)

        return {
            "usuario_id" : str(row.id),
            "nome" : pessoa.nome,
            "telefone" : pessoa.telefone,
            "email" : pessoa.email,
            "cidade" : pessoa.cidade,
            "estado" : pessoa.estado
        }

    def publicacao_to_dict(self, row):
        return {
            "titulo" : row.titulo,
            "descricao" : row.descricao,
            "data_criacao" : row.data_criacao.strftime("%Y-%m-%d %H:%M:%S"),
            "usuario" : row.usuario.id,
            "raca" : row.raca,
            "animal" : row.animal,
            "cidade" : row.cidade,
            "bairro" : row.bairro,
            "imagem" : row.imagem
        }