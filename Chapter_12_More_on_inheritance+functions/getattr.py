class PC:
    processor = "ryzen 5"

m = PC()
x = getattr(m, 'processor')
print(x)