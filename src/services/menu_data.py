import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_quantity = int(row["recipe_amount"])

                dish = self.get_or_create_dish(dish_name, dish_price)

                ingredient = Ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def get_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish
        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish
