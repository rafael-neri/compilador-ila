import analisadorLexico
import analisadorSintatico


#c = list('AGHFDJCEIB')
#print c.index('D', 4)

al = analisadorLexico.analisadorLexico("projeto.ila")
listaTS = al.gerarListaTS()
al.imprimeTS()
print '\n\n'
erros = al.mostrarErros()

if not erros:
    print '\n'
    analisadorSintatico.analisadorSintatico(listaTS)