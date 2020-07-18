import os
import datetime
import requests
from zipfile import ZipFile
from bs4 import BeautifulSoup


class CovidMxData:
    """
    Descarga archivos de datos de Covid 19 de la Dirección General de Epidemiología
    de la Secretaría de Salud del Gobierno de México.
    Puede descargar el archivo más reciente, el diccionario de datos y los archivos
    históricos.
    """

    def __init__(self):
        """
        Constructor.
        Solicita urls de los archivos.
        """
        self.url_dge = 'https://www.gob.mx/salud/documentos/datos-abiertos-152127'
        self.__get_urls()

    def __get_urls(self):
        """
        Obtiene urls de archivos a partir del portal de datos de salud.
        """
        response = requests.get(self.url_dge)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select(
            'div.article-body table tbody > tr > td:nth-child(2) > a')

        if len(table) < 1:
            self.urlRec = ""
            self.urlDicc = ""
            self.urlHist = ""
        else:
            self.urlRec = table[0]['href']
            self.urlDicc = table[1]['href']
            self.urlHist = table[2]['href']

    def __downloadFile(self, url, tipo, extract=True):
        """
        Descarga archivo(s) desde url proporcionada. 

        Parameters:
            url (string): URL proporcionada.
            tipo (string): Tipo de archivo por descargar.
            extract (boolean): Indica si se extrae o no el zip.

        Returns:
            [String]: Nombre(s) de archivo(s) del zip o el nombre del zip descargado.
        """
        zip_files = []
        r = requests.get(url, allow_redirects=True)
        subdir = "historico/" if tipo == "HIST" else ""
        if extract == False:
            zip_files.append(url.rsplit('/', 1)[1])
        file_name = 'descargas_covid/' + subdir + url.rsplit('/', 1)[1]
        open(file_name, 'wb').write(r.content)
        if extract:
            with ZipFile(file_name, 'r') as zip:
                for info in zip.infolist():
                    zip_files.append(info.filename)
                zip.extractall(path='descargas_covid/' + subdir)
                os.remove(file_name)
        return zip_files

    def reciente(self, unzip=True):
        """
        Solicita descarga del archivo más reciente.
        """
        if self.urlRec == "":
            raise ValueError("URL de archivo reciente vacía.")
        if os.path.isdir('descargas_covid') == False:
            os.mkdir('descargas_covid')
        return self.__downloadFile(self.urlRec, "REC", unzip)

    def diccionario_covid(self, unzip=True):
        """
        Solicita descarga de diccionario de datos.
        """
        if self.urlDicc == "":
            raise ValueError("URL de diccionario de datos vacía.")
        if os.path.isdir('descargas_covid') == False:
            os.mkdir('descargas_covid')
        return self.__downloadFile(self.urlDicc, "DICC", unzip)

    def historico_covid(self, unzip=True):
        """
        Solicita descarga de archivos históricos.
        """
        if self.urlHist == "":
            raise ValueError("URL de datos històricos vacía.")

        if os.path.isdir('descargas_covid') == False:
            os.mkdir('descargas_covid')

        if os.path.isdir('descargas_covid/historico') == False:
            os.mkdir('descargas_covid/historico')

        histResponse = requests.get(self.urlHist)

        soupHist = BeautifulSoup(histResponse.text, 'html.parser')

        tables = soupHist.select(
            'div.article-body table tbody tr td:nth-child(2) > a')

        files = []

        cont = 0
        for t in tables:
            if cont == 2:
                break
            histFile = t['href']
            files.extend(self.__downloadFile(histFile, "HIST", unzip))
            cont = cont + 1

        return files
