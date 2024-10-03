import random
num1 = None
num2 = None
res =  None
pre = None

def gennu(num1, num2):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    return num1, num2


def preguntar(num1, num2, res, pre):

    res = num1 * num2
    print("¿Cuanto es ",num1," X ",num2,"?")
    pre = int(input())

    return num1, num2, res, pre


def verficar(num1, num2, res, pre):
    if pre == res:
        print("Bien")

    else:
        print("Está mal, porque", num1, "X", num2, "es", res)


while(__name__ == "__main__"):
    num1, num2 = gennu(num1, num2)
    num1, num2, res, pre = preguntar(num1, num2, res, pre)
    verficar(num1, num2, res, pre)



