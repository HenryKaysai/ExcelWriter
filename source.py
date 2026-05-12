import pandas as pd
import os

#Pede para o usuário quantas colunas ele quer na tabela
print("--- Initial Configuration ---")
colunas_max = int(input("How many variables (columns) does your experiment have today? "))

#1. Definindo cabeçalho
nomes_colunas = []

for j in range(colunas_max):
    nome = input(f"Type the name of the column {j + 1}:")
    nomes_colunas.append(nome)

#Definindo uma matriz para preencher os dados
data_frame = [nomes_colunas]

print("\n--- Data Typing ---")
print("Tip: Type 'stop' on the first field of a new line to stop data typing.\n")

contador_linhas = 1


#2. Loop infinito para as linhas
while True:
    linha_atual = []

    primeiro_imput = input(f"Line {contador_linhas} - {nomes_colunas[0]}: ")
    
    #Checa se o primeiro valor dalinha é o texto de parada
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

#Creating the pandas data frame =df
nomes_colunas = data_frame[0]
dados_numericos = data_frame[1:]

df = pd.DataFrame(dados_numericos, columns=nomes_colunas)
print("\n--- VERIFY YOUR PANDAS SPREADSHEET! ---")
print(df)


#4. Ask the user to verify what he wishes to do with his data
while True:
    print("----->  What do you wish to do with your data?")
    print("----->  Type 1 to create a new archive")
    print("----->  Type 2 to create a new tab on an existing archive")
    print("----->  Type stop to abort")
        
    export_decision = (input(f"Your decision is: "))
    if export_decision.lower() == "abort":
        break

    #Creates a new file based on the name that has been given by the user
    if export_decision == "1":
        file_name = (input("What is the name of your new archive?"))
        
        #If the file does not have the extension name adds it
        if not file_name.endswith(".xlsx"):
            file_name += ".xlsx"

        df.to_excel(file_name, index=False)
        print(f"\nSucess! Archive '{file_name}' created on the same folder as your script.")
        break
        

    #Add a new tab to an existing archive
    elif export_decision == "2":
        while True:
            file_name = input("\nWhat is the name of your existing file? (or type 'back' to return) ")
            
            #Goes back to the menu
            if file_name.lower() == 'back':
                break

            #If the file does not have the extension name adds it
            if not file_name.endswith(".xlsx"):
                file_name += ".xlsx"

            if os.path.exists(file_name):
                print(f"File {file_name} found!")
                break
            else:
                print(f"Error: The file '{file_name}' does not exist in this folder. Try again.")

        if file_name.lower() == 'back':
            continue


        #Ask the user the name of the new tab
        print("\nWARNING!!!!!")
        print("\nIF THE NAME YOU ARE CHOOSING IS EQUAL TO THE NAME OF ANOTHER TAB")
        print("\nTHE PROGRAM WILL REPLACE IT")
        tab_name = input("What should be the name of the new tab?")
        
        #Opens the file on the mode 'a' (append) using openpyxl
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            
            #Defines the data frame and sends it to 'writer'
            df.to_excel(writer, sheet_name=tab_name, index=False)
            
        print(f"\nSuccess! Tab '{tab_name}' added to '{file_name}'.")
        break
