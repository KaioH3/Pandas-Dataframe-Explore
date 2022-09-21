# Pandas-Dataframe-Explore
Um plugin simples para a exploração de dataframes geradas pelas funções da biblioteca Pandas.


Para instalar globalmente no sistema operacional Windows,
coloque o arquivo "pandaexp.py" na pasta site-packages:  
"C:\Users\USERNAME\AppData\Roaming\Python\PythonVERSAO\site-packages\setup.py" e importe com: "import pandaexp".  
Exemplo: "C:\Users\Joazinho\AppData\Roaming\Python\Python39\site-packages"


Ou, para instalar no ambiente do anaconda no sistema operacional windows,  
coloque o arquivo "pandaexp.py" na pasta site-packages do Anaconda: "C:\Users\USERNAME\anaconda3\Lib\site-packages"  
Exemplo: "C:\Users\Joazinho\AppData\Roaming\Python\Python39\site-packages"


Para usar localmente,  
coloque o "pandaexp.py" na mesma pasta do arquivo onde irá executar o dataframe e importe o plugin normalmente.    

Funções:  
"escolher_df(dados)": escolhe o dataframe e disponibiliza globalmente as variáveis "dataframe" e "categoricas", que é a função que armazena as colunas que só possuem variáveis categóricas.  

"inicio_fim(opcao)": imprime na tela uma sequência de caracteres com a finalidade de manter uma formatação mais graciosa.    

"inicio_fim_print(frase, funcao)": imprime uma função já formatada com a função "inicio_fim" e com a frase escolhida.  

"explorar(linhas=5, numero_de_colunas=None, mostrar_amostra='nao')": explora o dataframe, demonstrando o formato em que os dados estão, o head e o tail do dataframe, o nome das colunas, informações gerais das colunas e informações estatísticas.  

"col_categ(mostra_categoricas=True)": mostra as colunas categóricas.  

"preenche_nan(opcao_nan='outro', valor=-1)": preenche valores NaN(Not a Number), com o valor -1 definido como padrão.  

"label_unica(unicos_lista=[])": mostra as labels que cada coluna categórica possui.  

"labels_frequentes(inicia_lf = 1, opcao_lf='c', linhas_lf=5)": mostra as labels mais frequentes.  

"tudo(dados1, **kwargs)": une todas as funções permitindo escolher que algumas funções sejam suprimidas ou ativadas, conforme a necessidade.  
