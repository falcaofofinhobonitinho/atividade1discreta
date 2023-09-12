name = "__main__"

def g(x):
  return x - 1

def f(x):
  return x ** 2

def composição(f, g, x):
  return f(g(x))

def main():
  f = input("Digite a função f(x): ")
  g = input("Digite a função g(x): ")
  x = int(input("Digite o valor de x: "))

  if isinstance(f, callable) and isinstance(g, callable):
    f = eval(f) if type(f) == str else lambda x: f
    g = eval(g) if type(g) == str else lambda x: g

    print("f(x) = ", f)
    print("g(x) = ", g)
    print("x = ", x)

    print("(g ° f)(x) = ", composição(g, f, x))
    print("(g ° g)(x) = ", composição(g, g, x))
    print("(f° f)(x) = ", composição(f, f, x))
    print("(f ° g)(x) = ", composição(f, g, x))

  else:
    print("As funções f(x) e g(x) devem ser callables.")

if name == "__main__":
  main()
