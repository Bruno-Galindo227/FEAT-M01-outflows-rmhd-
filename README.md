# FEAT-M01-outflows-rmhd

## Fast-Radio-Bursts (FRBs)

Este repositório foi criado para armazenar os códigos, simulações, notebooks, documentação e demais recursos utilizados na história de usuário **FEAT-01**, desenvolvida para a pesquisa de mestrado sobre **Fast Radio Bursts (FRBs)**.

O **principal objetivo** deste repositório é centralizar o desenvolvimento computacional do projeto, garantindo a organização, rastreabilidade e reprodutibilidade das implementações realizadas ao longo da pesquisa. Para isso, o repositório reúne códigos em desenvolvimento, configurações de simulações, análises de dados, documentação técnica e ferramentas auxiliares utilizadas durante o estudo. 

O objetivo do projeto **"Hipóteses de outflows relativísticos e Magnetares em cenários dinâmicos"** é análisar se simulações de magnetares recém formados de processos como a explosão de uma supernova ou fusão de objetos compactos, são capazes de gerar parâmetros condizentes com os obtidos na literatura ciéntifica para **FRBs** associados a magnetares. 

A infraestrutura do **README** foi desenvolvida com o intuito do controle de versionamente, o registro de alterações, compartilhamento do projeto e a reutilização de resultados obtidos. 

## Estrutura do projeto

```text
FEAT-M01-outflows-rmhd/
│
├── README.md                 # Descrição geral do projeto
├── CHANGELOG.md              # Histórico de alterações
├── environment.yml           # Dependências Python
│
├── docs/                     # Documentação técnica
│   ├── decisions/            # Decisões técnicas (ADRs)
│   └── meetings/             # Atas de reuniões
│
├── notebooks/                # Jupyter Notebooks
├── src/                      # Código-fonte
│
├── data/
│   ├── raw/                  # Dados brutos
│   ├── processed/            # Dados processados
│   └── external/             # Dados externos
│
├── simulations/
│   ├── pluto/                # Casos de simulação PLUTO
│   └── test_cases/           # Testes
│
├── results/
│   ├── figures/              # Figuras geradas
│   ├── tables/               # Tabelas
│   └── logs/                 # Logs das execuções
│
└── writing/
    ├── dissertation/         # Escrita da dissertação
    └── papers/               # Artigos e manuscritos
```

## Ambiente computacional

Sistema operacional:

- Ubuntu 24.04 LTS

Principais dependências:

- PLUTO 4.4 Patch 4
- Chombo
- MPI
- HDF5
- Python 3

---

## Versionamento

O projeto utiliza Git e GitHub para:

- controle de versões;
- rastreabilidade das alterações;
- recuperação de versões anteriores;
- colaboração durante o desenvolvimento.

---
## Comandos 

# 1. Criar o ambiente Conda
conda env create -f environment.yml
# 2. Ativar o ambiente
conda activate feat-m01-outflows-rmhd
# 3. Registrar o ambiente como kernel do Jupyter
python -m ipykernel install --user \
--name feat-m01-outflows-rmhd \
--display-name "FEAT-M01 Outflows RMHD"

---

## Estado atual

Atualmente o projeto encontra-se em fase inicial de desenvolvimento da infraestrutura computacional.

Já foram implementados:

- ambiente PLUTO;
- compilação das dependências;
- organização inicial dos diretórios;
- testes iniciais do ambiente.

---

## Autor

Bruno Ramos Galindo

Mestrado em Astrofísica

Instituto Nacional de Pesquisas Espaciais (INPE)

Orientador: Prof. Dr. Márcio Guilherme Bronzato de Avellar
