""" Importação dos módulos dir() """
import utils
from utils.knot_utils import par, conversao_romana, valida_cpf

def is_even(number: int) -> bool:
    return par(number)

def roman_conversion(number: int) -> str:
    return conversao_romana(number)

def cpf_validate(cpf: str) -> bool:
    return valida_cpf(cpf)