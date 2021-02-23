# N student take k apples and distributor them among each other evenly.
# The remaning the undiisible part remains in the basket. how many apples will each single student get?
# how many apples will remain in the basket? the program reads the no N and K .
# It should print the two ans
n = int(input ("how many apples :-"))
k = int(input ("how many students :-"))
remaning = n/k
get = n%k
print(f"each student will get {remaning}")
print(f"{get} will remain in the basket")

