from pathlib import Path
from morph_tool import converter


if __name__ == '__main__':

    morph_name = '010710HP2'
    h5_path = Path(morph_name + '.h5')
    swc_path = Path(morph_name + '.swc')

    converter.convert(h5_path, swc_path, single_point_soma=True)

