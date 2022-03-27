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



포르쉐 = Porsche("박스터", "2억","별이다섯개",300)

print(포르쉐.model)
print(포르쉐.선호도)