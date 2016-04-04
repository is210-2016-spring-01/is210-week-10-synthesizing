#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""


def sum_orders(cust, order):
    """Defines a function that combines two data sets into a dictionary.

    Args:
        cust (dict): a dictionary of customers keyed by customer id
        order (dict): a dictionary of orders keyed by order id

    Returns:
        combined_list (dict): a dictionary combining the two data sets

    Example:
        >>> ORDERS = {1: {'customer_id': 2, 'total':10},
        3: {'customer_id': 2, 'total':10},
        4: {'customer_id': 3, 'total':15}}
        >>> CUSTOMERS = {2: {'name': 'Person One;, 'email': 'email@one.com},
        3: {'name': 'Person Two;, 'email': 'email@two.com}}
        >>> sum_orders(cust=CUSTOMERS, order=ORDERS)
        {2: {'name': 'Person One',
        'email': 'email@one.com',
        'orders': 2,
        'total': 20}
        3: {'name': 'Person Two',
        'email': 'email@two.com',
        'orders': 1,
        'total': 15}}
        """
    combined_list = {}
    for key, val in cust.iteritems():
        orders = 0
        totals = 0
        for i in order.values():
            if key == i['customer_id']:
                orders += 1
                totals += i['total']
                combined_list[key] = {'name': val['name'],
                                      'email': val['email'],
                                      'orders': orders,
                                      'total': totals}

    return combined_list
