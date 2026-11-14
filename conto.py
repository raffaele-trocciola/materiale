#!/usr/bin/env python3
class ContoBancario():
    
    def __init__ (self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    def deposita(self, importo):
        self.saldo += importo

    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo

    def __str__ (self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print (conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata: ', e)

if __name__ == "__main__":
    main()
