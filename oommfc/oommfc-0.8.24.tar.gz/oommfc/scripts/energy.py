import sys
import numbers
import oommfc as oc
import discretisedfield as df


def energy_script(system):
    mif = ''
    for term in system.energy:
        mif += globals()[(f'{term.__class__.__name__.lower()}'
                          '_script')](term, system)

    return mif


def exchange_script(term, system):
    if isinstance(term.A, numbers.Real):
        mif = '# UniformExchange\n'
        mif += f'Specify Oxs_UniformExchange:{term.name} {{\n'
        mif += f'  A {term.A}\n'
        mif += '}\n\n'

    elif isinstance(term.A, dict):
        if 'default' in term.A.keys():
            default_value = term.A['default']
        else:
            default_value = 0
        mif = '# Exchange6Ngbr\n'
        mif += f'Specify Oxs_Exchange6Ngbr:{term.name} {{\n'
        mif += f'  default_A {default_value}\n'
        mif += '  atlas :main_atlas\n'
        mif += '  A {\n'
        for key, value in term.A.items():
            if key != 'default':
                if ':' in key:
                    region1, region2 = key.split(':')
                else:
                    region1, region2 = key, key
                mif += f'    {region1} {region2} {value}\n'
        mif += '  }\n'
        mif += '}\n\n'

    elif isinstance(term.A, df.Field):
        Amif, Aname = oc.scripts.setup_scalar_parameter(term.A, 'exchange_A')
        mif = Amif
        mif += '# ExchangePtwise\n'
        mif += f'Specify Oxs_ExchangePtwise:{term.name} {{\n'
        mif += f'  A {Aname}\n'
        mif += '}\n\n'

    return mif


def zeeman_script(term, system):
    Hmif, Hname = oc.scripts.setup_vector_parameter(term.H, 'zeeman_H')

    mif = ''
    mif += Hmif

    if isinstance(term.wave, str):
        if term.wave == 'sin':
            mif += 'proc TimeFunction { total_time } {\n'
            mif += '  set PI [expr {4*atan(1.)}]\n'
            mif += f'  set w [expr {{ {term.f}*2*$PI }}]\n'
            mif += f'  set tt [expr {{ $total_time - {term.t0} }}]\n'
            mif += f'  set wt [expr {{ $w*$tt }}]\n'
            mif += '  set f [expr {sin($wt)}]\n'
            mif += '  set df [expr {$w*cos($wt)}]\n'
            mif += f'  set Hx [expr {{ {term.H[0]}*$f }}]\n'
            mif += f'  set Hy [expr {{ {term.H[1]}*$f }}]\n'
            mif += f'  set Hz [expr {{ {term.H[2]}*$f }}]\n'
            mif += f'  set dHx [expr {{ {term.H[0]}*$df }}]\n'
            mif += f'  set dHy [expr {{ {term.H[1]}*$df }}]\n'
            mif += f'  set dHz [expr {{ {term.H[2]}*$df }}]\n'
            mif += '  return [list $Hx $Hy $Hz $dHx $dHy $dHz ] \n'
            mif += '}\n\n'
        elif term.wave == 'sinc':
            mif += 'proc TimeFunction { total_time } {\n'
            mif += '  set PI [expr {4*atan(1.)}]\n'
            mif += f'  set w [expr {{ {term.f}*2*$PI }}]\n'
            mif += f'  set tt [expr {{ $total_time - {term.t0} }}]\n'
            mif += '  set wt [expr {$w*$tt}]\n'
            mif += '  set sinwt [expr {sin($wt)}]\n'
            mif += '  set coswt [expr {cos($wt)}]\n'
            mif += '  if {$wt != 0} { set f [expr {$sinwt/$wt}] }\n'
            mif += '  if {$wt == 0} { set f [expr {1}] }\n'
            mif += ('  if {$wt != 0} { set df '
                    '[expr {($wt*$w*$coswt - $w*$sinwt)/($wt*$wt)}] }\n')
            mif += '  if {$wt == 0} { set df [expr {0}] }\n'
            mif += f'  set Hx [expr {{ {term.H[0]}*$f }}]\n'
            mif += f'  set Hy [expr {{ {term.H[1]}*$f }}]\n'
            mif += f'  set Hz [expr {{ {term.H[2]}*$f }}]\n'
            mif += f'  set dHx [expr {{ {term.H[0]}*$df }}]\n'
            mif += f'  set dHy [expr {{ {term.H[1]}*$df }}]\n'
            mif += f'  set dHz [expr {{ {term.H[2]}*$df }}]\n'
            mif += '  return [list $Hx $Hy $Hz $dHx $dHy $dHz ] \n'
            mif += '}\n\n'

        mif += '# ScriptUZeeman\n'
        mif += f'Specify Oxs_ScriptUZeeman:{term.name} {{\n'
        mif += f'  script_args total_time\n'
        mif += f'  script TimeFunction\n'
        mif += '}\n\n'
    else:
        mif += '# FixedZeeman\n'
        mif += f'Specify Oxs_FixedZeeman:{term.name} {{\n'
        mif += f'  field {Hname}\n'
        mif += '}\n\n'

    return mif


def demag_script(term, system):
    mif = '# Demag\n'
    if system.m.mesh.bc in ('neumann', 'dirichlet', ''):  # no PBC
        oxs_cls = 'Oxs_Demag'
    else:  # PBC
        if len(system.m.mesh.bc) == 1:
            oxs_cls = 'Oxs_Demag'
        elif len(system.m.mesh.bc) >= 2:
            msg = ('Demagnetisation energy term with periodic boundary '
                   'conditions in three directions is not supported.')
            raise ValueError(msg)

    mif += f'Specify {oxs_cls}:{term.name} {{\n'
    if hasattr(term, 'asymptotic_radius'):
        mif += f'  asymptotic_radius {term.asymptotic_radius}\n'
    mif += '}\n\n'

    return mif


def dmi_script(term, system):
    if term.crystalclass in ['T', 'O']:
        oxs = 'Oxs_DMI_T'
    elif term.crystalclass == 'D2d':
        oxs = 'Oxs_DMI_D2d'
    elif term.crystalclass == 'Cnv':
        if sys.platform == 'win32' and system.m.mesh.bc == '':
            oxs = 'Oxs_DMExchange6Ngbr'
        else:
            oxs = 'Oxs_DMI_Cnv'

    mif = f'# DMI of crystallographic class {term.crystalclass}\n'
    mif += f'Specify {oxs}:{term.name} {{\n'

    if isinstance(term.D, numbers.Real):
        mif += f'  default_D {term.D}\n'
        mif += '  atlas :main_atlas\n'
        mif += '  D {\n'
        mif += f'    main main {term.D}\n'
        mif += '  }\n'
        mif += '}\n\n'

    elif isinstance(term.D, dict):
        if 'default' in term.D.keys():
            default_value = term.D['default']
        else:
            default_value = 0
        mif += f'  default_D {default_value}\n'
        mif += '  atlas :main_atlas\n'
        mif += '  D {\n'
        for key, value in term.D.items():
            if key != 'default':
                if ':' in key:
                    region1, region2 = key.split(':')
                else:
                    region1, region2 = key, key
                mif += f'    {region1} {region2} {value}\n'
        mif += '  }\n'
        mif += '}\n\n'

    return mif


def uniaxialanisotropy_script(term, system):
    umif, uname = oc.scripts.setup_vector_parameter(term.u, 'ua_u')

    # Determine if higher-order anisotropy is defined
    if isinstance(term.K2, (numbers.Real, dict, df.Field)):
        k1mif, k1name = oc.scripts.setup_scalar_parameter(term.K1, 'ua_K1')
        k2mif, k2name = oc.scripts.setup_scalar_parameter(term.K2, 'ua_K2')

        mif = ''
        mif += k1mif
        mif += k2mif
        mif += umif
        mif += '# UniaxialAnisotropy\n'
        mif += f'Specify Southampton_UniaxialAnisotropy4:{term.name} {{\n'
        mif += f'  K1 {k1name}\n'
        mif += f'  K2 {k2name}\n'
        mif += f'  axis {uname}\n'
        mif += '}\n\n'

    else:
        kmif, kname = oc.scripts.setup_scalar_parameter(term.K, 'ua_K')

        mif = ''
        mif += kmif
        mif += umif
        mif += '# UniaxialAnisotropy\n'
        mif += f'Specify Oxs_UniaxialAnisotropy:{term.name} {{\n'
        mif += f'  K1 {kname}\n'
        mif += f'  axis {uname}\n'
        mif += '}\n\n'

    return mif


def cubicanisotropy_script(term, system):
    kmif, kname = oc.scripts.setup_scalar_parameter(term.K, 'ca_K')
    u1mif, u1name = oc.scripts.setup_vector_parameter(term.u1, 'ca_u1')
    u2mif, u2name = oc.scripts.setup_vector_parameter(term.u2, 'ca_u2')

    mif = ''
    mif += kmif
    mif += u1mif
    mif += u2mif
    mif += '# CubicAnisotropy\n'
    mif += f'Specify Oxs_CubicAnisotropy:{term.name} {{\n'
    mif += f'  K1 {kname}\n'
    mif += f'  axis1 {u1name}\n'
    mif += f'  axis2 {u2name}\n'
    mif += '}\n\n'

    return mif


def magnetoelastic_script(term, system):
    B1mif, B1name = oc.scripts.setup_scalar_parameter(term.B1, 'mel_B1')
    B2mif, B2name = oc.scripts.setup_scalar_parameter(term.B2, 'mel_B2')
    ediagmif, ediagname = oc.scripts.setup_vector_parameter(
        term.e_diag, 'mel_ediag')
    eoffdiagmif, eoffdiagname = oc.scripts.setup_vector_parameter(
        term.e_offdiag, 'mel_eoffdiag')

    mif = ''
    mif += B1mif
    mif += B2mif
    mif += ediagmif
    mif += eoffdiagmif
    mif += '# MagnetoElastic\n'
    mif += f'Specify YY_FixedMEL:{term.name} {{\n'
    mif += f'  B1 {B1name}\n'
    mif += f'  B2 {B2name}\n'
    mif += f'  e_diag_field {ediagname}\n'
    mif += f'  e_offdiag_field {eoffdiagname}\n'
    mif += '}\n\n'

    return mif


def rkky_script(term, system):
    sr1 = system.m.mesh.subregions[term.subregions[0]]
    sr2 = system.m.mesh.subregions[term.subregions[1]]

    direction, first, second = sr1 | sr2

    for key, value in system.m.mesh.subregions.items():
        if value == first:
            first_name = key
        elif value == second:
            second_name = key

    mif = ''

    mif += '# Scalar field for RKKY surfaces\n'
    mif += 'Specify Oxs_LinearScalarField:rkkyfield {\n'
    vectorval = df.util.assemble_index(0, 3, {df.util.axesdict[direction]: 1})
    mif += '  vector {{{} {} {}}}\n'.format(*vectorval)
    mif += '  norm 1.0\n'
    mif += '}\n\n'

    mif += '# TwoSurfaceExchange\n'
    mif += f'Specify Oxs_TwoSurfaceExchange:{term.name} {{\n'
    if isinstance(term.sigma, numbers.Real):
        mif += f'  sigma {term.sigma}\n'
    if isinstance(term.sigma, numbers.Real):
        mif += f'  sigma2 {term.sigma2}\n'

    mif += '  surface1 {\n'
    mif += '    atlas :main_atlas\n'
    mif += f'    region {first_name}\n'
    mif += '    scalarfield :rkkyfield\n'
    mif += f'    scalarvalue {first.pmax[df.util.axesdict[direction]]}\n'
    mif += f'    scalarside -\n'
    mif += '  }\n'

    mif += '  surface2 {\n'
    mif += '    atlas :main_atlas\n'
    mif += f'    region {second_name}\n'
    mif += '    scalarfield :rkkyfield\n'
    mif += f'    scalarvalue {second.pmin[df.util.axesdict[direction]]}\n'
    mif += f'    scalarside +\n'
    mif += '  }\n'

    mif += '}\n\n'

    return mif
