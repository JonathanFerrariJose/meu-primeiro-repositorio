## Exemplo de README para o seu projeto
```markdown
# Faxina de dados

Lê `sujo.csv` e grava `limpo.csv` com nome, telefone e data padronizados.

## Como rodar
    python faxina.py

## Arquivos
- `faxina.py`: lê o CSV, usa as funções e grava o resultado
- `limpeza.py`: funções de limpeza (nome, telefone, data)
- `sujo.csv`: dados fictícios de entrada
```

## Estrutura de um projeto organizado
```text
meu-projeto/
|-- main.py
|-- limpeza.py
|-- dados/
|   `-- sujo.csv
|-- requirements.txt
|-- .gitignore
`-- README.md
```
Código em módulos, dados em uma pasta própria, dependências listadas, README explicando o projeto e `.gitignore` protegendo o que não deve subir: esse é o formato ideal de um repositório no GitHub.

## Git deste exercício
```bash
git switch -c feature/refatoracao-faxina
git add limpeza.py faxina.py README.md
git commit -m "Refatora a faxina em funções e módulo"
git push -u origin feature/refatoracao-faxina
```
Depois, no GitHub, **Compare & pull request** → descreva a mudança → **Create pull request**.