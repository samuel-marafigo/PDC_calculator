# Importar bibliotecas necessárias
import csv
from collections import defaultdict
from datetime import datetime, timedelta

# Definir função para calcular o PDC
def calculate_PDC(filename):
    # Abrir o arquivo CSV
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        # Ler o arquivo CSV e transformar as informações em um dicionário
        reader = csv.DictReader(file, delimiter=';')
        user_medication = defaultdict(list)
        for row in reader:
            user_id = row['Usuário']
            date = datetime.strptime(row['Data da Saída'], '%d/%m/%Y').date()
            quantity = float(row['Quantidade'].replace(',', ''))
            user_medication[user_id].append((date, quantity))

    # Selecionar apenas os usuários com pelo menos 3 dispensações de medicamentos
    valid_users = [user_id for user_id, dispensing_data in user_medication.items() if len(dispensing_data) > 2]

    # Calcular o PDC para cada usuário válido
    PDC = {}
    for user in valid_users:
        dispensing_data = user_medication[user]
        dispensing_data.sort(key=lambda x: x[0])
        start_date = dispensing_data[0][0]
        if start_date > datetime(2022, 6, 30).date():
            continue
        end_date = datetime(2022, 12, 31).date()  # sempre usar 31 de dezembro de 2022 como data final
        covered_days = 0
        current_date = start_date
        current_quantity = 0
        surplus = 0
        for dispensing in dispensing_data:
            # Se a quantidade dispensada for 0, passar para a próxima dispensação
            if dispensing[1] == 0:
                continue
            # Se não houver quantidade atualmente em estoque, atualizar a data atual
            if current_quantity == 0:
                current_date = dispensing[0]
            # Cobrir dias a partir da data atual até a data da próxima dispensação
            while current_quantity < dispensing[1]:
                current_quantity += 1
                if current_date > end_date:
                    break
                if current_quantity > dispensing[1]:
                    surplus = current_quantity - dispensing[1]
                    current_quantity = dispensing[1]
                covered_days += 1
                current_date += timedelta(days=1)
            # Remover a quantidade dispensada da quantidade atual em estoque
            current_quantity -= dispensing[1]
            # Se houver sobra, atualizar a quantidade atual em estoque e remover a sobra
            if surplus > 0:
                current_quantity = surplus
                surplus = 0
            # Se a data atual passar da data final, parar o loop
            if current_date > end_date:
                break

        # Calcular o PDC para o usuário e adicionar ao dicionário PDC
        total_days = (end_date - start_date).days + 1
        PDC[user] = min(covered_days / total_days, 1.0)

    # Retornar os dicionários PDC e user_medication
    return PDC, user_medication


def write_PDC_to_file(input_filename, output_filename, PDC, user_medication):
    # Create a new list of dictionaries
    user_data = {}

    with open(input_filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            user_id = row['Usuário']
            if user_id in PDC:
                age = int(row['Idade'])
                sexo = row['Sexo']
                farmaceutico = row['Farmacêutico']
                cenario = row['Cenário']

                if user_id in user_data:
                    # If the user has different Farmacêutico, Sexo or Cenário, exclude them
                    if user_data[user_id]['Farmacêutico'] != farmaceutico or \
                            user_data[user_id]['Cenário'] != cenario or \
                            user_data[user_id]['Sexo'] != sexo:
                        del user_data[user_id]
                        continue
                    # Update age to maximum value
                    user_data[user_id]['Idade'] = max(user_data[user_id]['Idade'], age)
                else:
                    user_data[user_id] = {'Usuário': user_id, 'Idade': age, 'Sexo': sexo, 'Farmacêutico': farmaceutico,
                                          'Cenário': cenario, 'PDC': PDC[user_id]}

    data_with_PDC = list(user_data.values())

    # Define the header for the new CSV file, including PDC
    header = ['Usuário', 'Idade', 'Sexo', 'Farmacêutico', 'Cenário', 'PDC']

    # Open the new CSV file in write mode
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer
        writer = csv.DictWriter(file, fieldnames=header, delimiter=';')
        # Write the header to the CSV file
        writer.writeheader()
        # Write the data_with_PDC data to the CSV file
        writer.writerows(data_with_PDC)
    #print (data_with_PDC)

# Call the write_PDC_to_file function to write the data_with_PDC to a new CSV file
PDC, user_medication = calculate_PDC('Master anom.csv')
write_PDC_to_file('Master anom.csv', 'teste PDC_output.csv', PDC, user_medication)