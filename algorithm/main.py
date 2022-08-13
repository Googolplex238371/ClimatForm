def change(change):
  denoms = [25,10,5,1]
  x = change
  coins = 0
  for i in denoms:
    if x < i:
      pass
    else:
      a = (x - x%i)/i
      x = a
      coins = coins + 1
  return coins
