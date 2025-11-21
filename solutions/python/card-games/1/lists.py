def get_rounds(number):
    return [number,number+1,number+2]
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2
def list_contains_round(rounds, number):
    #for r in rounds:
    #    if r == number:
    #        return True
    #return False
    return number in rounds
def card_average(hand):
    count=0
    sum=0
    for i in hand:
        count+=1
        sum+=i
    return sum/count

def approx_average_is_average(hand):
    count=0
    sum=0
    for i in hand:
        count+=1
        sum+=i
    b=sum/count
    a=(hand[0]+hand[-1])/2
    if a==b:
        return True
    elif hand[len(hand)//2]==b:  #n/2+1
        return True
    else:
        return False

def average_even_is_average_odd(hand):
    odd=[]
    even=[]
    os=0
    es=0
    oc=0
    ec=0
    for idx,val in enumerate(hand):
        if idx%2==0:
            even.append(val)
        else:
            odd.append(val)
    for j in even:
        es+=j
        ec+=1     
    ef = es / ec if ec != 0 else 0

    for k in odd:
        os+=k
        oc+=1
    of = os / oc if oc != 0 else 0
    return ef == of
def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]*=2
    return hand
    
