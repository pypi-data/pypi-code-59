DEFAULT_DOMAIN="cloudimg.io"

"""
VERSION 6 VARIABLES
"""
v6_operators = [
    {
        'name_list': ['cdn'],
        'value_reg': ''
    },
    {
        'name_list': ['cdno'],
        'value_reg': ''
    },
    {
        'name_list': ['width'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['height'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['crop'],
        'value_reg': '[0-9]+x[0-9]+'
    },
    {
        'name_list': ['crop_px'],
        'value_reg': '[0-9]+,[0-9]+,[0-9]+,[0-9]+-[0-9]+'
    },
    {
        'name_list': ['cover'],
        'value_reg': '[0-9]+x[0-9]+'
    },
    {
        'name_list': ['fit'],
        'value_reg': '[0-9]+x[0-9]+'
    },
    {
        'name_list': ['bound'],
        'value_reg': '[0-9]+x[0-9]+'
    }
]
v6_filters = [
    {
        'name_list': ['fcontrast'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['fbright'],
        'value_reg': '[0-9]|[0-9][0-9]|2[0-4][0-9]|25[0-5]' # 0-255
    },
    {
        'name_list': ['fgrey'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['fpixelate'],
        'value_reg': ''
    },
    {
        'name_list': ['fgaussian'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['fsharp'],
        'value_reg': '[0-4]'
    },
    {
        'name_list': ['fradius'],
        'value_reg': '[0-9]|1[0-4][0-9]|150' #0-150
    },
    {
        'name_list': ['ftrim'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['r'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['c'],
        'value_reg': '[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]'
    },
    {
        'name_list': ['fbgblur'],
        'value_reg': '[1-9]|1[0-9]|20' # 1-20
    },
    {
        'name_list': ['fbgopacity'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['fwk'],
        'value_reg': ''
    },
    {
        'name_list': ['wpos'],
        'value_reg': '(south|north)(east|west)'
    },
    {
        'name_list': ['wscale'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['wpad'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['q'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['i1'],
        'value_reg': ''
    },
    {
        'name_list': ['tjpg'],
        'value_reg': ''
    },
    {
        'name_list': ['png-lossy-'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['png-lossless'],
        'value_reg': ''
    },
    {
        'name_list': ['tpng'],
        'value_reg': ''
    },
    {
        'name_list': ['png-lossy-20'],
        'value_reg': ''
    },
    {
        'name_list': ['webp-lossy-'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['webp'],
        'value_reg': ''
    },
    {
        'name_list': ['twebp'],
        'value_reg': ''
    },
    {
        'name_list': ['webp-lossy-'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    }
]

v6_params = [
    {
        'name_list': ['mark_url'],
        'value_reg': '.*'
    },
    {
        'name_list': ['mark_alpha'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['mark_pos'],
        'value_reg': '(south|north)(east|west)'
    },
    {
        'name_list': ['mark_size'],
        'value_reg': '([0-9]|[0-9][0-9]|100)pp' #(0-100)pp
    },
    {
        'name_list': ['mark_pad'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['mark_height'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['mark_width'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['mark_text'],
        'value_reg': '.*'
    },
    {
        'name_list': ['mark_fontsize'],
        'value_reg': '[5-9]|[0-9][0-9]|100' #5-100
    },
    {
        'name_list': ['mark_color'],
        'value_reg': '[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]'
    },
    {
        'name_list': ['mark_font'],
        'value_reg': '.*'
    },
    {
        'name_list': ['mark_pad'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    }
]

"""
VERSION 7 VARIABLES
"""
v7_operators = [
    {
        'name_list': ['width', 'w'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['height', 'h'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['org_if_sml'],
        'value_reg': '1'
    },
    {
        'name_list': ['sharp'],
        'value_reg': '1'
    },
    {
        'name_list': ['func'],
        'value_reg': 'crop|face|fit|bound|cover'
    },
    {
        'name_list': ['gravity'],
        'value_reg': '(north|south)(east|west)|auto|[0-9]+,[0-9]+'
    },
    {
        'name_list': ['tl_px'],
        'value_reg': '[0-9]+,[0-9]+'
    },
    {
        'name_list': ['br_px'],
        'value_reg': '[0-9]+,[0-9]+'
    },
    {
        'name_list': ['r'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['trim'],
        'value_reg': '[0-9]+'
    }
]
v7_filters = [
    {
        'name_list': ['bright'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['contrast'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['grey'],
        'value_reg': '1'
    },
    {
        'name_list': ['gray'],
        'value_reg': '1'
    },
    {
        'name_list': ['pixellate'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['pixelate'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['blur'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['sharp'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['radius'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['bg_colour', 'bg_color'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['blur_faces'],
        'value_reg': '1|(TH,?)?(R,?)?(S,?)?(CR)?'
    },
    {
        'name_list': ['f'],
        'value_reg': 'bright:[0-9]+|contrast:[0-9]+|grey|gray|pixellate:[0-9]+|pixelate:[0-9]+|blur:[0-9]+|sharp:[0-9]+|radius:[0-9]+'
    },
    {
        'name_list': ['wat'],
        'value_reg': '1'
    },
    {
        'name_list': ['wat_gravity'],
        'value_reg': '(north-south)(east-west)|center'
    },
    {
        'name_list': ['wat_scale'],
        'value_reg': '([0-9]|[0-9][0-9]|100)p?' #0-100
    },
    {
        'name_list': ['wat_pad'],
        'value_reg': '[0-9]+p?(,[0-9]+p?)?'
    },
    {
        'name_list': ['wat_opacity'],
        'value_reg': '[0-1]'
    },
    {
        'name_list': ['wat_url'],
        'value_reg': '.*'
    },
    {
        'name_list': ['wat_text'],
        'value_reg': '.*'
    },
    {
        'name_list': ['wat_font'],
        'value_reg': '.*'
    },
    {
        'name_list': ['wat_colour', 'wat_color'],
        'value_reg': '[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]'
    },
    {
        'name_list': ['wat_fontsize'],
        'value_reg': '[0-9]+'
    },
    {
        'name_list': ['force_format'],
        'value_reg': 'jpeg|png|webp|'
    },
    {
        'name_list': ['q'],
        'value_reg': '[0-9]|[0-9][0-9]|100' #0-100
    },
    {
        'name_list': ['optipress'],
        'value_reg': '[1-3]'
    },
    {
        'name_list': ['p'],
        'value_reg': '.*'
    }
]