while True:
  n = int(input())
  if n == 0:
    exit(0)
  elif n % 42 == 0:
    print("PREMIADO")
  else:
    print("TENTE NOVAMENTE")