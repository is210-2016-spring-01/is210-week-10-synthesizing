#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a database"""


def sum_orders(customers, orders):
    """Sum of customers and their orders.

    Args:
        customers (dict): A dictionary of customer keyed by customer_id
        orders (dict): A dictionary of orders keyed by order_id

    Returns:
        dict: Combined dictionaries using order values to create total.

    Examples

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
    customers_orders = {}
    for cust_key, cust_val in customers.iteritems():
        orders_tot = 0
        orders_amt = 0
        for order_key in orders.values():
            if cust_key == order_key['customer_id']:
                orders_tot += order_key['total']
                orders_amt += 1
                customers_orders[cust_key] = {'name': cust_val['name'],
                                              'email': cust_val['email'],
                                              'orders': orders_amt,
                                              'total': orders_tot}
    return customers_orders
