
"""
= = = = = = = = 
Richie.S 
Start 06/40/2019 


= = = = = = = = 
"""

def maintainM():
     print(MaleCalorieRecomendation)

def gainM():
     print (MaleCalorieRecomendation+200)


def cutM():
     print (MaleCalorieRecomendation-200 )

def  maintainF():
     print (FemaleCalorieCalculator)

def gainF():
     print (FemaleCalorieCalculator+200)

def cutF():
     print(FemaleCalorieCalculator-200)




def main():

     
     print ('CalorieCalculator')
     G=["M","F"]
     GENDER=input("Are you male[M] or female[F]?")
     AGE=float(input('What"s your age?'))
     WEIGHT =float(input('How much do you weigh?'))
     HEIGHT=float(input('How tall are you?'))


     WEIGHT=WEIGHT/2.2
     HEIGHT=HEIGHT*2.554
     L=['S','B','C']
     LEVEL=input("Are you Maintaining[S],bulking[B], or cutting[C]")
     FemaleCalorieCalculator= 65.1+ (9.563 * WEIGHT) + (1.850 * HEIGHT) - (4.67*AGE)
     MaleCalorieRecomendation=66.5 + (13.75 * WEIGHT) + (5.003 *HEIGHT) - (6.775 *AGE)
     for T in L:
          if LEVEL==("S"):
               maintainM()

     for T in L:
          if LEVEL==("B"):
               gainM()

     for T in L:
          if LEVEL==('C'):
               cutM()
                    

               

     for Q in G:
          if (GENDER == ("M")):
               continue
               
               
          else: FemaleCalorieCalculator

main()




 



     
