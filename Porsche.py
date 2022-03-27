from statistics import mode


class Porsche:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def set_name(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

포르쉐 = Porsche(None, None)

포르쉐.set_name("카이엔")
포르쉐.set_price("2억")

print(포르쉐.model)
print(포르쉐.price)