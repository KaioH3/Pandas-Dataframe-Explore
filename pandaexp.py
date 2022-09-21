'''
License:GPL 3.0
'''
def escolher_df(dados):
    global dataframe
    global categoricas
    dataframe = dados
    categoricas = dataframe.select_dtypes(include=['object']).columns
    try: import pandas as pd
    except: print('Você não importou a biblioteca Pandas como "pd" ou não importou a biblioteca "pandas", mas tudo já foi resolvido.')
        
def inicio_fim(opcao):
    hifen = '-'
    if opcao == 1:
        print(hifen*28, "INICIO", hifen*28) # "hifen*28" imprime 28 "hifen"  
        
    if opcao == 2:
        print(hifen*56, "FIM", hifen*56, "\n\n\n")
    
def inicio_fim_print(frase, funcao):
    inicio_fim(1)
    print(frase)
    print(funcao) # para vermos quantas linhas e colunas o dataframe tem
    inicio_fim(2)
    
    # uso: inicio_fim_print("Informações dos dados:", dataframe.info(max_cols=numero_de_colunas)) ficaria assim:
    # inicio_fim(1)
    # print("Informações dos dados:")
    # print(dataframe.info(max_cols=numero_de_colunas))
    # inicio_fim(2)
    
def explorar(linhas=5, numero_de_colunas=None, mostrar_amostra='nao'):
    if mostrar_amostra.lower() == 'sim' or mostrar_amostra.lower() == 's':
        dataframe.sample(linhas)
        
    inicio_fim_print("Formato dos dados:", dataframe.shape)
    
    # Para vermos as 5 ou mais linhas iniciais e ter uma noção da estrutura dos dados
    inicio_fim_print("Head:", dataframe.head(linhas))
    
    # Para vermos as ultimas 5 ou mais linhas e ter uma noção da estrutura dos dados
    inicio_fim_print("Tail:", dataframe.tail(linhas))
    
    inicio_fim_print("Nome de todas as colunas:", dataframe.columns)    

    inicio_fim_print("Informações dos dados:", dataframe.info(max_cols=numero_de_colunas))    

    inicio_fim_print("Informações estatisticas:", dataframe.describe())
    
def col_categ(mostra_categoricas=True):
    if mostra_categoricas == True:
        print("Colunas categoricas:")
        print(categoricas, "\n")
        
        for i in categoricas:
            print("|Coluna categorica quantidade: {}".format(i),"|")
            print((dataframe[i]).value_counts(), "\n")
    
def preenche_nan(opcao_nan='outro', valor=-1):
    if opcao_nan == 1:
        dataframe.fillna(value=valor, inplace=True)
                    
def label_unica(unicos_lista=[]):
    pergunta = input("Tem certeza que quer mostrar todos os nomes e quantidade das labels das colunas categoricas deste dataframe?(s)im ou (n)ao: \n")
    if pergunta.lower() == 'sim' or pergunta.lower() == 's':
        for i in range(len(categoricas)):
            print("|Label da Coluna categorica: {}".format(categoricas[i]),"|")
            print(dataframe[categoricas[i]].unique(),"\n")
            
    else:
        pergunta2 = input("quer ler alguma lista de classes?(Passe as informações no formato de lista para unicos_lista)\n")
        if pergunta2.lower() == 'sim' or pergunta2.lower() == 's':
            for i in range(len(unicos_lista)):
                print("|Label da Coluna categorica: {}".format(unicos_lista[i]),"|")
                print(dataframe[unicos_lista[i]].unique(),"\n")
                               
def labels_frequentes(inicia_lf = 1, opcao_lf='c', linhas_lf=5):
    if inicia_lf == 1:
        if opcao_lf.lower() == 'crescente' or opcao_lf.lower() == 'c':
            for i in categoricas:
                print("|Categorias mais frequentes: {}".format(i),"|")
                print(dataframe[i].value_counts(ascending=True).head(linhas_lf), "\n")

        elif opcao_lf.lower() == 'decrescente' or opcao_lf.lower() == 'd':
            for i in categoricas:
                print("|Categorias mais frequentes: {}".format(i),"|")
                print(dataframe[i].value_counts(ascending=False).head(linhas_lf), "\n")
        
def tudo(dados1, **kwargs):
    # como "kwargs" é um dicionario, usamos para resgatar os valores do mesmo .get(objeto a ser resgatado, valor padrão se o objeto não for encontrado)
    
    linhas, numero_de_colunas, mostrar_amostra = kwargs.get('linhas', 5), kwargs.get('numero_de_colunas', None), kwargs.get('mostrar_amostra', 'nao')
    unicos_lista, mostra_categoricas = kwargs.get('unicos_lista', []), kwargs.get('mostra_categoricas', False)
    opcao_nan, valor = kwargs.get('opcao_nan', 'nao iniciar'), kwargs.get('valor', -1)
    inicia_lf, opcao_lf, linhas_lf = kwargs.get('inicia_lf', 'nao iniciar'), kwargs.get('opcao_lf', 'c'), kwargs.get('linhas_lf', 5)
    
    escolher_df(dados1)
    explorar(linhas, numero_de_colunas, mostrar_amostra)
    label_unica(unicos_lista)
    col_categ(mostra_categoricas)
    preenche_nan(opcao_nan, valor)
    labels_frequentes(inicia_lf, opcao_lf, linhas_lf)

    
    


# import sys 
# sys.path --> para ver em quais pastas o python busca as bibliotecas

# dir(funcaoDEG) para ver quais funcoes esta biblioteca tem

# para instalar a função colocar esse arquivo na pasta Anaconda3/Lib/site-packages/ ou, para acessar localmente, coloque na pasta do arquivo que será executado
