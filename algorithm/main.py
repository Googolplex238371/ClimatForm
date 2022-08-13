def change():
  change = input("Enter Change Amount ")
  denoms = [25,10,5,1]
  x = int(change)
  coins = 0
  for i in denoms:
    if x < i:
      pass
    else:
      a = (x - x%i)/i
      x = x - i*a
      coins = coins + a
  print(int(coins))
change()
