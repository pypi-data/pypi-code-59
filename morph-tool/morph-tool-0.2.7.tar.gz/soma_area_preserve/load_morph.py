#!/usr/bin/env python
import sys
from pathlib import Path
from bluepyopt.ephys import simulators, morphologies, models
import neurom
from neurom.features import neuronfunc
import numpy as np
from morph_tool import diff
from morphio import SomaType
from morphio.mut import Morphology


def soma_to_single_point(soma, soma_NRN_surface):
    assert soma.type == SomaType.SOMA_SIMPLE_CONTOUR
    r0 = 0.5 * soma.diameters[:-1]
    r1 = 0.5 * soma.diameters[1:]
    h2 = np.sum((soma.points[:-1] - soma.points[1:]) ** 2., axis=1)
    print('r0', r0, 'r1', r1, 'h2', h2)

    center = np.mean(soma.points, axis=0)
    print(soma.points)
    print(center - soma.points)
    print(np.linalg.norm(soma.points - center, axis=1))
    print(np.min(np.linalg.norm(soma.points - center, axis=1)))
    radius = np.max(np.linalg.norm(soma.points - center, axis=1))
    # surface_area = 4 * np.pi * (.5 * radius) ** 2
    # print(surface_area)
    soma.points = center[None, :]
    # surface_area = np.sum(np.pi * (r0 + r1) * np.sqrt((r0 - r1) ** 2 + h2))
    surface_area = soma_NRN_surface
    print(surface_area)
    soma.diameters = [float((surface_area / np.pi) ** 0.5)]
    print(soma.points)
    # return


def _section_points(h_section):
    points = []
    for ipt in range(h_section.n3d()):
        x = h_section.x3d(ipt)
        y = h_section.y3d(ipt)
        z = h_section.z3d(ipt)
        points.append([x, y, z])
    # somehow it's revered comparing to morph-tool convert
    points = list(reversed(points))
    return np.array(points)


def _section_diameters(h_section):
    diams = [h_section.diam3d(ipt) for ipt in range(h_section.n3d())]
    diams = list(reversed(diams))
    return np.array(diams)


def compare_new_xyz():
    import pandas as pd
    new_xyz_neuron = pd.read_csv('new_xyz_neuron.txt').to_numpy()
    new_xyz_morph_tool = pd.read_csv('new_xyz_morph-tool.txt').to_numpy()
    print(np.allclose(new_xyz_neuron, new_xyz_morph_tool))
    diff = new_xyz_neuron - new_xyz_morph_tool
    bad_ids = diff > 1e-6
    print(diff[bad_ids])

def load_morph(path):
    sim = simulators.NrnSimulator()
    h = sim.neuron.h
    icell = models.CellModel('model', path, [], [])
    morph = morphologies.NrnFileMorphology(path, do_replace_axon=False, do_set_nseg=True)
    morph.instantiate(sim, icell)

    assert len(icell.soma) == 1
    soma_sec = icell.soma[0]

    # neurom_nrn = neurom.load_neuron(path)
    # print('neurom Soma Area: ', neuronfunc.soma_surface_area(neurom_nrn))
    # print('Sphere surface area', 4 * np.pi * (.5 * soma_sec.L) ** 2)
    print('NEURON Soma Area: ', h.area(0.5, sec=soma_sec))
    print('NEURON Soma Length: ', soma_sec.L)


if __name__ == '__main__':
    from morph_tool.neuron_surface import get_NEURON_surface

    morph_name = '010710HP2'
    h5_path = Path(morph_name + '.h5')
    asc_path = Path(morph_name + '_proj42.asc')
    swc_path = Path(morph_name + '.swc')
    print('#### ASCII')
    load_morph(str(asc_path))
    # NEURON Soma Area:  885.3939304816817
    # NEURON Soma Length:  28.84645698701402
    print('#### SWC')
    load_morph(str(swc_path))
    # morphology = Morphology(h5_path)
    # soma_to_single_point(morphology.soma, get_NEURON_surface(str(asc_path)))
    # if diff(asc_path, swc_path):
    #     print('morphologies differ')
    # else:
    #     print('morphologies equal according to morph-tool')
