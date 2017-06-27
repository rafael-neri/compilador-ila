import re
import string
import sys

class analisadorSintatico:
    
    listaTSAux = {}
   
    # CONSTRUTOR
    def __init__(self, listaTS):
        #print 'ListaTS: ', listaTS
        
        for indice, item in listaTS.items():
            linha = ''
            for v in item:
                linha += v[0]
            self.listaTSAux[indice] = linha
                
        #print 'ListaAux: ', self.listaTSAux
            
        #regex = [re.compile('[a-zA-Z0-9]+[=][(0-9)]+([+-/*][0-9]+)*', re.IGNORECASE)]
        #regex = [re.compile('^[a-zA-Z]+[0-9]*[=][(]*[0-9a-zA-Z]+[)]*', re.IGNORECASE)]
        
        regex = re.compile('^[a-zA-Z]+[0-9]*[=](.)+', re.IGNORECASE)

        
        variaveis = {}
        
        for indice, item in self.listaTSAux.items():
            result = re.match(regex, item)
            
            #print indice, ': ', result
            
            if result != None:
                for elem in listaTS[indice]:
                    #print '\n\n', elem
                    if elem[1] == 'Identificador':
                        valor = string.split(item, '=')                     
                        
                        #print variaveis                  
                        for variavel, val in variaveis.items():
                            if variavel in valor[1]:
                                valor[1] = valor[1].replace(variavel, str(val))
                                
                        try:
                            variaveis[valor[0]] = eval(valor[1])
                        except:
                            print 'Erro inesperado na linha ', indice , elem
                            
        
        print variaveis