#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a sum of orders."""


def sum_orders(customers, orders):
    """Combine customers and order dictionaries.

    Args:
        customers (dict): Dictionary of customers keyed by customer id.
        orders (dict): Dictionary of orders keyed by order id.

    Returns:
        dict: Merged dictionaries with new total order value.

    Examples:
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'orders': 2, 'total': 20, 'name': 'Person One',
        'email': 'email@one.com'},3: {'orders': 1, 'total': 15,
        'name': 'Person Two', 'email': 'email@two.com'}}

        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {1: {'orders': 1, 'total': 199, 'name': 'steve langford',
        'email': 'news@100.com'}, 2: {'orders': 1, 'total': 777,
        'name': 'jon lieberman', 'email': 'embedded@100.com'}}
    """
    totalordered = {}
    for cust_id, total in customers.iteritems():  # Loop customers dict
        order_qty = 0  # Reset order counter
        order_amt = 0  # Reset total orders sum for same customer
        for orderkey, order in orders.iteritems():  # Loop orders dict
            if cust_id == order['customer_id']:  # Pair customer IDs
                order_qty += 1  # Update order counter for each match
                order_amt += order['total']  # Update running sum for ID
            if order_qty > 0:
                totalordered[cust_id] = {'email': customers[cust_id]['email'],
                                         'name': customers[cust_id]['name'],
                                         'orders': order_qty,
                                         'total': order_amt}  # Insert keyvals
            else:
                pass
    return totalordered
