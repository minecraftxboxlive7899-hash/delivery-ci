import pytest

from delivery import calculate_delivery


# --- Обычная доставка: обычные и граничные значения ---
@pytest.mark.parametrize(
    "subtotal, expected",
    [
        (0, 300),
        (500, 300),
        (999, 300),
        (1000, 150),
        (3000, 150),
        (4999, 150),
        (5000, 0),
        (10000, 0),
    ],
)
def test_standard_delivery(subtotal, expected):
    assert calculate_delivery(subtotal) == expected


# --- Экспресс-доставка: +250 руб., в том числе для заказов от 5000 ---
@pytest.mark.parametrize(
    "subtotal, expected",
    [
        (0, 550),
        (999, 550),
        (1000, 400),
        (4999, 400),
        (5000, 250),
        (10000, 250),
    ],
)
def test_express_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=True) == expected


def test_express_false_equals_default():
    assert calculate_delivery(1000, express=False) == calculate_delivery(1000)


def test_free_standard_delivery_from_5000():
    assert calculate_delivery(5000) == 0


def test_express_is_standard_plus_250():
    for subtotal in (0, 999, 1000, 4999, 5000):
        assert calculate_delivery(subtotal, True) == calculate_delivery(subtotal) + 250


# --- Ошибочные данные ---
@pytest.mark.parametrize("subtotal", [-1, -1000])
def test_negative_subtotal_raises_value_error(subtotal):
    with pytest.raises(ValueError):
        calculate_delivery(subtotal)


@pytest.mark.parametrize("subtotal", ["1000", 1000.5, None, [1000], True, False])
def test_invalid_subtotal_type_raises_type_error(subtotal):
    with pytest.raises(TypeError):
        calculate_delivery(subtotal)


@pytest.mark.parametrize("express", ["yes", 1, 0, None])
def test_invalid_express_type_raises_type_error(express):
    with pytest.raises(TypeError):
        calculate_delivery(1000, express)
