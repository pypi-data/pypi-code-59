from typing import Iterable, Sequence

import pandas as pd

from .tonnage_list import TonnageList
from .column import Column
from .index_level import IndexLevel


class HistoricalTonnageList(Sequence):
    def __init__(self, tonnage_lists: Iterable[TonnageList]):
        self.tonnage_lists = list(tonnage_lists)

    def __getitem__(self, index):
        return self.tonnage_lists.__getitem__(index)

    def __len__(self):
        return self.tonnage_lists.__len__()

    def to_data_frame(self) -> pd.DataFrame:
        index_tuples = []
        data = []
        for tonnage_list in self.tonnage_lists:
            for vessel in tonnage_list.vessels:
                index_tuples.append(
                        (tonnage_list.date.date(), vessel.imo)
                )
                data.append(Column.create_row(vessel))

        data_frame = pd.DataFrame(
            data,
            index=pd.MultiIndex.from_tuples(
                index_tuples,
                names=[IndexLevel.DATE, IndexLevel.IMO]
            ),
            columns=list(Column)
        )

        return data_frame.astype(Column.get_data_types())
