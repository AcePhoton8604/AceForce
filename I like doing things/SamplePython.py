#vital online compiler: https://www.onlinegdb.com/online_python_compiler
#next time: https://www.w3schools.com/python/python_datatypes.asp
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
    a = """What is quantum physics? Put simply, it’s the physics that explains how everything works: the best description we have of the nature of the particles that 
    make up matter and the forces with which they interact. Quantum physics underlies how atoms work, and so why chemistry and biology work as they do. You,
     me and the gatepost – at some level at least, we’re all dancing to the quantum tune. If you want to explain how electrons move through a computer chip, 
     how photons of light get turned to electrical current in a solar panel or amplify themselves in a laser, or even just how the sun keeps burning, you’ll need to use 
     quantum physics. The difficulty – and, for physicists, the fun – starts here. To begin with, there’s no single quantum theory. There’s quantum mechanics, the basic 
     mathematical framework that underpins it all, which was first developed in the 1920s by Niels Bohr, Werner Heisenberg, Erwin Schrödinger and others. It 
     characterises simple things such as how the position or momentum of a single particle or group of few particles changes over time. But to understand how things
     work in the real world, quantum mechanics must be combined with other elements of physics – principally, Albert Einstein’s special theory of relativity, which 
     explains what happens when things move very fast – to create what are known as quantum field theories. Three different quantum field theories deal with three of 
     the four fundamental forces by which matter interacts: electromagnetism, which explains how atoms hold together; the strong nuclear force, which explains the 
     stability of the nucleus at the heart of the atom; and the weak nuclear force, which explains why some atoms undergo radioactive decay. Over the past five decades
      or so these three theories have been brought together in a ramshackle coalition known as the “standard model” of particle physics. For all the impression that this
    model is slightly held together with sticky tape, it is the most accurately tested picture of matter’s basic working that’s ever been devised. Its crowning glory came in
     2012 with the discovery of the Higgs boson, the particle that gives all other fundamental particles their mass, whose existence was predicted on the basis of 
     quantum field theories as far back as 1964. Conventional quantum field theories work well in describing the results of experiments at high-energy particle smashers
     such as CERN’s Large Hadron Collider, where the Higgs was discovered, which probe matter at its smallest scales. But if you want to understand how things work in
     many less esoteric situations – how electrons move or don’t move through a solid material and so make a material a metal, an insulator or a semiconductor, for 
     example – things get even more complex. The billions upon billions of interactions in these crowded environments require the development of “effective field
      theories” that gloss over some of the gory details. The difficulty in constructing such theories is why many important questions in solid-state physics remain 
      unresolved – for instance why at low temperatures some materials are superconductors that allow current without electrical resistance, and why we can’t get this
     trick to work at room temperature. But beneath all these practical problems lies a huge quantum mystery. At a basic level, quantum physics predicts very strange 
     things about how matter works that are completely at odds with how things seem to work in the real world. Quantum particles can behave like particles, located in
      a single place; or they can act like waves, distributed all over space or in several places at once. How they appear seems to depend on how we choose to measure
      them, and before we measure they seem to have no definite properties at all – leading us to a fundamental conundrum about the nature of basic reality.
    This fuzziness leads to apparent paradoxes such as Schrödinger’s cat, in which thanks to an uncertain quantum process a cat is left dead and alive at the same time.
    But that’s not all. Quantum particles also seem to be able to affect each other instantaneously even when they are far away from each other. This truly bamboozling
    phenomenon is known as entanglement, or, in a phrase coined by Einstein (a great critic of quantum theory), “spooky action at a distance”. Such quantum powers
    are completely foreign to us, yet are the basis of emerging technologies such as ultra-secure quantum cryptography and ultra-powerful quantum computing. But as
    to what it all means, no one knows. Some people think we must just accept that quantum physics explains the material world in terms we find impossible to square
    with our experience in the larger, “classical” world. Others think there must be some better, more intuitive theory out there that we’ve yet to discover. In all this,
    there are several elephants in the room. For a start, there’s a fourth fundamental force of nature that so far quantum theory has been unable to explain. Gravity 
    remains the territory of Einstein’s general theory of relativity, a firmly non-quantum theory that doesn’t even involve particles. Intensive efforts over decades to bring
    gravity under the quantum umbrella and so explain all of fundamental physics within one “theory of everything” have come to nothing. Meanwhile cosmological 
    measurements indicate that over 95 per cent of the universe consists of dark matter and dark energy, stuffs for which we currently have no explanation within the 
    standard model, and conundrums such as the extent of the role of quantum physics in the messy workings of life remain unexplained. The world is at some level 
    quantum – but whether quantum physics is the last word about the world remains an open question.

Source: https://www.newscientist.com/definition/quantum-physics/
"""
 
    print(a) 
strings()





