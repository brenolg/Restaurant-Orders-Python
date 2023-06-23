import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu(source_path)

    def load_menu(self, source_path: str) -> None:
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                quantity = int(row["recipe_amount"])

                dish = self.get_dish(name, price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)

    def get_dish(self, name: str, price: str) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish
