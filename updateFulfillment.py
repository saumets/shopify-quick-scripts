#!/usr/bin/env python
# coding=utf-8

# Quick and dirty script to update fulfillment_service value on all products

import shopify
import config

def update_products():
    products = shopify.Product.find(limit=250)

    for product in products:
        if len(product.variants) < 1:
            print("[error]: no product variants found!")
        else:
            for variant in product.variants:
                variant.fulfillment_service = "manual"

        product.save()
        if product.errors:
            for message in product.errors.full_messages():
                print("[ERROR] {0}".format(message))
            return


print("Updating fulfillment settings for all products...")
update_products()
print("Process Complete.")
