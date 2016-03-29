#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 10 synthesizing task that combines dictionaries."""


def sum_orders(customers, orders):
    """ Combines the two passed datasets and, based on customer id, and return
        a single dictionary.

    ARGS:
        customers (dict): A dictionary of customers keyed by customer_id.
        orders (dict): A dictionary of orders keyed by order id.

    RETURNS:
        dict: key: customer id, with name, email, orders (number of), and
                total (sum or orders)

    EXAMPLE:
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
    combined = {}                           # initialize new dictionary

    for ordinfo in orders.itervalues():

        cnum = ordinfo.get('customer_id')   # get customer number for order

        if cnum not in combined:            # first order for the customer?

            if cnum in customers:           # verify customer in dictionary
                combined[cnum] = {'name': customers[cnum]['name'],
                                  'email': customers[cnum]['email']}
            else:                           # otherwise unknown customer
                combined[cnum] = {'name': 'unknown', 'email': 'unknown'}

            combined[cnum]['orders'] = 0    # intialize number of orders
            combined[cnum]['total'] = 0     # initialize total of orders

        combined[cnum]['orders'] += 1       # bump count of orders
        combined[cnum]['total'] += ordinfo['total']     # and add to total

    return combined
