class Televisão:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv1 = Televisão(pcanal=1, min=2, max=10)
print(tv1.canal)
for x in range (1,20):
    tv1.muda_canal_para_cima()
    print(tv1.canal)

tv2 = Televisão(pcanal=10, min=1, max=10)
print(tv2.canal)
for x in range (1, 20):
    tv2.muda_canal_para_baixo()
    print(tv2.canal)

