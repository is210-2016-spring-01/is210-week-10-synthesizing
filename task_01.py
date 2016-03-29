#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 doc string"""


def sum_orders(customers, orders):
    """ A function that creates a dictionary contain customer number,
        email, number of orders and order total.

    Args:
        customers (dict): Arg to be arithmetically increment with myint2.
        orders (dict): Arg to increment myint.

    Returns:
        dict:  Combined dictionary (name, email, orders, total)

    Example:
        >>> sum_orders(CUSTOMERS, ORDERS)
        {1: {'orders': 3, 'total': 1287,
             'name': 'Ekaterin Vorsoisson',
             'email': 'evorsoisson@komarr.net'},
         2: {'orders': 3, 'total': 1235,
             'name': 'Cordelia Naismith',
             'email': 'cordelia@beta.com'},
         3: {'orders': 0, 'total': 0,
             'name': 'Ivan Vorpatril',
             'email': 'iv398@barrayar.net'}}
    """
    counter = 0
    sum_total = 0
    new_total = 0
    new_dict = {}
    for cust_num, cust_data in customers.iteritems():
        for _, ord_data in orders.iteritems():
            if cust_num == ord_data['customer_id']:
                sum_total = ord_data['total']
                new_total += sum_total
                counter += 1
        customers[cust_num]['orders'] = counter
        customers[cust_num]['total'] = new_total
        if customers[cust_num]['orders'] > 0:
            new_dict.update({cust_num: cust_data})
        new_total = 0
        counter = 0
    return new_dict
