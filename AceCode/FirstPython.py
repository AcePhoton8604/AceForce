#next time: https://www.w3schools.com/python/python_strings_format.asp
x = "So I have started learning python. Huzzah for me!"
print(x)
print ("potato")
# This is a python comment
" " "One could leave comments like this too, since python only reads it but without a variable assigned doesn't execute(thing) it" " "
def variables():
      xa = str(3)
      xb = int(3)
      xc = float(3)
      print(xa)
      print(xb)
      print(xc)#next time: https://www.w3schools.com/python/python_operators.asp
x = "So I have started learning python. Huzzah for me!"
print(x)
print ("potato")
# This is a python comment
" " "One could leave comments like this too, since python only reads it but without a variable assigned doesn't execute(thing) it" " "
def variables():
      xa = str(3)
      xb = int(3)
      xc = float(3)
      print(xa)
      print(xb)
      print(xc)
      print (type(xa))
      print (type(xb))
      print (type(xc))
      aa, ab, ac = 1, 2, 3
      print (aa,ab,ac)
variables()
def unpacking():
      flavors = ["blueberry", "strawberry", "cheese", "chocolate", "litchi"]
      o, p, q, r, s = flavors
      print(o, p , q, r, s + "are my favorite flavors in order from first to fifth")
unpacking()
def outstate():
      s1 = "Python is"
      s2 = " epic "
      s3 = "and no this is not part of "
      s4 =" me practising tutorials, python is really legitimately"
      s5 = s1+s2+s3+s4+s2
      print(s5)
outstate()
def functionq():
      w = "coll"
      global vry
      vry = "very, very"
      print("Functions are "+ w)
functionq()
def datatypes():
      q1  = str("Hello Y'all") #string
      q2  = int(20) # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
      q3  = float(20.5) # Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 
                          # Float can also be scientific numbers with an "e" to indicate the power of 10.
      q4  = complex(1j) # Complex numbers are written with a "j" as the imaginary part.
      q5  = list(("apple", "banana", "cherry"))
      q6  = tuple(("apple", "banana", "cherry"))
      q7  = range(6)
      q8  = dict(name="John", age=36)
      q9  = set(("apple", "banana", "cherry"))
      q10 = frozenset(("apple", "banana", "cherry"))
      q11 = bool(5)
      q12 = bytes(5)
      q13 = bytearray(5)
      q14 = memoryview(bytes(5))
      print (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14)
      #convert Float Int and Complex files into other forms
      a = float(q2)
      b = int (q3)
      c = complex (q2)
      print (a,b,c)
      #Random numbers!!
      import random
      print (random.randrange(0,99999999999999999999999999999999999999999999999999999999999999999999))
datatypes()
def casting():
      x = int(1)   
      y = int(2.8)
      z = int("3")
      w = float("4.2")
      v = str(3.0)
      print (x,y,z,w,v)
casting()
def strings():
    a = """       What is quantum physics? Put simply, it’s the physics that explains how everything works: the best description we have of the nature of the particles that 
    make up matter and the forces with which they interact. 

Source: https://www.newscientist.com/definition/quantum-physics/
"""
    b = "Good day to everyone who's doing coding in their free time."
    print(a.strip())
    print(b[0:58])
    def stringlogic():
      for c in "Blueberries are epic":
            print(c)   
      if "quantum" in a :
            print(len(a))
            print ("Quantum mechanics is cool".lower())
      else :   #Also, <if "quantum" not in a:>
        print( "quantum mechanics is still cool".upper())
        print(a.replace("quantum","Quantum"))
        print (a.replace(b))
        stringlogic()
        print("HALLO")
strings()
def formathod():
      quantity = 3
      itemno = 567
      price = 49.95
      myorder = "I want {} pieces of item {} for {} dollars."
      print(myorder.format(quantity, itemno, price))
formathod()
print("""



""")
def escapechar():
      txt = "We are the so-called \"Potatoes\" from the north."
      print(txt)
escapechar()
print("This is important: https://www.w3schools.com/python/python_strings_methods.asp")
def BooleansInFunction():
      print("\n\n\n\n\n")
      print(10 > 9)
      print(10 == 9)
      print(10 < 9)
      a = 2000000000000000000000
      b = 20000000000000000000000
      if b > a:
            print("b is greater than a")
      else:
            print("b is not greater than a")
      print(bool("erm"))
BooleansInFunction()
def aFunction() :
      return True
      x = 200
      print(isinstance(x, int))
print(aFunction())


      print (type(xa))
      print (type(xb))
      print (type(xc))
      aa, ab, ac = 1, 2, 3
      print (aa,ab,ac)
variables()
def unpacking():
      flavors = ["blueberry", "strawberry", "cheese", "chocolate", "litchi"]
      o, p, q, r, s = flavors
      print(o, p , q, r, s + "are my favorite flavors in order from first to fifth")
unpacking()
def outstate():
      s1 = "Python is"
      s2 = " epic "
      s3 = "and no this is not part of "
      s4 =" me practising tutorials, python is really legitimately"
      s5 = s1+s2+s3+s4+s2
      print(s5)
outstate()
def functionq():
      w = "coll"
      global vry
      vry = "very, very"
      print("Functions are "+ w)
functionq()
def datatypes():
      q1  = str("Hello Y'all") #string
      q2  = int(20) # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
      q3  = float(20.5) # Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 
                          # Float can also be scientific numbers with an "e" to indicate the power of 10.
      q4  = complex(1j) # Complex numbers are written with a "j" as the imaginary part.
      q5  = list(("apple", "banana", "cherry"))
      q6  = tuple(("apple", "banana", "cherry"))
      q7  = range(6)
      q8  = dict(name="John", age=36)
      q9  = set(("apple", "banana", "cherry"))
      q10 = frozenset(("apple", "banana", "cherry"))
      q11 = bool(5)
      q12 = bytes(5)
      q13 = bytearray(5)
      q14 = memoryview(bytes(5))
      print (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14)
      #convert Float Int and Complex files into other forms
      a = float(q2)
      b = int (q3)
      c = complex (q2)
      print (a,b,c)
      #Random numbers!!
      import random
      print (random.randrange(0,99999999999999999999999999999999999999999999999999999999999999999999))
datatypes()
def casting():
      x = int(1)   
      y = int(2.8)
      z = int("3")
      w = float("4.2")
      v = str(3.0)
      print (x,y,z,w,v)
casting()
def strings():
    a = """       What is quantum physics? Put simply, it’s the physics that explains how everything works: the best description we have of the nature of the particles that 
    make up matter and the forces with which they interact. 

Source: https://www.newscientist.com/definition/quantum-physics/
"""
    b = "Good day to everyone who's doing coding in their free time."
    print(a.strip())
    print(b[0:58])
    def stringlogic():
      for c in "Blueberries are epic":
            print(c)   
      if "quantum" in a :
            print(len(a))
            print ("Quantum mechanics is cool".lower())
      else :   #Also, <if "quantum" not in a:>
        print( "quantum mechanics is still cool".upper())
        print(a.replace("quantum","Quantum"))
        print (a.replace(b))
        stringlogic()
        print("HALLO")
strings()
def formathod():
      age = 8604
      txt = "My name is AcePhoton, and I am {}"
      print(txt.format(age))
formathod()






