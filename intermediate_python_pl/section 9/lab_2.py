class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        # self.current_product = 0
        # self.current_promotion = 0
        # self.current_customer = 0

    def __getitem__(self, item):
        if item >= len(self.customers) * len(self.products) * len(self.promotions):
            raise StopIteration()
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions) * len(self.customers))
            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)
            pos_customers = item
        return f'{self.products[pos_products]} - {self.promotions[pos_promotions]} - {self.customers[pos_customers]}'


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)


# for i in range(30):
#     print(combinations[i])

it_comb = iter(combinations)

print(next(it_comb))

for i in it_comb:
    print(i)

