"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, product):
        cart.add_product(product, 4)
        assert cart.products[product] == 4

    def test_add_product_more_quantity(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)

    def test_remove_product_from_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 2)
        assert cart.products[product] == 1

    def test_remove_product_complete(self, cart, product):
        cart.add_product(product, 1)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_all_cart(self, cart, product):
        cart.clear()
        assert not cart.products

    def test_total_price(self, cart, product):
        product2 = Product("notebook", 250, "This is a notebook", 25)
        cart.add_product(product, 3)
        cart.add_product(product2, 3)
        total_price = cart.get_total_price()
        assert total_price == (3 * 100) + (3 * 250)

    def test_creating_order(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998

    def test_buy_cart_quantity_about_zero(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 0)
            cart.buy()
            raise ValueError

    def test_buy_cart_quantity_less_zero(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, -1)
            cart.buy()
            raise ValueError
