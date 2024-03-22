class Flowers:

    def __init__(self, name, freshness, color, stem_length, price, lifespan_days):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan_days = lifespan_days

    def __repr__(self):
        return (f"{self.name}, freshness: {self.freshness}%, color: {self.color}, "
                f"stem length: {self.stem_length} cm, ${self.price}, lifespan: {self.lifespan_days} days")


class Rose(Flowers):
    pass


class Tulip(Flowers):
    pass


class Chamomile(Flowers):
    pass


rose = Rose("Rose", 95, "red", 50, 10, 6)
tulip = Tulip("Tulip", 100, "yellow", 20, 5, 5)
chamoline = Chamomile("Chamoline", 90, "white", 60, 7, 7)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower_obj):
        self.flowers.append(flower_obj)

    def get_cost(self):
        return sum(flower_obj.price for flower_obj in self.flowers)

    def get_lifespan(self):
        total_lifespan = sum(flower_obj.lifespan_days for flower_obj in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower_obj: flower_obj.freshness, reverse=True)
        return self.flowers

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower_obj: flower_obj.color)
        return self.flowers

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flowers_obj: flowers_obj.stem_length, reverse=True)
        return self.flowers

    def sort_by_price(self):
        self.flowers.sort(key=lambda flowers_obj: flowers_obj.price, reverse=True)
        return self.flowers

    def find_flowers(self, param_name, param_value):
        if param_name == 'lifespan_days':
            search_flowers = [flower for flower in self.flowers if flower.lifespan_days == param_value]
            if search_flowers:
                return search_flowers
            else:
                return None


bouquet = Bouquet()

bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(chamoline)

print(bouquet.get_cost())
print(bouquet.get_lifespan())
print(bouquet.sort_by_freshness())
print(bouquet.sort_by_color())
print(bouquet.sort_by_stem_length())
print(bouquet.sort_by_price())
print(bouquet.find_flowers('lifespan_days', 6))
