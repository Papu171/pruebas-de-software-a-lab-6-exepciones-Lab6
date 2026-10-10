class MyException(Exception):
    pass


class ExceptionsDemo:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("ZeroDivisionError Detected: no se puede dividir entre cero")
        except TypeError:
            print("TypeError Detected: los operandos deben ser numeros")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("IndexError Detected: indice fuera de rango")
        except TypeError:
            print("TypeError Detected: no es una lista valida o el indice no es entero")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print(f"KeyError Detected: la llave '{key}' no existe")
        except TypeError:
            print("TypeError Detected: el objeto no es un diccionario")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f"FileNotFoundError Detected: el archivo '{filename}' no existe")
        except PermissionError:
            print(f"PermissionError Detected: sin permisos para leer '{filename}'")
        except OSError as e:
            print("OSError Detected:", e)

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("AttributeError Detected: el objeto no tiene ese atributo")

    def check_positive(self, number):
        if number < 0:
            raise MyException("The number must be positive.")
        else:
            print("Valid number:", number)


if __name__ == "__main__":

    demo = ExceptionsDemo()

    demo.divide(10, 0)
    demo.divide("10", 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())

    try:
        demo.check_positive(-5)
    except MyException as e:
        print("Custom error:", e)