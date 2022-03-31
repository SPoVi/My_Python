import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, price, items):
        self.price = price
        self.items = items
    
    def buy(self, req_items, money):
        #req_items : requestes number of items
        #monet: amount costumer puts
        self.req_items = req_items
        self.money = money
        
        cost = (self.price * self.req_items)
        # If there are enought items and costumer has sufficient money
        if  (self.items < self.req_items):
            print("Not enough items in the machines")
            raise ValueError
            
        elif (cost > self.money):
            print("Not enough coins")
            raise ValueError
        elif (self.items > self.req_items and (self.price * self.req_items) < self.money):
            self.items = self.items - self.req_items
            print (self.money - cost )
        
            
        
            
        
if __name__ == '__main__':

    num_items = 10
    item_coins = 50
    machine = VendingMachine(num_items, item_coins)

    print("\nIntroduce la cantidad a comprar:  ")
    num_items = int(input())
    print("\nIntroduce la cantidad de dinero depositado: ")
    num_coins = int(input())
    print("\nSu cambio es: ")
    change = machine.buy(num_items, num_coins)
    
