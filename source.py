#Pede para o usuário quantas linhas ele quer na tabela
#print("Quantas linhas devemos definir hoje?")
#linhas_max = int(input())

#Pede para o usuário quantas colunas ele quer na tabela
print("--- Initial Configuration ---")
colunas_max = int(input("How many variables (columns) does your experiment have today? "))

#1. Definindo cabeçalho
nomes_colunas = []

for j in range(colunas_max):
    nome = input(f"Digite o nome da coluna {j + 1}:")
    nomes_colunas.append(nome)

#Definindo uma matriz para preencher os dados
data_frame = [nomes_colunas]

print("\n--- Data Typing ---")
print("Tip: Type 'stop' on the first field of a new line to stop data typing.\n")

contador_linhas = 1


#2. Loop infinito para as linhas
while True:
    linha_atual = []

    #Checa se o primeiro valor dalinha é o texto de parada
    primeiro_imput = input(f"Line {contador_linhas} - {nomes_colunas[0]}: ")

    if primeiro_imput.lower() == "stop":
        print("-----> Stopping data typing...")
        break

    #Se for um número armazena e continua
    linha_atual.append(float(primeiro_imput))

    #3. Loop normal para o resto das colunas daquela linha
    for j in range(1, colunas_max):
        valor = float(input(f"Line {contador_linhas} - {nomes_colunas[j]}: "))
        linha_atual.append(valor)

    #Salva a linha e aumenta o contadaor
    data_frame.append(linha_atual)
    contador_linhas += 1


#Só para conferir se deu certo no final:
print("\n--- VERIFY YOUR SPREADSHEET! ---")

#Pega a lista inteira e joga dentro da variável 'linha'
for linha in data_frame:
    
    #Agora ele pega cada número de dentro da 'linha'
    for valor in linha:
        print(valor, end="\t")
        
    print() #Pula a linha


import pandas as pd

nomes_colunas = data_frame[0]
dados_numericos = data_frame[1:]

df = pd.DataFrame(dados_numericos, columns=nomes_colunas)
print("\n--- VERIFY YOUR PANDAS SPREADSHEET! ---")
print(df)

nome_arquivo = "teste.xlsx"
df.to_excel(nome_arquivo, index=False)
print(f"\nSucess! Archive '{nome_arquivo}' created on the same folder as your script.")