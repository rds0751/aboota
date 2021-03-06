from oscar.core import prices


class WithoutCreditOrderTotalCalculator(object):
    """
    Calculator class for calculating the order total.
    """

    def __init__(self, request=None):
        # We store a reference to the request as the total may
        # depend on the user or the other checkout data in the session.
        # Further, it is very likely that it will as shipping method
        # always changes the order total.
        self.request = request

    def calculate(self, basket, shipping_charge, **kwargs):
        excl_tax = basket.total_excl_tax + shipping_charge.excl_tax
        if basket.is_tax_known and shipping_charge.is_tax_known:
            incl_tax = basket.total_incl_tax + shipping_charge.incl_tax
        else:
            incl_tax = None
        return prices.Price(
            currency=basket.currency,
            excl_tax=excl_tax, incl_tax=incl_tax)

class WithCreditOrderTotalCalculator(object):
    """
    Calculator class for calculating the order total.
    """

    def __init__(self, request=None):
        # We store a reference to the request as the total may
        # depend on the user or the other checkout data in the session.
        # Further, it is very likely that it will as shipping method
        # always changes the order total.
        self.request = request

    def calculate(self, basket, shipping_charge, **kwargs):
        excl_tax = basket.total_excl_tax + shipping_charge.excl_tax - basket.total_jr_credit
        if basket.is_tax_known and shipping_charge.is_tax_known:
            incl_tax = basket.total_incl_tax + shipping_charge.incl_tax - basket.total_jr_credit
        else:
            incl_tax = None
        return prices.Price(
            currency=basket.currency,
            excl_tax=excl_tax, incl_tax=incl_tax)
