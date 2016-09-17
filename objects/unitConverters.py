# https://www.unc.edu/~rowlett/units/symbol.html
from __future__ import division


def __init__(self):
    pass


# Function declaration for converting units
def conv_g_to_mg(v):
    return v * 1000


def conv_g_to_cg(v):
    pass


def conv_g_to_dg(v):
    pass


def conv_g_to_kg(v):
    return v / 1000


def conv_g_to_decag(v):
    pass


def conv_g_to_hg(v):
    pass


def conv_g_to_q(v):
    pass


def conv_g_to_T(v):
    pass


def conv_ml_to_cl(v):
    pass


def conv_ml_to_dl(v):
    pass


def conv_ml_to_l(v):
    pass


def conv_ml_to_hl(v):
    pass


def conv_ml_to_m3(v):
    pass


units = {
    # mass
    'g': {'mg': conv_g_to_mg,
          'cg': conv_g_to_cg,
          'dg': conv_g_to_dg,
          'kg': conv_g_to_kg,
          'decag': conv_g_to_decag,
          'hg': conv_g_to_hg,
          'q': conv_g_to_q,
          'T': conv_g_to_T
          },
    'mg': {},
    'cg': {},
    'dg': {},
    'kg': {},
    'decag': {},
    'q': {},
    'T': {},
    # volume
    'ml': {'cl': conv_ml_to_cl,
           'dl': conv_ml_to_dl,
           'l': conv_ml_to_l,
           'hl': conv_ml_to_hl,
           'm3': conv_ml_to_m3
           },
    'cl': {},
    'dl': {},
    'l': {},
    'hl': {},
    'm3': {}
    # energy

    # gravity
}


# to be used like this:
funct=units['g']['kg'](3)
print "getting function address %r " % funct