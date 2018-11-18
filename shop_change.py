amount = 1001
change = 0
notes=[1,10,100]
change_tally = [0,0,0]
while amount>0:
    print(amount)
    if (amount>=100):
        amount = amount - 100
        change_tally[2] +=1
        continue
    if (amount>=10):
        amount = amount - 10
        change_tally[1] +=1
        continue
    if (amount>=1):
        amount = amount - 1
        change_tally[0] +=1
        continue
print(change_tally)