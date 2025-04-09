from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient
from azure.ai.ml.entities import AmlCompute
from azure.core.exceptions import ResourceNotFoundError
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar credenciais e cliente Azure ML
credential = DefaultAzureCredential()
ml_client = MLClient(
    credential=credential,
    subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
    resource_group_name=os.getenv("AZURE_RESOURCE_GROUP"),
    workspace_name=os.getenv("AZURE_WORKSPACE_NAME")
)

# Nome do recurso de computação
compute_name = "compute-instance-dinamico"

# Criar o recurso de computação, se não existir
try:
    compute_instance = ml_client.compute.get(compute_name)
    print(f"Recurso de computação já existe: {compute_instance.name}")
except ResourceNotFoundError:
    print(f"Recurso de computação '{compute_name}' não encontrado. Criando um novo...")
    compute_instance = AmlCompute(
        name=compute_name,
        size="STANDARD_DS11_V2",
        min_instances=0,
        max_instances=1
    )
    compute_instance = ml_client.compute.begin_create_or_update(compute_instance).result()
    print(f"Recurso de computação criado: {compute_instance.name}")

# Carregar os dados
sorvetes = pd.read_csv("data/raw/vendas_sorvetes.csv")
print(sorvetes.head())

# Análise exploratória
plt.figure(figsize=(10, 6))
sns.scatterplot(data=sorvetes, x='Temperatura (°C)', y='Vendas')
plt.title('Relação entre Temperatura e Vendas de Sorvetes')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vendas')
plt.show()

# Pré-processamento de dados
X = sorvetes[['Temperatura (°C)']]
y = sorvetes['Vendas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Calcular métricas de desempenho
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')

# Criar o diretório 'data/processed' se não existir
os.makedirs("data/processed", exist_ok=True)

# Salvar o modelo treinado
model_path = "data/processed/modelo_regressao_linear.pkl"
joblib.dump(model, model_path)
print(f"Modelo salvo em: {model_path}")

# Salvar as previsões e os dados reais em um arquivo CSV
resultados = pd.DataFrame({
    "Valores Reais": y_test.values,
    "Valores Previstos": y_pred
})
resultados_path = "data/processed/resultados.csv"
resultados.to_csv(resultados_path, index=False)
print(f"Resultados salvos em: {resultados_path}")