from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    farinha = Ingredient("farinha")
    bacon = Ingredient("bacon")

    assert farinha.name == "farinha"
    assert farinha.restrictions == {Restriction.GLUTEN}
    assert farinha.__repr__() == "Ingredient('farinha')"

    assert hash(farinha) != hash(bacon)
    assert hash(farinha) == hash(farinha)
    assert farinha.__eq__(farinha)
