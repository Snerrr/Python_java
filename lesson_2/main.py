import hot_water
import hot_water_vending_machin

a = hot_water.Hot_water("Cola", 55, 0.5, 10)
b = hot_water.Hot_water("Cofe", 99, 0.1, 70)
c = hot_water_vending_machin.Hot_water_vending_machin([a, b])
print(c.getProduct("Cola",10,0.5))
print(c.getProduct("Cofe",70,0.1))
print(c.getProduct("Cola3",101,0.5))
