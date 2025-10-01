#  Documentação referente aos Robôs RPA do TJPA

## Instalação

Requisitos:

- [Python 3.13](https://www.python.org/)
- [Poetry 2.2.1](https://python-poetry.org/)

### Após clonar o projeto mude para o diretório de instalação e instale as dependências via Poetry

```bash
poetry install
```

## Gerar a documentação

O comando a seguir gera a documentação **HTML** e distribui a mesma automaticamente com *autoreload*
em `http://0.0.0.0:9000`.

```bash
poetry run inv docs
# Ou com ambiente virtual ativado (poetry env activate | source)
inv docs
```
