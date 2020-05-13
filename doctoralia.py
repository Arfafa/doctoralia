import argparse
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-p',
                    '--pages',
                    default=10,
                    type=int,
                    help='Número de páginas a serem percorridas. Default 10')

args = parser.parse_args()


def main():
    base_url = 'https://www.doctoralia.com.br/online/'

    dados = pd.DataFrame(columns=['nome',
                                  'especialidade',
                                  'competencia',
                                  'cidade',
                                  'estado',
                                  'uf'])

    regex_competencias = re.compile(".*?\((.*?)\)")

    for i in range(1, args.pages+1):
        url = base_url+str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for doctor in soup.find_all(class_="panel panel-default"):
            nome = doctor.find(class_="h4 text-base-color offset-bottom-0-5 display-flex-wrap")
            nome = nome.text.strip()

            especialidade = doctor.find(class_='h5 text-base-weight offset-bottom-0 text-muted')

            if especialidade is None:
                competencias = None

            else:
                especialidade = especialidade.text
                competencias = re.findall(regex_competencias, especialidade)
                competencias = ','.join(competencias)
                competencias = ','.join(map(str.strip, competencias.split(',')))

                especialidade = re.sub("[\(\[].*?[\)\]]", "", especialidade)[:-7].strip()
                especialidade = ','.join(map(str.strip, especialidade.split(',')))

            endereco = doctor.find_all(class_='address-name')
            cidade = endereco[-1].find(itemprop='addressLocality')['content'].strip()
            estado = endereco[-1].find(itemprop='addressRegion')['content']
            uf = estado[-2:].strip()
            estado = estado[:-2].strip()

            dados.loc[len(dados)] = [nome,
                                     especialidade,
                                     competencias,
                                     cidade,
                                     estado,
                                     uf]

        dados.to_csv('doctoralia.csv', index=False)


if __name__ == '__main__':
    main()
