while(1):
  cnt = 0
  n = input()
  if n == '#':
    break
  for i in n:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
      cnt += 1
    elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i =='U':
      cnt += 1
  print(cnt)