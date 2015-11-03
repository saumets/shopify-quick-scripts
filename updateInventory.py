#!/usr/bin/env python
# coding=utf-8

# Quick and dirty script to update inventory_management, inventory_policy and inventory_quantity values on all products

import shopify
import config

___author___ = "paulsaumets"

def update_inventory():
    products = shopify.Product.find(limit=250)

    for product in products:
        if len(product.variants) < 1:
            print("[error]: no product variants found!")
        else:
            for variant in product.variants:
                variant.inventory_management = ""
                variant.inventory_policy = "continue"
                # variant.inventory_quantity = 100

        product.save()
        if product.errors:
            for message in product.errors.full_messages():
                print("[ERROR] {0}".format(message))
            return


print("Updating inventory settings for all products...")
update_inventory()
print("Process Complete.")
