# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.

def discount_factor(base_price):
    """Returns the dicount percentage based on price"""
    if base_price > 1000:
        return 0.95
    else:
        return 0.98


def get_price(quantity, item_price):
    """Returns price after dicounted rate"""
    base_price = quantity * item_price
    return base_price * discount_factor(base_price)
