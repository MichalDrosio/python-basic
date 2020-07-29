import string

def cezar(napis, klucz):
    alfabet = string.ascii_lowercase
    kod = alfabet[klucz:] + alfabet[:klucz]
    tabela = str.maketrans(alfabet, kod)
    return napis.translate(tabela)