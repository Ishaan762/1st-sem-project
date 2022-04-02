#1st sem project
#this code idea disbanded for OOPS logic code with same idea
import random
h_ace=s_ace=d_ace=c_ace=1
h_2=s_2=d_2=c_2=2
h_3=s_3=d_3=c_3=3
h_4=s_4=d_4=c_4=4
h_5=s_5=d_5=c_5=5
h_6=s_6=d_6=c_6=6
h_7=s_7=d_7=c_7=7
h_8=s_8=d_8=c_8=8
h_9=s_9=d_9=c_9=9
h_king=s_king=d_king=c_king=13
h_queen=s_queen=d_queen=c_queen=12
h_jack=s_jack=d_jack=c_jack=11

og_stk=[h_ace,s_ace,d_ace,c_ace,h_2,s_2,d_2,c_2,h_3,s_3,d_3,c_3,h_4,s_4,d_4,c_4,h_5,s_5,d_5,c_5,h_6,s_6,d_6,c_6,h_7,s_7,d_7,c_7,h_8,s_8,d_8,c_8,h_9,s_9,d_9,c_9,h_king,s_king,d_king,c_king,h_queen,s_queen,d_queen,c_queen,h_jack,s_jack,d_jack,c_jack,]
random.shuffle(og_stk)
stk=[]
print('Welcome to the Game')
l=5
c=0
bank=[]
while True:
    if og_stk==[]:
        print('Congratulations you win')
        print("You had",l,"lives left")
        break
    p1=0
    if len(stk)==10:
        if p1==0:
            print("You now have 10 cards, you have a choice to bank it at the cost of one life")
            print("Press Y to bank cards")
            print("Press N to continue forward without banking")
            mo=int(input())
            if mo=="Y":
                bank=list(stk)
                stk.clear()
                l=l-1
                p1=1
            elif mo=="N":
                p1=1
                continue
            else:
                print("Invlaid input")
    p2=0
    if len(stk)==20:
        if p2==0:
            print("You now have 10 cards, you have a choice to bank it at the cost of one life")
            print("Press Y to bank cards")
            print("Press N to continue forward without banking")
            mo=int(input())
            if mo=="Y":
                bank=list(stk)
                stk.clear()
                l=l-1
                p2=1
            elif mo=="N":
                p2=1
                continue
            else:
                print("Invlaid input")
    p3=0
    if len(stk)==30:
        if p3==0:
            print("You now have 10 cards, you have a choice to bank it at the cost of one life")
            print("Press Y to bank cards")
            print("Press N to continue forward without banking")
            mo=int(input())
            if mo=="Y":
                bank=list(stk)
                stk.clear()
                l=l-1
                p3=1
            elif mo=="N":
                p3=1
                continue
            else:
                print("Invlaid input")
    p4=0
    if len(stk)==40:
        if p4==0:
            print("You now have 10 cards, you have a choice to bank it at the cost of one life")
            print("Press Y to bank cards")
            print("Press N to continue forward without banking")
            mo=int(input())
            if mo=="Y":
                bank=list(stk)
                stk.clear()
                l=l-1
                p4=1
            elif mo=="N":
                p4=1
                continue
            else:
                print("Invlaid input")
    p5=0
    if len(stk)==10:
        if p5==0:
            print("You now have 10 cards, you have a choice to bank it at the cost of one life")
            print("Press Y to bank cards")
            print("Press N to continue forward without banking")
            mo=int(input())
            if mo=="Y":
                bank=list(stk)
                stk.clear()
                l=l-1
                p5=1
            elif mo=="N":
                p5=1
                continue
            else:
                print("Invlaid input")
    if c==0:
        temp=og_stk.pop(0)
        print("The card has value",temp)
        stk.append(temp)
    else:
        old=temp
        print(old)
        temp=og_stk.pop(0)
        print(temp)
        if i==1:
            if old<temp:
                print("The new card is ",temp)
                print("Success, card added to your stack")
                stk.append(temp)
            elif old==temp:
                print("The new card is ",temp)
                print("Bonus same value, card added to your stack")
                stk.append(temp)
            else:
                print("The new card is ",temp)
                print("Sorry one life lost")
                stk.clear()
                l-=1
                print(l,"lives left")
        elif i==2:
            if old>temp:
                print("The new card is ",temp)
                print("Bonus same value, card added to your stack")
                stk.append(temp)
            elif old==temp:
                print("The new card is ",temp)
                print("Bonus same value, card added to your stack")
                stk.append(temp)
            else:
                print("The new card is ",temp)
                print("Sorry one life lost and owned stack is cleared")
                stk.clear()
                l-=1
                print(l,"lives left")
    if l<=0:
        print("no more lives left you lose")
        break
    print('''Make your choice about next card
    1-Greater Value than Last card
    2-Lesser Value that last card''')
    i=int(input())
    c+=1
print("Game over")
