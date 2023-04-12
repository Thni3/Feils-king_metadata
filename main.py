
def sum(num1, num2, num3):
    try: return num1 +num2 +num3
    except TypeError:
        print("hei, TypeError i sum funksjonen")
    except Exception as err:
        print(f"Hei, feilen {err} har oppstått")

def multiply(num1, num2, num3):
    try: return num1 * num2 *num3
    except TypeError:
        print("hei, TypeError i multiply funksjonen")
    except Exception as err:
        print(f"Hei, feilen {err} har oppstått")

a = multiply ('5', 5, 1)
print(a)

b = sum(a, 10, 10)
print(b)
