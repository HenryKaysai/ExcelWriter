import pandas as pd
import os
import datetime

#Verify if the number is suposed to be a string or a float, if it is not it converts itself into the other
def number_string_validation(typing, stop_typing=False):
    while True:
        crude_value = input(typing).strip()
        
        if stop_typing and crude_value.lower() == "stop":
            return "stop_sign"

        if crude_value == "":
            print("Error: the field can't be blank. Type something.")
        else:
            try:
                return float(crude_value)
            except ValueError:
                return crude_value

#Sets the maximum number of columns
print("--- Initial Configuration ---")
column_max = int(input("How many variables (columns) does your experiment have today? "))
column_names = []

#Asks for the name of each column
for j in range(column_max):
    name = number_string_validation(f"Type the name of the column {j + 1}:")
    column_names.append(name)
#Creates the data frame with one line: the names
data_frame = [column_names]
line_count = 1

print("\n--- Data Typing ---")
print("\n--- Type stop to end typing ---")
#Typing of each line
while True:
    line = []
    #flag to verify stop scenario
    stop_everything = False

    for j in range(column_max):
        value = number_string_validation(f"Column {column_names[j]}: ", stop_typing=True)
        
        #If the stop sign is verified, break the for loop
        if value == "stop_sign":
            print("-----> Ending data typing...")
            stop_everything = True
            break

        line.append(value)

    #If the stop sign was reached, the flag was raised, break for the while
    if stop_everything == True:
        break

    data_frame.append(line)
    line_count += 1

#Só para conferir se deu certo no final:
print("\n--- VERIFY YOUR SPREADSHEET! ---")

#Pega a lista inteira e joga dentro da variável 'linha'
for linha in data_frame:
    
    #Agora ele pega cada número de dentro da 'linha'
    for valor in linha:
        print(valor, end="\t")
        
    print() #Pula a linha

#Creating the pandas data frame =df
column_names = data_frame[0]
num_str_data = data_frame[1:]

df = pd.DataFrame(num_str_data, columns=column_names)
print("\n--- VERIFY YOUR PANDAS SPREADSHEET! ---")
print(df)

#Takes the date from your computer to use in the future
today_date = datetime.date.today().strftime("%d-%m-%Y")

#4. Ask the user to verify what he wishes to do with his data
while True:
    print("----->  What do you wish to do with your data?")
    print("----->  Type 1 to create a new archive")
    print("----->  Type 2 to create a new tab on an existing archive")
    print("----->  Type stop to abort")
        
    export_decision = (input(f"Your decision is: "))
    if export_decision.lower() == "stop":
        break

    #Creates a new file based on the name that has been given by the user
    if export_decision == "1":
        
        while True:
        
            print("-----> Saving parameters")
            print("-----> type 1 to create a .csv file")
            print("-----> Type 2 to create a .xlsx file")
            print("-----> Type back to go back to the menu")
            print("-----> Tip: just add the name, not the extension")

            
            save_format = input("What format would you wish to save (1 or 2): ")
            
            #Makes that anything it will return to the menu on both inputs
            if save_format.lower() == "back":
                file_name = "back"
                break

            if save_format not in ["1", "2"]:
                print("Type a valid option...")
                continue

            file_name = input(f"What is the name of your new archive? (Press Enter to use '{today_date}'): ").strip()

            if file_name == "":
                file_name = today_date

            if save_format == "1":
                file_name += ".csv"
                df.to_csv(file_name, index=False)
                break

            elif save_format == "2":
                file_name += ".xlsx"
                df.to_excel(file_name, index=False)
                break

        #Returns to the main menu
        if file_name.lower() == 'back':
            continue

        print(f"\nSucess! Archive '{file_name}' created on the same folder as your script.")
        break
        
    #Add a new tab to an existing archive (ONLY WORKS FOR .xlsx)
    elif export_decision == "2":
        while True:
            print("-----> Saving parameters")
            print("-----> Tip: only .xlsx files support multiple tabs.")
            
            file_name = input("What is the name of your existing Excel file? (or type 'back' to return) ")
            
            if file_name.lower() == 'back':
                break

            # Garante que é um Excel, pois CSV não tem abas
            if not file_name.endswith(".xlsx"):
                if file_name.endswith(".csv"):
                    print("Error: .csv files do not support tabs. Please choose a .xlsx file.")
                    continue
                else:
                    file_name += ".xlsx"

            if os.path.exists(file_name):
                print(f"File '{file_name}' found!")
                break
            else:
                print(f"Error: The file '{file_name}' does not exist in this folder. Try again.")

        if file_name.lower() == 'back':
            continue

        print("\nWARNING!!!!!")
        print("IF THE NAME YOU ARE CHOOSING IS EQUAL TO THE NAME OF ANOTHER TAB")
        print("THE PROGRAM WILL REPLACE IT")
        tab_name = input(f"What should be the name of the new tab? (Press Enter to use '{today_date}'): ").strip()

        if tab_name == "":
            tab_name = today_date
        
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=tab_name, index=False)
            
        print(f"\nSuccess! Tab '{tab_name}' added to '{file_name}'.")
        break
