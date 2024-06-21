from random import randint # nag import ko og randint from random kay randint man ang gamiton

print("Swertress 3D National") # Nag print ko ani kay para masayran nga Swertress kani

num1, num2, num3 = [int(input(f"ENTER NUMBER {i+1}: ")) for i in range(3)] # Mag input og tulo ka number nga 0 to 9 pero naka range siya og 3 kay 3 raman ang ge pangayo
p1, p2, p3 = [randint(0, 9) for _ in range(3)] # nag generate og randomize integer sulod sa ge input nga number 

print(f"PUSTA: {num1} {num2} {num3}") # nag print og pusta nga imong ge input atong tulo ka number nga imong ge pusta
print(f"RESULTA: {p1} {p2} {p3}") # mag print siya sa resulta nga imong ge pusta

if {num1, num2, num3} == {p1, p2, p3}: # if condition kung si pusta is same sa result
    if num1 == p1 and num2 == p2 and num3 == p3: # Kung ang tanan numero sa pusta ug resulta magkaparehas
        print("Naysss Daog Ka!") # nag print sya og Nayss daog ka if ang result is same sa imong ge pusta
    else: # else condition ang tig salo sa condition if wala nag meet
        print("Nayss Daog kas Rambol!") # Nag print sya og Nayss Daog kas Rambol if ang result og imong pusta is nag rambol
else: # else condition ang tig salo sa condition if wala nag meet
    print("Toinks Pilde Ka!") # Nag print sya og Toinkss Pilde Ka if ang Result is dili tugma sa imong ge pusta