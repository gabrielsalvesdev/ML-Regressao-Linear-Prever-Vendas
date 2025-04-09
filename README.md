# Previsão de Vendas de Sorvetes

## Descrição do Projeto

Este projeto utiliza técnicas de **regressão linear** para prever as vendas de sorvetes com base na temperatura diária. A ideia é explorar a relação entre a temperatura e o comportamento de consumo, permitindo que empresas ajustem sua produção e estoques de forma mais eficiente. Além disso, o projeto integra ferramentas do **Azure Machine Learning** para gerenciar recursos e executar experimentos de forma escalável.

O objetivo principal é fornecer uma solução prática e automatizada para prever vendas, utilizando dados históricos e técnicas de aprendizado de máquina.

---

## Funcionalidades

- **Coleta e processamento de dados**:
  - Carregamento de dados históricos de temperatura e vendas.
  - Pré-processamento e limpeza dos dados para análise.

- **Análise exploratória**:
  - Visualização da relação entre temperatura e vendas utilizando gráficos de dispersão.

- **Treinamento de modelo**:
  - Treinamento de um modelo de regressão linear para prever vendas com base na temperatura.

- **Avaliação do modelo**:
  - Cálculo de métricas como **Mean Squared Error (MSE)** e **R² Score** para avaliar o desempenho do modelo.

- **Exportação de resultados**:
  - Salvamento do modelo treinado em formato `.pkl` para reutilização futura.
  - Exportação das previsões e valores reais em um arquivo `.csv`.

- **Integração com Azure Machine Learning**:
  - Gerenciamento de recursos de computação no Azure.
  - Execução de experimentos diretamente no ambiente do Azure ML.

---

## Tecnologias Utilizadas

- **Linguagem de programação**:
  - Python 3.8+

- **Bibliotecas principais**:
  - `pandas` e `numpy` para manipulação de dados.
  - `matplotlib` e `seaborn` para visualização de dados.
  - `scikit-learn` para treinamento e avaliação do modelo.
  - `joblib` para salvar e carregar o modelo treinado.

- **Ferramentas de nuvem**:
  - **Azure Machine Learning** para gerenciamento de recursos e experimentos.

---

## Estrutura do Projeto

```
ML-Regressao-Linear-Prever-Vendas/
├── data/
│   ├── raw/                # Dados brutos (ex.: vendas_sorvetes.csv)
│   ├── processed/          # Resultados processados (modelos e previsões)
│       ├── modelo_regressao_linear.pkl
│       └── resultados.csv
├── notebooks/
│   ├── Sorveteria.ipynb    # Notebook Jupyter com análise e treinamento
│   └── Sorveteria.py       # Script Python equivalente ao notebook
├── src/
│   └── config.py           # Configuração do projeto
├── .env                    # Variáveis de ambiente (Azure ML)
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── LICENSE                 # Licença do projeto
```

---

## Como Usar

### 1. Pré-requisitos

- Certifique-se de ter o **Python 3.8+** instalado.
- Configure uma conta no **Azure Machine Learning** e crie um workspace.

### 2. Configuração do ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabrielsalvesdev/ML-Regressao-Linear-Prever-Vendas.git
   cd ML-Regressao-Linear-Prever-Vendas
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```env
   AZURE_SUBSCRIPTION_ID=<sua_subscription_id>
   AZURE_RESOURCE_GROUP=<seu_resource_group>
   AZURE_WORKSPACE_NAME=<seu_workspace_name>
   AZURE_TENANT_ID=<seu_tenant_id>
   AZURE_CLIENT_ID=<seu_client_id>
   AZURE_CLIENT_SECRET=<seu_client_secret>
   ```

### 3. Execução

1. **Carregar e processar os dados**:
   - Certifique-se de que o arquivo `vendas_sorvetes.csv` está localizado em `data/raw/`.

2. **Executar o notebook**:
   - Abra o arquivo `notebooks/Sorveteria.ipynb` em um ambiente Jupyter e execute as células para realizar a análise e o treinamento do modelo.

3. **Executar o script Python**:
   - Como alternativa ao notebook, você pode executar o script diretamente:
     ```bash
     python notebooks/Sorveteria.py
     ```

4. **Verificar os resultados**:
   - O modelo treinado será salvo em `data/processed/modelo_regressao_linear.pkl`.
   - As previsões e os valores reais serão salvos em `data/processed/resultados.csv`.

---

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias para melhorias ou encontrar problemas, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:
- **Email**: contato@gabrielsalvesdev
- **LinkedIn**: [Gabriel Sousa](https://www.linkedin.com/in/gabriel-sousa-dev/)


