import copy
from itertools import product
from typing import Dict, List, Tuple

import pandas as pd
from bs4 import BeautifulSoup

PathwayAccession = str
KeggXML = str

EntryID = str
EntryType = str

Label = str
Labels = List[Label]
InteractionCategory = str

Entries = Dict[EntryID, "Entry"]
Relations = List["Relation"]


class Entry:
    def __init__(
        self, entry_id: EntryID, accessions: List[str], entry_type: EntryType,
    ):
        if isinstance(accessions, str):
            accessions = accessions.split(" ")
        self.accessions = accessions
        self.entry_id = entry_id
        self.entry_type = entry_type

    def __repr__(self) -> str:
        return (
            f"Entry("
            f"entry_id={self.entry_id}, "
            f"accession={self.accessions}, "
            f"entry_type={self.entry_type})"
        )


class Relation:
    def __init__(
        self,
        source: Entry,
        target: Entry,
        category: InteractionCategory,
        labels: Labels,
    ):
        self.source: Entry = source
        self.target: Entry = target
        self.category: InteractionCategory = category
        self.labels: Labels = labels

    def __repr__(self) -> str:
        return (
            f"Relation("
            f"source={self.source.entry_id}, "
            f"target={self.target.entry_id}, "
            f"category={self.category}, "
            f"labels={self.labels})"
        )


class KeggPathway:
    def __init__(self, xml: KeggXML):
        self.root: BeautifulSoup = BeautifulSoup(xml, features="lxml")
        self._columns: List[str] = ["source", "target", "label"]
        self._interactions: pd.DataFrame = None
        self._relations: Relations = []
        self._entries: Entries = {}

    def __repr__(self) -> str:
        return str(self.root)

    @property
    def entries(self) -> Entries:
        if self._entries:
            return copy.deepcopy(self._entries)

        entries: Entries = self._entries
        for entry in self.root.find_all("entry"):
            kegg_id = entry["id"]
            accessions = entry["name"].split(" ")
            entry_type = entry["type"]
            entry = Entry(kegg_id, accessions, entry_type)
            entries[kegg_id] = entry

        self._entries = copy.deepcopy(entries)
        return entries

    @property
    def relations(self) -> Relations:
        if self._relations:
            return copy.deepcopy(self._relations)

        relations = []
        entries: Entries = self.entries
        for relation in self.root.find_all("relation"):
            subtypes: List[Dict] = relation.find_all("subtype")
            source: Entry = entries[relation["entry1"]]
            target: Entry = entries[relation["entry2"]]
            category: InteractionCategory = relation["type"]
            labels: Labels = [st["name"] for st in subtypes]
            relations.append(
                Relation(
                    source=source,
                    target=target,
                    category=category,
                    labels=labels,
                )
            )

        self._relations = copy.deepcopy(relations)
        return relations

    @property
    def interactions(self) -> pd.DataFrame:
        if self._interactions is not None:
            return self._interactions.copy(deep=True)

        data: Dict = {"source": [], "target": [], "label": []}
        index: List[Tuple[EntryID, EntryID]] = []

        include_categories = ("pprel",)
        for relation in self.relations:
            if relation.category.lower() not in include_categories:
                continue
            if relation.source.entry_type.lower() not in ("gene",):
                continue
            if relation.target.entry_type.lower() not in ("gene",):
                continue

            combinations = product(
                relation.source.accessions, relation.target.accessions
            )
            for s, t in combinations:
                for label in relation.labels:
                    data["source"].append(s)
                    data["target"].append(t)
                    data["label"].append(label)
                    index.append((s, t))

        df = pd.DataFrame(data=data, columns=self._columns, index=index)
        self._ppis = df.copy(deep=True)
        return df
