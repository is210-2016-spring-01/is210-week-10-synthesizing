#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Correlation"""


def sum_orders(customers, orders):
    """A function which sum's orders

    Args:
        customers (dict): A dictionary of customers by customer_id.
        orders (dict): A dictionary of orders keyed by order id.
    Returns:
        (dict): the combined dictionary of customers and orders.
    Examples:
        >>> ORDERS = {1: {'customer_id': 1, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Cordelia Naismith', 'email':
        'cordelia@beta.com'},3: {'name': 'Ivan Vorpatril', 'email':
        'iv398@barrayar.net'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Cordelia Naismith',
        'email': ''cordelia@beta.com,
        'orders': 2,
        'total': 20}
        3: {'name': 'Ivan Vorpatril',
        'email': 'iv398@barrayar.net',
        'orders': 1,
        'total': 15}}
    """
    customer_list = {}
    for key, value in customers.iteritems():
        tot_orders = 0
        num_orders = 0
        for request in orders.values():
            if key == request['customer_id']:
                tot_orders += request['total']
                num_orders += 1
                customer_list[key] = {'name': value['name'],
                                      'email': value['email'],
                                      'orders': num_orders,
                                      'total': tot_orders}
    return customer_list
