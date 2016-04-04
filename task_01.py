#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: """


import data

CUSTOMERS = data.CUSTOMERS
ORDERS = data.ORDERS


def sum_orders(customers, orders):
    """takes 2 dict params, combines into
    single dict with inner dict, return combined dict"""
    if not customers:
        customers = CUSTOMERS
    if not orders:
        orders = ORDERS
    order_up = {}
    for key, value in customers.iteritems():
        orderinos = 0
        numbah = 1
        for order_id in orders.values():
            if key == (order_id['customer_id']):
                order_up[key] = {'name': value['name'], 'email': value['email'],
                                 'orders': numbah, 'total': orderinos}
                orderinos += order_id['total']
                numbah += 1
    return order_up
