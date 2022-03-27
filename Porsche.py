class Porsche:
    def __init__(self, model, price, 선호도, 최고속도):
        self.model = model
        self.price = price
        self.선호도 = 선호도
        self.최고속도 = 최고속도

    def set_name(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def set_선호도(self,선호도):
        self.선호도 = 선호도
    
    def set_최고속도(self,최고속도):
        self.최고속도 = 최고속도

종류 = []

포르쉐 = Porsche("카이엔", "2억", "별이 다섯개", 300)
포르쉐2 = Porsche("박스터", "1억", "별이 세개", 200)
포르쉐3 = Porsche("마칸", "5억", "별이 한개", 450)

종류.append(포르쉐)
종류.append(포르쉐2)
종류.append(포르쉐3)

for i in 종류:
    print(i.선호도)