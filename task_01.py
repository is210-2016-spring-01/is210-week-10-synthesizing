#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Correlating two related data sets."""


def sum_orders(customers, orders):
    """Combines two datasets into a single dictionary keyed by customer_id.

    Args:
        customers(dict): A dictionary of customers keyed by customer_id
        orders(dict): A dictionary of orders keyed by order id

    Returns:
        combined_dict: Returns the combined dictionary

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
    combined_dict = {}
    for key in customers.iterkeys():
        num_of_orders = 0
        total_of_orders = 0
        for value2 in orders.itervalues():
            if key == value2['customer_id']:
                total_of_orders += value2['total']
                num_of_orders += 1
                combined_dict[key] = {'name': customers[key]['name'],
                                      'email': customers[key]['email'],
                                      'orders': num_of_orders,
                                      'total': total_of_orders}
    return combined_dict
