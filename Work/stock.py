class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares):
        if num_shares > self.shares:
            raise RuntimeError("NO CAN DO")
        else:
            self.shares -= num_shares
