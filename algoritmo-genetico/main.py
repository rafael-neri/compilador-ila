import random
import base64


""""" INICIO DA CLASSE """""

class algoritmoGenetico:

    cidades = []
    tamanhoPopulacao = None
    populacao = [] 
    populacao2 = []
    flag = True
    
    def __init__(self, parametros):
        self.cidades, self.tamanhoPopulacao = parametros
        
        # flag que determina se e possivel operar com a qtdPopulacao informada
        if (self.tamanhoPopulacao/2)%2 != 0:
            self.flag = False        
        
    # geracao da populacao randomicamente    
    def gerarPopulacao(self):
        while len(self.populacao) != self.tamanhoPopulacao:
            cromossomo = []
            cromossomo.append(self.cidades[0])
            while len(cromossomo) != len(self.cidades):
                elem = random.choice(self.cidades)
                if elem not in cromossomo:
                    cromossomo.append(elem)
            
            cromossomo = ''.join(cromossomo)
            if cromossomo not in self.populacao:        
                self.populacao.append([cromossomo, random.randint(50, 5000)])
                
    # metade da popilacao e escolhida randomicamente          
    def escolha(self):
        while len(self.populacao2) < len(self.populacao)/2:
            #inserir individuo na populacao2
            self.populacao2.append(random.choice(self.populacao))
            
    
    # escolhe 4 individuos, seleciona os 2 melhores pelo fitness e gera 2 filhos
    def cruzar(self):
        filho1 = {}
        filho2 = {}
        print '\nLog de cruzamentos:'
        while len(self.populacao2) < len(self.populacao):
            # escolhe os 4 pais
            pai1 = random.choice(self.populacao)
            pai2 = random.choice(self.populacao)
            pai3 = random.choice(self.populacao)
            pai4 = random.choice(self.populacao)
            
            print 'pais escolhidos randomicamente: ', pai1, pai2, pai3, pai4
            
            # seleciona os 2 melhores pais
            if pai1[1] > pai2[1]:
                paiSelecionado1 = pai1
            else:
                paiSelecionado1 = pai2
                
            if pai3[1] > pai4[1]:
                paiSelecionado2 = pai3
            else:
                paiSelecionado2 = pai4
                
            print 'pais selecionados pelo fitness: ', paiSelecionado1, paiSelecionado2

            # cruza para gerar 2 filhos
            for i in range(len(self.cidades)/2):
                filho1[i] = paiSelecionado1[0][i]
                filho2[i] = paiSelecionado2[0][i]
                
                filho1[len(self.cidades)-i-1] = paiSelecionado2[0][len(self.cidades)-i-1]
                filho2[len(self.cidades)-i-1] = paiSelecionado1[0][len(self.cidades)-i-1]
            
            # verifica se os filhos sao validos e adiciona na popilacao2
            if(self.individuoEValido(filho1, filho2)):
                self.populacao2.append([''.join(filho1.values()), random.randint(50, 5000)])
                self.populacao2.append([''.join(filho2.values()), random.randint(50, 5000)])
                print 'filhos gerados pelo cruzamento: ', [''.join(filho1.values()), random.randint(50, 5000)], [''.join(filho2.values()), random.randint(50, 5000)], '\n'
            
            
            
    # metodo para verificar se os filhos sao validos 
    def individuoEValido(self, individuo1, individuo2):
        casos1 = []
        casos2 = []
        
        for i in individuo1.items():
            if i not in casos1:
                casos1.append(i)
            else:
                return False
            
        for i in individuo2.items():
            if i not in casos2:
                casos2.append(i)
            else:
                return False
            
        return True
            
    # verbose mode: mostra os detalhes dos atributos do algoritmo genetico  
    def mostrarDetalhes(self):
        print '\nCidades: ', self.cidades, '\nTamanho da populacao: ', self.tamanhoPopulacao
        print '\nPopulacao Inicial', self.populacao
        print 'Populacao Final', self.populacao2

        
""""" FINAL DA CLASSE """""






""""" MAIN """""

if __name__ == '__main__':
    
    listaCidades = ['A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z']

    #Escolhe quantidade de cidades
    #cidades = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    qtdCidades = input("Com quantas cidades deseja operar? ")
    cidades = []
    for i in range(0,qtdCidades):
        cidades.append(listaCidades[i])

    #Escolhe a quantidade da populacao
    #populacao = 4
    qtdPopulacao = input("Qual deve ser o tamanho da populacao? ")

    ag = algoritmoGenetico([cidades, qtdPopulacao])  
    if ag.flag:  
        ag.gerarPopulacao()        
        ag.escolha()
        ag.cruzar()    
        ag.mostrarDetalhes()
    else:
        print '\n\nNao e possivel operar com uma populacao de tamanho ', qtdPopulacao
        print base64.decodestring('UGFyYSBtYWlvcmVzIGluZm9ybWFjb2VzIGxpZ3VlIHBhcmEgMDgwMC02MTYxNjE=')
    