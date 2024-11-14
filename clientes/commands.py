from .models import Cliente, Carro
import re


class ProcessaUsuarios:
    def __init__(self, requisicao):
        self.requisicao_post = requisicao.POST
        self.nome = self.requisicao_post.get('nome')
        self.sobrenome = self.requisicao_post.get('sobrenome')
        self.email = self.requisicao_post.get('email')
        self.cpf = self.requisicao_post.get('cpf')
        self.carros = self.requisicao_post.getlist('carro')
        self.placas = self.requisicao_post.getlist('placa')
        self.anos = self.requisicao_post.getlist('ano')
        self.erro_msg = None
    
    
    def valida_dados(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        cpf_regex_pontos = r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$'
        cpf_regex_sem_pontos = r'^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$'
        
        if not re.match(cpf_regex_pontos, self.cpf) and not re.match(cpf_regex_sem_pontos, self.cpf):
            self.erro_msg = 'CPF inválido, reveja o formato'
            return False
            
        if Cliente.objects.filter(cpf=self.cpf).exists():
            self.erro_msg = 'CPF já cadastrado'
            return False
        
        if not re.match(email_regex, self.email):
            self.erro_msg = 'E-mail inválido, reveja o formato'
            return False
        
        if Cliente.objects.filter(email=self.email).exists():
            self.erro_msg = 'E-mail já cadastrado'
            return False
        
        return True
    
    
    def salva_cliente(self):
        self.cliente_bd = Cliente(
            nome=self.nome,
            sobrenome=self.sobrenome,
            email=self.email,
            cpf=self.cpf
        )
        self.cliente_bd.save()
    
    def salva_carro(self):
        relaciona_carros = list(zip(self.carros, self.placas, self.anos))
        for nome_carro, placa, ano in relaciona_carros:
            carro = Carro(
                carro=nome_carro,
                placa=placa,
                ano=ano,
                cliente=self.cliente_bd
            )
            carro.save()
