# Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web utilizando Python, PyAutoGUI e Pandas.

## Estrutura

- `main.py`: Script principal de automação.
- `produtos.csv`: Base de dados dos produtos a serem cadastrados.
- `instructions.MD`: Instruções rápidas de instalação.

## Requisitos

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pandas](https://pypi.org/project/pandas/)

Instale as dependências com:

```sh
pip install pyautogui pandas
```

## Como funciona

O script abre o navegador, acessa o site de cadastro, faz login e insere os dados de cada produto do arquivo `produtos.csv` automaticamente.

## Uso

1. Ajuste as posições dos cliques conforme necessário.
2. Execute o script:

```sh
python main.py
```

## Observações

- Certifique-se de que o navegador e o site estejam acessíveis.
- O arquivo `produtos.csv` deve estar no mesmo diretório do script.

## Autor

Projeto para estudo de automação com Python.
