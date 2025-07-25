import math

print("Welcome to the World!")

#1
print(5 * (3+6))

#2
print((3 - 12.8) / (4.8**(1/3) - 1))

#3 
print(3 + math.exp(3.62))

#4
math.sqrt(4.1 + (math.log(6))**3)

#5
math.sin(2 * math.pi)

#6
math.sin(math.radians(360))

h = 16.20
r = 1.80/2
rho = 2.30*1000

# calculate the volume
vol = math.pi*r**2*h

# calculate the mass
mass = vol*rho

#display results
print(f'the volume is {vol:.2f}')
print(f"the mass is {mass:.2f}")
