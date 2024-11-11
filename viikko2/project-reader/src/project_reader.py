from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        text = request.urlopen(self._url).read().decode("utf-8")

        text_parse = toml.loads(text)

        name = text_parse["tool"]["poetry"]["name"]
        description = text_parse["tool"]["poetry"]["description"]
        authors = text_parse["tool"]["poetry"]["authors"]
        dependencies = text_parse["tool"]["poetry"]["dependencies"].keys()
        dev_dependencies = text_parse["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, authors, dependencies, dev_dependencies)