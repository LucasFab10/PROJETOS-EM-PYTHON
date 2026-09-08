class Extrato:
    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, conta):
        print(f"Extrato da conta: {conta}\n")

        for tran in self.transacoes:
            print(
                f"{tran[0]:15s} "
                f"R$ {tran[1]:10.2f} "
                f"{tran[2].strftime('%d/%m/%Y')}"
            )