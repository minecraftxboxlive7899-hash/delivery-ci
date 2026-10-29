"""Расчёт стоимости доставки заказа."""

EXPRESS_SURCHARGE = 250


def calculate_delivery(subtotal, express=False):
    """Возвращает стоимость доставки в рублях (без стоимости товаров).

    subtotal -- целая неотрицательная сумма товаров в рублях;
    express  -- True для экспресс-доставки (+250 руб.).
    """
    # bool является подклассом int, поэтому проверяем его отдельно
    if isinstance(subtotal, bool) or not isinstance(subtotal, int):
        raise TypeError("subtotal должен быть целым числом (int)")
    if not isinstance(express, bool):
        raise TypeError("express должен быть логическим значением (bool)")
    if subtotal < 0:
        raise ValueError("subtotal не может быть отрицательным")

    if subtotal < 1000:
        cost = 300
    elif subtotal < 5000:
        cost = 150
    else:
        cost = 0

    if express:
        cost += EXPRESS_SURCHARGE
    return cost
