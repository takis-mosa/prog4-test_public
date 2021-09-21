import pytest
from .part1 import *


def test_volume_kubus_0():
    assert volume_kubus(0) == 0


def test_volume_kubus_3():
    assert volume_kubus(3) == 27


def test_volume_kubus_4():
    assert volume_kubus(4) == 64


def test_volume_kubus_raises_exception_on_negative_or_zero_with_message():
    with pytest.raises(RuntimeError, match=r"negatieve lengte"):
        volume_kubus(-1)


def test_minutes_in_day():
    assert minutes_in_day(1) == 60 * 24


def test_minutes_in_2_days():
    assert minutes_in_day(2) == 2 * 60 * 24


def test_minutes_in_week():
    assert minutes_in_week(1) == 7 * 60 * 24


def test_minutes_in_two_weeks():
    assert minutes_in_week(2) == 2 * 7 * 60 * 24


def test_minutes_in_day_raises_custom_exception_on_negative():
    with pytest.raises(NegativeDuration):
        minutes_in_day(-10)


def test_list_of_squares_1():
    assert list_of_squares(1) == [0]


def test_list_of_squares_4():
    assert list_of_squares(4) == [0, 1, 4, 9]


def test_list_of_squares_20():
    assert list_of_squares(4) == [0, 1, 4, 9]


def test_product_of_list_1():
    assert product_of_list([4]) == 4


def test_product_of_list_2():
    assert product_of_list([3, 10]) == 30


def test_product_of_list_3():
    assert product_of_list([2, 30, 5]) == 300


def test_product_of_list_4():
    assert product_of_list([100, 4, 1, 2]) == 800


def test_price_search_empty():
    articles = []
    price_search(articles, "Ghost of Tsushima") == None


def test_price_search():
    articles = [
        ["FIFA 22", 54],
        ["Mario Kart 8 Deluxe", 51],
        ["Ghost of Tsushima", 40],
        ["Red Dead Redemption 2", 45],
    ]
    price_search(articles, "Ghost of Tsushima") == 40


def test_price_search_rdr2():
    articles = [
        ["FIFA 22", 54],
        ["Mario Kart 8 Deluxe", 51],
        ["Ghost of Tsushima", 40],
        ["Red Dead Redemption 2", 45],
    ]
    price_search(articles, "Red Dead Redemption 2") == 45


def test_price_search_not_found():
    articles = [
        ["FIFA 22", 54],
        ["Mario Kart 8 Deluxe", 51],
        ["Ghost of Tsushima", 40],
        ["Red Dead Redemption 2", 45],
    ]
    price_search(articles, "Terraria") == None
