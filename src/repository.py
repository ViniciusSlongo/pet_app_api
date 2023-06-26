from .models import *

class CadastroRepository:

    def post(self, body):
        if not body:
            return Exception   
        
        Cadastro().insert(body).execute()

class UsuarioRepository:

    def post(self, body):
        if not body:
            return Exception
        
        return Usuario().insert(body).execute()
    
    def get_by_login_id(self, id):

        if not id:
            return Exception

        return Usuario().select().where(Usuario.login == id).execute()

class PublicacaoRepository:

    def get_by_usuario_id(self, id):

        if not id:
            return Exception
        
        return Publicacao().select().where(Publicacao.usuario == id).execute()

    def get_all(self):
        return Publicacao().select().execute()

    def post(self, body):
        if not body:
            return Exception
        
        return Publicacao().insert(body).execute()

class PessoaRepository:

    def post(self, body):
        if not body:
            return Exception
        
        return Pessoa().insert(body).execute()
    
    def get_by_id(self,id):
        if not id:
            return Exception

        return Pessoa.select().where(Pessoa.id == id).execute()

class LoginRepository:

    def create_login(self, body):

        if not body:
            return Exception

        return Login().insert(body).execute()
    
    def login(self, body):

        if not body:
            return Exception
        query = Login.select().where(
                        (Login.email == body["email"]) &
                        (Login.senha == body["senha"])
        )
        return query.execute()