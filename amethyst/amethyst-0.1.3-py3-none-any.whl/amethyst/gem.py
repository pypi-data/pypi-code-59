"""Module dedicated to gem management."""

import logging
from enum import Enum
from typing import NamedTuple
from typing import Optional, TextIO, List, Dict, Tuple

import click

from amethyst.face import Face, FacePosition

Faces = Dict[FacePosition, Optional[Face]]


class GemType(Enum):
    """Enumeration of gem types, that will impact how faces will be displayed."""

    duo = 2
    quadro = 4
    octo = 8


class GemConfig(NamedTuple):
    """Define the configuration parameters related to a gem."""
    outer_size: int = -1
    inner_size: int = -1


class Gem(NamedTuple):
    """Defines a gem, mainly its faces."""

    type: GemType = GemType.octo
    north: Optional[Face] = None
    north_east: Optional[Face] = None
    east: Optional[Face] = None
    south_east: Optional[Face] = None
    south: Optional[Face] = None
    south_west: Optional[Face] = None
    west: Optional[Face] = None
    north_west: Optional[Face] = None

    @classmethod
    def from_module_name(cls, module_name: str) -> 'Gem':
        """Create a gem instance based on a module name"""

        # logging.info('Creating a gem from module name')
        raise NotImplementedError

    @classmethod
    def from_dmenu(cls, dmenu: TextIO) -> 'Gem':
        """Create a gem instance based on a dmenu entry"""

        logging.info('Creating a gem from dmenu.')
        dmenu_items = [item.strip() for item in dmenu.readlines() if not item.startswith('#') and len(item.strip()) > 0]
        logging.info('Dmenu items: \'%s\'.', '\', \''.join(dmenu_items))

        if len(dmenu_items) > 8:
            raise click.BadOptionUsage('dmenu', 'The dmenu file must have at most 8 items, but %d were provided.'
                                       % len(dmenu_items))
        if len(dmenu_items) < 2:
            raise click.BadOptionUsage('dmenu', 'The dmenu file must have at least 2 items, but %d were provided.'
                                       % len(dmenu_items))

        faces, nowhere_labels = cls._get_faces(dmenu_items)
        for nowhere_label in nowhere_labels:
            face = cls._find_free_slot(faces, nowhere_label)
            faces[face.position] = face

        return Gem(type=cls.deduct_gem_type(faces),
                   north=faces[FacePosition.N], north_east=faces[FacePosition.NE],
                   east=faces[FacePosition.E], south_east=faces[FacePosition.SE],
                   south=faces[FacePosition.S], south_west=faces[FacePosition.SW],
                   west=faces[FacePosition.W], north_west=faces[FacePosition.NW])

    @classmethod
    def deduct_gem_type(cls, faces: Faces) -> GemType:
        """Deduct the gem type according to gem faces."""

        if faces[FacePosition.NE] or faces[FacePosition.SE] or faces[FacePosition.SW] or faces[FacePosition.NW]:
            logging.info('At least one face among NE, SE, SW and NW is required: using a Octo gem.')
            gem_type = GemType.octo
        elif faces[FacePosition.N] or faces[FacePosition.S]:
            logging.info('At least one face among N and S is required: using a Quadro gem.')
            gem_type = GemType.quadro
        else:
            logging.info('No specific face is required: using a Duo gem.')
            gem_type = GemType.duo
        return gem_type

    @classmethod
    def _get_faces(cls, dmenu_items: List[str]) -> Tuple[Faces, List[str]]:
        """Get the gem faces, also returns a list of labels that do not have a dedicated position."""

        faces: Dict[FacePosition, Optional[Face]] = {face: None for face in FacePosition}
        nowhere_labels: List[str] = []

        for str_face in dmenu_items:
            face_items = str_face.split(':')
            if len(face_items) >= 2:
                face_label = str_face.split(':', 1)[1]
                try:
                    face_position = FacePosition[face_items[0]]
                    logging.info('Placing face %s in requested slot %s.', face_label, face_position.value)
                    faces[face_position] = Face(face_position, face_label)
                except KeyError:
                    logging.warning('Face %s: not recognised face position \'%s\', using a free space instead.',
                                    face_label, face_items[0])
                    nowhere_labels.append(face_items[0])
            else:
                nowhere_labels.append(face_items[0])

        return faces, nowhere_labels

    @classmethod
    def _find_free_slot(cls, faces: Faces, face_label: str) -> Face:
        """Find a free slot available for a given face."""

        faces_priority: List[FacePosition] = [FacePosition.W, FacePosition.E, FacePosition.N, FacePosition.S,
                                              FacePosition.NW, FacePosition.NE, FacePosition.SW, FacePosition.SE]

        for face_position in faces_priority:
            if not faces[face_position]:
                logging.info('Placing face %s in free slot %s.', face_label, face_position.value)
                return Face(face_position, face_label)

        raise ValueError('No free slot available.')
