import random
def basketball(p):
    shot_made=False
    davis=False
    lebron=False
    possession=random.randint(1,2)
    if possession==1:
        lebron=True
    else:
        davis=True
    while shot_made==False:
        shot_counter=random.randint(1,2)
        if lebron==True:
            if shot_counter==1:
                return(True)
            else:
                davis=True
                lebron=False
        elif davis==True:
            steal_chance=random.random()
            if steal_chance<=p:
                davis=False
                lebron=True
            elif shot_counter==1:
                return(False)

lebron_wins=0
davis_wins=0
for i in range(1000000):
    x=basketball(.333333)
    if x==True:
        lebron_wins+=1
    else:
        davis_wins+=1
print('lebron wins', lebron_wins, 'times')
print('davis wins', davis_wins, 'times')
