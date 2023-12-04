lv, judge = input().split()
lv = int(lv)
score = 0
if judge == "miss":
  score = 0
elif judge == "bad":
  score = 200 * lv
elif judge == "cool":
  score = 400 * lv
elif judge == "great":
  score = 600 * lv
elif judge == "perfect":
  score = 1000 * lv
print(score)