import pandas as pd
import matplotlib.pyplot as plt
import os

# Criar um DataFrame com os dados fornecidos
data = {
    'Dia': [
        "01/01/2023", "02/01/2023", "03/01/2023", "04/01/2023", "05/01/2023",
        "06/01/2023", "07/01/2023", "08/01/2023", "09/01/2023", "10/01/2023",
        "11/01/2023", "12/01/2023", "13/01/2023", "14/01/2023", "15/01/2023",
        "16/01/2023", "17/01/2023", "18/01/2023", "19/01/2023", "20/01/2023",
        "21/01/2023", "22/01/2023", "23/01/2023", "24/01/2023", "25/01/2023",
        "26/01/2023", "27/01/2023", "28/01/2023", "29/01/2023", "30/01/2023",
        "31/01/2023", "01/02/2023", "02/02/2023", "03/02/2023", "04/02/2023",
        "05/02/2023", "06/02/2023", "07/02/2023", "08/02/2023", "09/02/2023",
        "10/02/2023", "11/02/2023", "12/02/2023", "13/02/2023", "14/02/2023",
        "15/02/2023", "16/02/2023", "17/02/2023", "18/02/2023", "19/02/2023",
        "20/02/2023", "21/02/2023", "22/02/2023", "23/02/2023", "24/02/2023",
        "25/02/2023", "26/02/2023", "27/02/2023", "28/02/2023", "01/03/2023",
        "02/03/2023", "03/03/2023", "04/03/2023", "05/03/2023", "06/03/2023",
        "07/03/2023", "08/03/2023", "09/03/2023", "10/03/2023", "11/03/2023",
        "12/03/2023", "13/03/2023", "14/03/2023", "15/03/2023", "16/03/2023",
        "17/03/2023", "18/03/2023", "19/03/2023", "20/03/2023", "21/03/2023",
        "22/03/2023", "23/03/2023", "24/03/2023", "25/03/2023", "26/03/2023",
        "27/03/2023", "28/03/2023", "29/03/2023", "30/03/2023", "31/03/2023",
        "01/04/2023", "02/04/2023", "03/04/2023", "04/04/2023", "05/04/2023",
        "06/04/2023", "07/04/2023", "08/04/2023", "09/04/2023", "10/04/2023"
    ],
    'Temperatura (°C)': [
        20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
        40, 42, 44, 46, 48, 50, 52, 54, 55, 54,
        52, 50, 48, 46, 44, 42, 40, 38, 36, 34,
        32, 30, 28, 26, 24, 22, 20, 18, 16, 14,
        12, 10, 8, 6, 4, 2, 0, 2, 4, 6,
        8, 10, 12, 14, 16, 18, 20, 22, 24, 26,
        28, 30, 32, 34, 36, 38, 40, 42, 44, 46,
        48, 50, 52, 54, 55, 54, 52, 50, 48, 46,
        44, 42, 40, 38, 36, 34, 32, 30, 28, 26,
        24, 22, 20, 18, 16, 14, 12, 10, 8, 6,
        4, 2, 0, 2, 4, 6, 8, 10, 12, 14,
        16, 18, 20, 22, 24, 26, 28, 30, 32, 34
    ],
    'Vendas': [
        30, 35, 40, 50, 60, 70, 80, 90, 100, 120,
        130, 140, 150, 160, 165, 170, 175, 175, 175, 175,
        170, 160, 150, 140, 130, 120, 110, 100, 90, 80,
        70, 60, 50, 40, 35, 30, 25, 20, 15, 10,
        5, 0, 5, 10, 15, 20, 25, 30, 35, 40,
        50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
        150, 160, 165, 170, 175, 175, 175, 175, 170, 160,
        150, 140, 130, 120, 110, 100, 90, 80, 70, 60,
        50, 40, 35, 30, 25, 20, 15, 10, 5, 0,
        5, 10, 15, 20, 25, 30, 35, 40, 50, 60,
        70, 80, 90, 100, 110, 120, 130, 140, 150, 160
    ]
}

# Verificar comprimentos dos arrays
print(f"Dias: {len(data['Dia'])}, Temperaturas: {len(data['Temperatura (°C)'])}, Vendas: {len(data['Vendas'])}")

# Criar DataFrame apenas com os dados completos
df = pd.DataFrame({
    'Dia': data['Dia'][:min(len(data['Dia']), len(data['Temperatura (°C)']), len(data['Vendas']))],
    'Temperatura (°C)': data['Temperatura (°C)'][:min(len(data['Dia']), len(data['Temperatura (°C)']), len(data['Vendas']))],
    'Vendas': data['Vendas'][:min(len(data['Dia']), len(data['Temperatura (°C)']), len(data['Vendas']))]
})

# Salvar o DataFrame como CSV na pasta data/raw
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)  # Criar a pasta se não existir
output_file = os.path.join(output_dir, "vendas_sorvetes.csv")
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Arquivo CSV salvo em: {output_file}")
