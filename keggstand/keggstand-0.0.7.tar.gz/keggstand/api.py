import io
from typing import Any, Dict, List, Tuple, Union

import pandas as pd
import requests

from .parsers import KeggPathway

Accession = str
AccessionMap = Dict[Accession, List[Accession]]
KeggAccession = Accession

Organism = str

GeneAccession = KeggAccession
GeneName = str
GeneDetail = str

PathwayAccession = KeggAccession
PathwayName = str
KeggXML = str

Organisms = List[Organism]
Pathway = Tuple[PathwayAccession, PathwayName]
Pathways = List[Pathway]
PathwayDetail = KeggXML
Genes = List[Tuple[GeneAccession, GeneName]]

Key = str
NestedKey = List[str]


class NestedDictionary:
    def __init__(self):
        self.dict = {}

    def __repr__(self):
        return repr(self.dict)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def set(self, keys: Union[Key, NestedKey], value: Any):
        if isinstance(keys, str):
            keys = keys.split("__")
        current = self.dict
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
                current = current[key]
        current[keys[-1]] = value
        return self

    def get(self, keys: Union[Key, NestedKey], default: Any = None):
        if isinstance(keys, str):
            keys = keys.split("__")
        current = self.dict
        for key in keys[:-1]:
            current = current.get(key, {})
        return current.get(keys[-1], default)


class Kegg:
    """
    Simple wrapper for KEGG's API.

    Attributes
        organisms (str): KEGG three letter organism code.
    """

    BASE_URL: str = "http://rest.kegg.jp/"

    def __init__(self, cache: bool = True):
        self.use_cache = cache
        self.cache = NestedDictionary()

    @classmethod
    def url_builder(cls, operation: str, arguments: Union[str, List[str]]):
        if isinstance(arguments, str):
            arguments = [arguments]
        if not arguments:
            raise ValueError("At least one argument is required.")
        return "{}{}/{}/".format(cls.BASE_URL, operation, "/".join(arguments))

    @staticmethod
    def get(url: str) -> requests.Response:
        response = requests.get(url)
        if not response.ok:
            raise requests.RequestException(
                f"Request {url} failed with {response.status_code}.",
                response=response,
            )
        return response

    @staticmethod
    def parse_json(response: requests.Response):
        return response.json()

    @staticmethod
    def parse_dataframe(response: requests.Response):
        handle = io.StringIO(response.content.decode())
        df = pd.read_csv(handle, delimiter="\t", header=None)
        return df

    def turn_cache_off(self):
        self.use_cache = False

    def turn_cache_on(self):
        self.use_cache = True

    def get_from_cache(self, keys: Union[Key, NestedKey], **kwargs):
        return self.cache.get(keys, **kwargs)

    def set_cache(self, keys: Union[Key, NestedKey], value: Any):
        return self.cache.set(keys, value)

    def organisms(self) -> Organisms:
        location = ["organism"]
        if self.use_cache and self.get_from_cache(location):
            cached: Organisms = self.get_from_cache(location)
            return cached

        url = self.url_builder("list", "organism")
        df: pd.DataFrame = self.parse_dataframe(self.get(url))

        organisms: Organisms = list(df[1].values)
        self.set_cache(location, organisms)
        return organisms

    def list_pathways(self, organism: Organism) -> Pathways:
        location = ["pathway", organism]
        if self.use_cache and self.get_from_cache(location):
            cached: Pathways = self.get_from_cache(location)
            return cached

        url: str = self.url_builder("list", ["pathway", organism])
        df: pd.DataFrame = self.parse_dataframe(self.get(url))

        pathways: Pathways = list(df.to_records(index=False))
        self.set_cache(location, pathways)
        return pathways

    def list_genes(self, organism: Organism) -> Genes:
        location = [organism]
        if self.use_cache and self.get_from_cache(location):
            cached: Genes = self.get_from_cache(location)
            return cached

        url = self.url_builder("list", organism)
        df: pd.DataFrame = self.parse_dataframe(self.get(url))

        genes: Genes = list(df.to_records(index=False))
        self.set_cache(location, genes)
        return genes

    def get_gene(self, gene: GeneAccession) -> GeneDetail:
        location = ["gene", gene]
        if self.use_cache and self.get_from_cache(location):
            cached: GeneDetail = self.get_from_cache(location)
            return cached

        url = self.url_builder("get", gene)

        detail: GeneDetail = self.get(url).content.decode()
        self.set_cache(location, detail)
        return detail

    def get_pathway(self, pathway: PathwayAccession) -> KeggPathway:
        location = [pathway, "kgml"]
        if self.use_cache and self.get_from_cache(location):
            cached: KeggPathway = KeggPathway(
                xml=self.get_from_cache(location)
            )
            return cached

        pathway = pathway.split(":")[-1]
        url = self.url_builder("get", [pathway, "kgml"])

        detail: PathwayDetail = self.get(url).content.decode()
        self.set_cache(location, detail)
        return KeggPathway(xml=detail)

    def convert(self, source: str, destination: str) -> AccessionMap:
        location = ["conv", source, destination]
        if self.use_cache and self.get_from_cache(location):
            cached: AccessionMap = self.get_from_cache(location)
            return cached

        url = self.url_builder("conv", [source, destination])

        df: pd.DataFrame = self.parse_dataframe(self.get(url))
        mapping: AccessionMap = {}
        for row in df.to_dict("records"):
            # KEGG API is structured as destination first then source.
            dst, src = row.values()
            if source != "hsa":
                src = src.split(":")[-1]
            if destination != "hsa":
                dst = dst.split(":")[-1]

            if src in mapping:
                mapping[src].append(dst)
            else:
                mapping[src] = [dst]

        self.set_cache(location, mapping)
        return mapping
