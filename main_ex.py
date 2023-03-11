"""Funkcje które się nie uruchomią jeśli plik zostanie zaimportowany"""
def funkcja1():
    """Funkcja 1"""
    print('funkcja1')

def funkcja2():
    """Funkcja 2"""
    print('funkcja2')

if __name__=="__main__""":
    funkcja1()
    funkcja2()
