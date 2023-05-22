from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest

from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish = Dish("pizza", 10)
    assert dish.name == "pizza"

    dish1 = Dish("pizza", 10)
    dish2 = Dish("pizza", 10)
    assert hash(dish1) == hash(dish2)

    dish1 = Dish("pizza", 10)
    dish2 = Dish("hamburguer", 12)
    assert hash(dish1) != hash(dish2)

    dish = Dish("pizza", 10)
    assert repr(dish) == "Dish('pizza', R$10.00)"

    with pytest.raises(TypeError):
        Dish("name", "price")

    with pytest.raises(ValueError):
        Dish("name", -1)

    dish = Dish("pizza", 10)
    dish.recipe = {"tomate": 2, "queijo": -1}
    assert dish.recipe.get("alface") is None

    dish1.add_ingredient_dependency(Ingredient("farinha"), 100)

    assert dish1.get_ingredients() == {
        Ingredient("farinha"),
    }

    assert dish1.get_restrictions() == {
        Restriction.GLUTEN,
    }

    dish1 = Dish("pizza", 10)
    dish1.recipe = {"tomate": 2, "queijo": 1}
    dish2 = Dish("pizza", 10)
    dish2.recipe = {"tomate": 2, "queijo": 1}
    assert dish1 == dish2
