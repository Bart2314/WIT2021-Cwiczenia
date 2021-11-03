import time
start_time = time.time()

a = 5000000
b = 3000000

i = 1
#i = max(a,b) # max w celu oszczędności w przypadku dużych liczb (?)

while i % a != 0 or i % b != 0:
    i += 1

print("Najmniesza wspólna wielokrotnosć " + str(a) + " i " + str(b) + " to: " + str(i))

print("--- %s seconds ---" % (time.time() - start_time))