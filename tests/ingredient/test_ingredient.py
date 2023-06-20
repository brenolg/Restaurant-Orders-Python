from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Teste de instanciação correta da classe
    ingredient = Ingredient("Tomato")
    assert ingredient.name == "Tomato"

    # Teste de população correta do atributo restrictions
    ingredient = Ingredient("farinha")
    assert ingredient.restrictions == {Restriction.GLUTEN}

    # Teste do método mágico __repr__
    ingredient = Ingredient("Sugar")
    assert repr(ingredient) == "Ingredient('Sugar')"

    # Teste do método mágico __eq__ para ingredientes iguais
    ingredient1 = Ingredient("Salt")
    ingredient2 = Ingredient("Salt")
    assert ingredient1 == ingredient2
    assert ingredient1 != "Salt"

    # Teste do __hash__ para ingredientes iguais
    ingredient1 = Ingredient("Flour")
    ingredient2 = Ingredient("Flour")
    assert hash(ingredient1) == hash(ingredient2)

    # Teste do __hash__ para ingredientes diferentes
    ingredient1 = Ingredient("Flour")
    ingredient2 = Ingredient("Egg")
    assert hash(ingredient1) != hash(ingredient2)

    # Teste de desigualdade entre ingredientes iguais
    ingredient1 = Ingredient("Egg")
    ingredient2 = Ingredient("Egg")
    assert not (ingredient1 != ingredient2)

    # Teste de igualdade entre ingredientes diferentes
    ingredient1 = Ingredient("Chicken")
    ingredient2 = Ingredient("Beef")
    assert not (ingredient1 == ingredient2)

    # Teste do valor retornado pelo método __repr__
    ingredient = Ingredient("Butter")
    assert repr(ingredient) == "Ingredient('Butter')"

    # Teste do atributo name
    ingredient = Ingredient("Fish")
    assert ingredient.name == "Fish"

    # Teste do atributo restrictions
    ingredient = Ingredient("farinha")
    assert ingredient.restrictions == {Restriction.GLUTEN}
