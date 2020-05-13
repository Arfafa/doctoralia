# Projeto
Projeto desenvolvido com intuito de realizar raspagem de 
dados do site [Doctoralia](https://www.doctoralia.com.br)

## Como Funciona?

O projeto possui um único arquivo capaz de realizar a 
raspagem de dados do site Doctoralia na sessão de médicos.

Os dados coletados são:
- Nome do médico
- Especialidade(s)
- Competência(s)
- Cidade
- Estado
- UF

### Rodando o projeto

Assim que realizar o download ou clonar o projeto, 
basta rodar o comando:

```bash
$ python doctoralia.py -p 15
```

Após isso, o script raspará as informações presentes 
nas 15 primeiras páginas.

O parâmetro '-p' é opcional, sendo que, caso não seja 
passado, o script buscará as informações  nas primeiras 
10 páginas.

Quando o script terminar de rodar, o arquivo 
'doctoralia.csv' será criado com as informações coletadas.
