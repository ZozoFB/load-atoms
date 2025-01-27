from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml

from load_atoms.util import DATASETS_DIR


@dataclass
class DatabaseEntry:
    name: str
    filenames: List[str]
    description: str
    citation: str = None
    license: str = None

    @classmethod
    def from_file(cls, file: Path):
        with open(file) as f:
            data = yaml.safe_load(f)

        if "filename" in data:
            data["filenames"] = [data["filename"]]
            del data["filename"]

        return cls(**data)


DATASETS = {
    entry.name: entry
    for entry in map(DatabaseEntry.from_file, DATASETS_DIR.glob("**/*.yaml"))
}


def is_known_dataset(dataset_id: str) -> bool:
    """Check if a dataset is known."""
    return dataset_id in DATASETS


def get_database_entry_for(dataset_id: str) -> DatabaseEntry:
    """Get the database entry for a dataset."""
    assert is_known_dataset(dataset_id), f"Dataset {dataset_id} is not known."
    return DATASETS[dataset_id]


# TODO: implement this
def print_info_for(db_entry: DatabaseEntry) -> None:
    """print any license/citation info for a dataset"""
    pass
