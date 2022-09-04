## Criando classe genérica
## Sempre inicia com class e após o nome da Classe

class Veiculo:
    ## Atributos de classe
    modelo = 'X6'

    ## Métodos
    
    ## Construtor e atributos de objeto/instancia
    def __init__(self, cor, portas, ano):
        self.cor = cor
        self.portas = portas
        self.ano = ano  
        self.velocidade = 0  
    
    def acelerar(self, velocidade):
         print(f"Acelerou a {velocidade}")
    
    def frear(self):
        print("Freou")
    
    @classmethod
    def meteodo_de_classe(cls, parametro1, parametro2):
            print("Método de classe")
            
            
class Carro(Veiculo):
    
    ## Médoto construtor da classe herdeira
    def __init__(self, cor, portas, ano, modelo):
         super().__init__(cor, portas, ano)
         self.modelo = modelo
    
    def obterModelo(self):
        print(self.modelo)