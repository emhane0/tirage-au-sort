import random
import time 
bvr = 0
un = 0
deux = 0
trois = 0
quatre = 0
cinq = 0
six = 0
brr = 0
m = int(input("combien de foit veut tu lancer le dé?"))
while bvr < m:
    brg = random.randint(1, 6)
    bvr = bvr + 1
    if brg == 1:
        un = un + 1
    if brg == 2:
        deux = deux + 1
    if brg == 3:
        trois = trois + 1
    if brg == 4:
        quatre = quatre + 1
    if brg == 5:
        cinq = cinq + 1
    if brg == 6:
        six = six + 1
print("le resulta de un est", un)
print("le resulta de deux est", deux)
print("le resulta de trois est", trois)
print("le resulta de quatre est", quatre)
print("le resulta de cinq est", cinq)
print("le resulta de six est", six)
time.sleep(20.0)