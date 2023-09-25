from decimal import Decimal


def output_currency(val: Decimal):
    return "${:,.2f}".format(val)