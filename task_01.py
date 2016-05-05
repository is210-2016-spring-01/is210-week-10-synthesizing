#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Too much information"""


def sum_orders(customers, orders):
    """All these orders get put into a neat pile!

    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id

    Returns:
        dictionary of everything put together

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
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
    for key, value in customers.iteritems():
        net_orders, which_order = 0, 0
        for purchase in orders.values():
            if key == purchase['customer_id']:
                net_orders += purchase['total']
                which_order += 1
                combined_list[key] = {'name': value['name'],
                                      'email': value['email'],
                                      'orders': which_order,
                                      'total': net_orders}
    return combined_list
