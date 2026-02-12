import math

P = input("podaj kapital poczatkawy     ")
P = int(P)

R = input("podaj oprocentowanie roczne      ")
R = int(R)
r = R / 100

t = input("podaj czas w latach      ")
t = int(t)

A = P * math.exp(r * t)

print(A)