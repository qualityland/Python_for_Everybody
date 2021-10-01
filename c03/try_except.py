sh = input("Enter hours:")
sr = input("Enter rate:")
try:
    h = float(sh)
    r = float(sr)

except:
    print("Hours and rate need to be numbers.")
    quit()

p = h * r

if h > 40 :
    p = p + (h - 40) * r * 0.5

print("Pay:", p)
