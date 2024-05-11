def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return False
    
def abrir_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'r')
    except:
        print('Não foi possível abrir para leitura.')
    else:
        print(f'Arquivo {nome_arquivo} aberto com sucesso!\n')
        return a
    
def cria_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        ('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!\n')

def listar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else: # se deu certo
        dados = a.readlines()
    finally:
        a.close()
        return dados
    
def inserir_score(nome_arquivo, nome_jogador, score):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nome_jogador};{score}\n')
    finally:
        a.close()