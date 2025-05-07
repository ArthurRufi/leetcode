# test_a.py
from peaples import Peaples

def test_nomear_pessoa_retorna_nome_em_str():
    nome = "artold"
    p = Peaples(nome)
    resultado = p.nomear_pessoa()  # Certifique-se de que está chamando o método
    assert resultado == nome
