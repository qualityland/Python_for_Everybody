hs = input("Enter hours:")
h = float(hs)
rt = input("Enter rate:")
r = float(rt)

p = h * r

if h > 40 :
    p = p + (h - 40) * r * 0.5

print("Pay:", p)
