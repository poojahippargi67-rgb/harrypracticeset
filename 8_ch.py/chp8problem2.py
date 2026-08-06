def f_to_c(f):
    return 5 * (f - 32) / 9

f = float(input("Enter temperature in F: "))
print(f"{f_to_c(f):.2f}")