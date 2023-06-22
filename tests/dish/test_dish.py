import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    Pizza = Dish("Pizza", 12.00)
    Pizza2 = Dish("Pizza", 12.00)
    Rice = Dish("Rice", 10.00)
    XBacon = Dish("XBacon", 10.00)

    # Testa atributo name é diferente do passado no construtor
    assert Pizza.name == "Pizza"

    # Test os hashes
    assert hash(Rice) == hash(Rice)
    assert (Pizza) == (Pizza2)
    assert hash(XBacon) != hash(Rice)

    # Testa preço
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("XBacon", None)
    with pytest.raises(ValueError,
         match="Dish price must be greater then zero."):
        Dish("Beans", 0)
    assert XBacon.price + Rice.price == 20.00

    # test Ingredient
    Bacon = Ingredient("bacon")
    XBacon.add_ingredient_dependency(Bacon, 1)

    assert XBacon.get_ingredients() == {Bacon}

    # test Restrictions
    assert XBacon.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    # test __repr__
    assert hash(XBacon) == hash(repr(XBacon))
    assert repr(XBacon) == "Dish('XBacon', R$10.00)"
