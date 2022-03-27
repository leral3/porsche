from statistics import mode


class Porsche:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def set_name(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

포르쉐 = Porsche("박스터", "2억")

print(포르쉐.get_model())