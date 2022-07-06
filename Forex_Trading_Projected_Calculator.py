initial=150.07
x = 1
lotsize=0
lotsizes =[]
money=[]

def profit_1():
  z = lotsize*30
  y = lotsize*80
  profit_1_ko = y-z
  return profit_1_ko


while (x < 128):
  lotsizez= initial/850
  lotsize = round(lotsizez, 2)
  lotsizes.append(lotsize)
  initial += profit_1()
  money.append(initial)
  x=x+1


print(lotsizes)
print(initial)
#print(money)
