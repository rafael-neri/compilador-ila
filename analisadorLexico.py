import shlex
import sys
import re
import string

class analisadorLexico:

    # PALAVRAS RESERVADAS DO ILA
    reservadasILA = ("variaveis", "faca_enquanto", "funcao", "fim_enquanto", "retornar", "se", "entao",
                     "inicio", "senao", "posicionar", "fim_se", "limpar","numerico", "ler", "caracter", "outro_caso"
                     "escrever", "matriz", "faca caso", "para", "caso", "ate", "proximo", "fim_caso", "fim")

    # OPERADORES ARITIMETICOS
    operadoresAritimeticos = ("+", "-", "*", "/", "^")

    # OPERADORES RELACIONAIS
    operadoresRelacionais = (">", "<", "<>", ">=", "<=")

    # OPERADORES LOGICOS
    operadoresLogicos = ("e", "ou", "nao")
                         
    # EXPRESSOES ARITIMETICAS
    expressoesAritimeticas = ("(",")","[","]")
    
    # OUTRAS VARIAVEIS
    arquivo = None
    listaTS = []
    erros = []
    
    # CONSTRUTOR QUE RECEBE O ARQUIVO
    def __init__(self, arquivo):
        if self.arquivo == None:            
            self.arquivo = file(arquivo, 'rt')

    
    # RETORNA OS POSSIVEIS TOKENS DE UM ARQUIVO - PRIVADO    
    def gerarListaTS(self):           
        # LER O CONTEUDO DO ARQUIVO
        conteudoArquivo = string.split(self.arquivo.read(), '\n')   
        listaTokens = {}
        pos = 0
        
        #LISTA OS POSSIVEIS TOKENS
        for linha in conteudoArquivo:
            # OBTEM OS TOKENS DA LINHA
            tokensLinha = shlex.shlex(linha)
            #tokensLinha.commenters = '//'
            tokensLinha.quotes = "'",'"'
            tokensLinha.wordchars += '.=><:'
            
            pos+=1
                
            tokensLinha = list(tokensLinha)
            if tokensLinha != []:
                # VALIDAR OS TOKENS DA LINHA E INSERE EM LISTATOKENS        
                tokensValidados = self.__validaTokens__(tokensLinha)   
                listaTokens[pos] = tokensValidados
                
                # VERIFICA SE RETORNOU ERRO
                for elem in tokensValidados:
                    if elem[1] == 'desconhecido':
                        self.erros.append(str(elem[0]) + ': token desconhecido na linha ' + str(pos))
        
        
        self.listaTS = listaTokens
        return self.listaTS
    
    def __validaTokens__(self, tokensLinha): 
        
        regex = {
                 1: re.compile('[a-z0-9"\']+[=][a-z0-9"\']+', re.IGNORECASE),
                 2: re.compile('[a-z0-9"\']+[>][=][a-z0-9"\']+', re.IGNORECASE),
                 3: re.compile('[a-z0-9"\']+[<][=][a-z0-9"\']+', re.IGNORECASE)
        }

        caracter = {
                    1: "=",
                    2: ">=",
                    3: "<="
        }
        
        tokensValidados = []
        
        # QUEBRA AS ESTRUTURAS NAO IDENTIFICADAS NO SHLEX
        for token in tokensLinha:  
            # FLAG
            t = False
            chave = len(tokensValidados)
                     
            for indice, valor in regex.items():
                result = re.match(valor, token)    
                if result:
                    t = string.split(token, caracter[indice])                                        
                    tokensValidados.insert(chave+1, t[0])
                    tokensValidados.insert(chave+2, caracter[indice])
                    tokensValidados.insert(chave+3, t[1])
            
            if not t:
                tokensValidados.insert(chave+1, token)
                    
        tokensValidadosAnalisados = []

        for token in tokensValidados:
            tokenAnalisado = self.__analisaToken__(token)
            tokensValidadosAnalisados.insert(len(tokensValidadosAnalisados)+1, {0: token, 1: tokenAnalisado})
        
        return tokensValidadosAnalisados  
    
    #ANALISA UM TOKEN    
    def __analisaToken__(self, token):
         
        # 1) VERIFICA SE E PALAVRA RESERVADA
        if token in self.reservadasILA:
            return "Palavra Reservada"
        
        # 2) VERIFICA SE E OPERADOR MATEMATICO
        if token in self.operadoresAritimeticos:
            if token == "+":
                return "Operador de Adicao"
            if token == "-":
                return "Operador de Subtracao"
            if token == "*":
                return "Operador de Multiplicacao"
            if token == "/":
                return "Operador de Divisao"
            if token == "+":
                return "Operador de Potencia"
    
        # 3) OPERADORES RELACIONAIS
        if token in self.operadoresRelacionais:
            if token == ">":
                return "Maior que"
            if token == "<":
                return "Menor que"
            if token == "==":
                return "Igualdade"
            if token == "<>":
                return "Diferenciacao"
            if token == ">=":
                return "Maior ou igual que"
            if token == "<=":
                return "Menor ou igual que"
             
        # 4) OPERADORES LOGICOS
        if token in self.operadoresLogicos:
            if token == "e":
                return "Operador de Uniao"
            if token == "ou":
                return "Operador de disjuncao"
            if token == "nao":
                return "Operador de Negacao"
        
        # 5) EXPRESSOES ARITIMETICAS
        if token in self.expressoesAritimeticas:
            return "Expressoes Aritimeticas"
        
        # 6) SEPARADOR
        if token == ",":
            return "Separador"
        
        # 7) VERIFICA SE E IDENTIFICADOR
        regex = re.compile('^[a-z][_a-z0-9]*$', re.IGNORECASE)
        result = regex.match(token)
        if result:
            return "Identificador"
        
        # 8) VERIFICA STRINGS
        regex = re.compile('^["].*["]' + "|"+ "^['].*[']", re.IGNORECASE)
        result = regex.match(token)
        if result:
            return "Valor"
        
        # 9) VERIFICA SE E UM NUMERAL
        regex = re.compile('^[0-9]+|^[0-9][0-9]*[.][0-9][0-9]*', re.IGNORECASE)
        result = regex.match(token)
        if result:
            return "Numeral"
        
        # 10) VERIFICA SE E ATRIBUICAO
        if token == "=":
            return 'Atribuicao'
     
        return "desconhecido"
                
    # IMPRIME A TABELA DE SIMBOLOS 
    def imprimeTS(self):
        
        print "Tabela de Simbolos:"
        
        for i, linha in self.listaTS.items(): 
            for elem in linha:           
                #IMPRIME O TOKEN
                sys.stdout.write(elem[0])
                
                #IMPRIME ESPACOS
                i = 16 - len(elem[0])
                while i:
                    sys.stdout.write(" ")
                    i = i-1
                
                #IMPRIME O TIPO
                sys.stdout.write(elem[1])
    
                #IMPRIME A QUANTIDADE
                #sys.stdout.write("  ("+str(val[1])+"x)\n")
                sys.stdout.write("\n")
            
            
    # IMPRIME OS ERROS
    def mostrarErros(self):
        
        for i, linha in self.listaTS.items():
            delimitadores = {'(': 0, ')': 0}
            for elem in linha:
                if elem[0] == '(':
                    delimitadores['('] += 1
                if elem[0] == ')':
                    delimitadores[')'] += 1
            
            if delimitadores['('] > delimitadores[')']:
                self.erros.append('Faltando delimitador ) na linha '+str(i))
            if delimitadores['('] < delimitadores[')']:
                self.erros.append('Faltando delimitador ( na linha '+str(i))
            
        
        print "Erros:"
        if len(self.erros) > 0:
            for erro in self.erros:
                print erro
            return True
        else:
            print "Nenhum erro encontrado"
            return False