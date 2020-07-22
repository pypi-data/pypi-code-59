"""Module dedicated to gem management."""

import logging
from enum import Enum
from typing import Optional, TextIO

import click

from amethyst.face import Face, FacePosition


class GemType(Enum):
    """Enumeration of gem types, that will impact how faces will be displayed."""

    duo = 2
    quadro = 4
    octo = 8


class Gem:
    """Class used to define and manage gems."""
    # pylint: disable=too-many-instance-attributes

    def __init__(self, north: Optional[Face] = None, north_east: Optional[Face] = None,
                 east: Optional[Face] = None, south_east: Optional[Face] = None,
                 south: Optional[Face] = None, south_west: Optional[Face] = None,
                 west: Optional[Face] = None, north_west: Optional[Face] = None):
        # pylint: disable=too-many-arguments

        self.north: Optional[Face] = north
        self.north_east: Optional[Face] = north_east
        self.east: Optional[Face] = east
        self.south_east: Optional[Face] = south_east
        self.south: Optional[Face] = south
        self.south_west: Optional[Face] = south_west
        self.west: Optional[Face] = west
        self.north_west: Optional[Face] = north_west
        self.type: GemType = GemType.octo

    @classmethod
    def from_module_name(cls, module_name: str) -> 'Gem':
        """Create a gem instance based on a module name"""

        # logging.info('Creating a gem from module name')
        raise NotImplementedError

    @classmethod
    def from_dmenu(cls, dmenu: TextIO) -> 'Gem':
        """Create a gem instance based on a dmenu entry"""

        logging.info('Creating a gem from dmenu.')
        gem = Gem()
        str_faces = [item.strip() for item in dmenu.readlines() if not item.startswith('#') and len(item.strip()) > 0]

        if len(str_faces) > 8:
            raise click.BadOptionUsage('dmenu', 'The dmenu file must have at most 8 items, but %d were provided.'
                                       % len(str_faces))
        if len(str_faces) < 2:
            raise click.BadOptionUsage('dmenu', 'The dmenu file must have at least 2 items, but %d were provided.'
                                       % len(str_faces))

        nowhere_labels = []
        for str_face in str_faces:
            face_items = str_face.split(':')
            if len(face_items) >= 2:
                try:
                    gem.add_face(Face(FacePosition[face_items[0]], str_face.split(':', 1)[1]))
                except KeyError:
                    logging.warning('Not recognised face position \'%s\', using a free space instead.', face_items[0])
                    nowhere_labels.append(face_items[0])
            else:
                nowhere_labels.append(face_items[0])

        for nowhere_label in nowhere_labels:
            gem.add_face_in_free_slot(nowhere_label)

        if gem.north_east or gem.south_east or gem.south_west or gem.north_west:
            logging.info('At least one face among NE, SE, SW or NW is required: using a Octo gem.')
            gem.type = GemType.octo
        elif gem.north or gem.south:
            logging.info('At least one face among N, S is required: using a Quadro gem.')
            gem.type = GemType.quadro
        else:
            logging.info('No specific face is required: using a Duo gem.')
            gem.type = GemType.duo

        return gem

    def add_face_in_free_slot(self, face_label) -> None:
        """Add a face in the gem on the first available free space."""

        faces_priority = [FacePosition.W, FacePosition.E, FacePosition.N, FacePosition.S,
                          FacePosition.NW, FacePosition.NE, FacePosition.SW, FacePosition.SE]

        for face_position in faces_priority:
            if not self.get_face_from_position(face_position):
                self.add_face(Face(face_position, face_label))
                logging.info('Placing face %s in free slot %s.', face_label, face_position.value)
                return

        raise ValueError('No free slot available.')

    def get_face_from_position(self, position: FacePosition) -> Face:
        """Given a face position, returns the corresponding face object in the current gem."""

        faces_position = {FacePosition.N: self.north, FacePosition.NE: self.north_east,
                          FacePosition.E: self.east, FacePosition.SE: self.south_east,
                          FacePosition.S: self.south, FacePosition.SW: self.south_west,
                          FacePosition.W: self.west, FacePosition.NW: self.north_west}

        return faces_position[position]

    def add_face(self, face: Face) -> None:
        """Add a face in the gem on the correct position."""

        if face.position == FacePosition.N:
            self.north = face
        elif face.position == FacePosition.NE:
            self.north_east = face
        elif face.position == FacePosition.E:
            self.east = face
        elif face.position == FacePosition.SE:
            self.south_east = face
        elif face.position == FacePosition.S:
            self.south = face
        elif face.position == FacePosition.SW:
            self.south_west = face
        elif face.position == FacePosition.W:
            self.west = face
        elif face.position == FacePosition.NW:
            self.north_west = face
        else:
            raise ValueError('Unrecognized face position.')
