# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 13:51:26 2016

@author: parattan
"""

#python exercises 
#1. 
def max(a, b):
    if(a>=b): 
        return a
    else: 
        return b

max(2,3) 

#2.
def max_of_three(a, b, c): 
    if(a>=b and a>c): 
        return a
    elif(b>=a and b>c): 
        return b
    else: 
        return c

max_of_three(2,3,4)
max_of_three(2,3,3)
max_of_three(3,3,2)

#3.
def str_len(s): 
    count = 0 
    for c in s: 
        count = count +1
    return count 

str_len("Apeejay")
str_len("")
str_len(" ")

#4.
def is_vowel(c):
    if(c in ('a', 'e','i', 'o', 'u')): 
        return True 
    else: 
        return False 

is_vowel('p')
is_vowel('a')
is_vowel('')

#5.
def translate(s): 
    if(len(s)==0):
        return s
    r1 = ""
    for c in s: 
        if(c == " " or is_vowel(c)):
            r1 = r1+c
        else:
            r1 = r1+c+'o'+c
    return r1
    #l = len(r1)
    #mid_point = l/2
    #r2 = r1[0:mid_point]+'o'+r2[mid_point:]
    #return r2 
    
translate("this is fun") == "tothohisos isos fofunon"

#6. 
def sum_f(lst): 
    s = 0 
    for l in lst: 
        s = s+l
    return s

def multiply_f(lst): 
    p = 1
    for l in lst: 
        p = p*l
    return p 
    
sum_f([1, 2, 3, 4])
multiply_f([1, 2, 3, 4])

#7. 
def reverse(s):
    r = ""
    for i in range(len(s)-1, -1, -1): 
        #print i 
        r = r+s[i] 
    return r 

reverse("This is a test")

#8. 
def is_palindrome(s):
    s = s.lower()
    result = True 
    for i in range(0, len(s)-1): 
        if(s[i]!=s[len(s)-1-i]): 
            result = False 
            break 
    return result 

is_palindrome("radar") == True

#9. 
def is_member(x,a):
    result = False 
    for l in a: 
        if(x==l): 
            result = True 
    return result 
    
is_member(1, [1,2,3,4]) == True
is_member(5, [1,2,3,4]) == False
is_member('a', ['a','b','c',1]) == True
is_member('x', ['a','b','c',1]) == False

#10.
def overlapping(lst1, lst2):
    result = False 
    for l1 in lst1: 
        for l2 in lst2: 
            if (l1==l2): 
                result = True 
                break 
    return result 
    
overlapping([1,2,3], [5,6,7,8,9]) == False 
overlapping([1,2,3], [5,6,1,7,8,9]) == True 
overlapping([1,2,3], [5,6,1,1,8,9]) == True  
overlapping([1,2,3], [5,6,1,2,8,9]) == True 

#11. 
def  generate_n_chars(times, c): 
    s= ""
    for i in range(0,times): 
        s = s+c
    return s
    
generate_n_chars(5,'c')

#12. 
def histogram(lst): 
    for l in lst: 
        print l*'*'

histogram([4, 9, 7])   

#13. 
def max_in_list(lst): 
    max = 0 
    for l in lst: 
        if(l>=max): 
            max = l 
    return max 
    
max_in_list([2,88,100,5,66])

#14. 
def map_len(lst): 
    len_dict = {}
    for l in lst:
        len_dict[l] = len(l)
    return len_dict

print map_len(["paavni", "anee", "rattan", "sood"])

#15. 
def find_longest_word(lst): 
    max = 0 
    longest_word = ""
    for l in lst: 
        if(len(l)>max): 
            max = len(l)
            longest_word = l
    return longest_word 
    
print find_longest_word(["paavni", "aneesh", "rattan", "sood"])

#16.
def filter_long_words(lst, n): 
    long_words = []
    for l in lst: 
        if(len(l)>=n): 
            long_words.append(l)
    return long_words 

print filter_long_words(["paavni", "anee", "rattan", "sood"], 5)

#17 
import re 
def palindrome_s(s): 
    s = s.lower()
    s = re.sub('[^a-zA-Z]+', '', s)
    if( is_palindrome(s)==True): 
        return True 
    else: 
        return False 

palindrome_s("Go hang a salami I'm a lasagna hog.") == True 
palindrome_s("No, not a palindrome!!") == False 


#18.
import string  
def pangram(s): 
    result = True 
    s = s.lower()
    alphabets = string.ascii_lowercase
    for a in alphabets:
        if(not s.find(a)>=0): 
            result = False 
            break
    return result
        
print pangram("The quick brown fox jumps over the lazy dog")
print pangram("abcdef")
print pangram("")

#19. 
def print_99_Bottles_of_Beer(): 
    for i in range(99,1, -1): 
        s = str(i) +" bottles of beer on the wall, " + str(i) +" bottles of beer. \n Take one down, pass it around, " + str(i-1) + " bottles of beer on the wall. \n"
        print s
        
    print "1 bottle of beer on the wall, 1 bottle of beer. \n Take one down and pass it around, no more bottles of beer on the wall. \n"
    print "No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall."
print_99_Bottles_of_Beer()

#20. 
def translate_swedish(text): 
    lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} 
    text = text.lower()
    text = text.split()
    translation = ""
    for t in text: 
        print t
        translation = translation+ " "+lexicon.get(t, "")
    return translation

print translate_swedish("Merry Christmas and happy new year")
        
#21.
def  char_freq(s): 
    freq_table = {}
    for c in s: 
        freq_table[c] = freq_table.get(c,0)+1
    return freq_table

print char_freq("abbabcbdbabdbdbabababcbcbab")

#22.
def caesar_cipher(s): 
    key_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    result = ""
    for c in s: 
        if(c==" "): 
            result = result+c
        else: 
            result = result+key_dict.get(c, c)
    return result 

print caesar_cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")

#23.
import re
def correct(s): 
    s = re.sub('[\s]+', "\s", s)
    s = re.sub('[.^\s]', ".\s", s)
    return s
correct("This   is  very funny  and    cool.Indeed!")

#24.
def make_3sg_form(w): 
    #endswith()
    l = len(w)
    if(w[-1:]=="y"): 
        sg3 = w[:l-2]+"ies"
    elif(w[-2:] in ("ch", "sh") or w[-1:] in ("o", "s", "x", "z")):
        sg3 = w+"es"
    else: 
        sg3 = w+"s"
    return sg3 

print make_3sg_form("try")
print make_3sg_form("brush")
print make_3sg_form("run")
print make_3sg_form("fix")

#25.
def make_ing_form(w):
    l = len(w)
    exception_list = ["be", "see", "flee", "knee"]
    if(w.endswith("e") and not w.endswith("ie") and not (w in exception_list)): 
        ing_form = w[:l-1]+"ing"
        print w + " 1st block"
    elif(w.endswith("ie")): 
        ing_form = w[:l-2]+"ying"
        print w + " 2nd block"
    elif(not is_vowel(w[-3]) and is_vowel(w[-2]) and not is_vowel(w[-1])): 
        ing_form = w +w[-1:]+"ing" 
        print w + " 3rd block"
    else: 
        ing_form = w+"ing"
        print w + " last block"
    return ing_form


print make_ing_form("lie")
print make_ing_form("see")
print make_ing_form("move")
print make_ing_form("hug")

#26. 
def max_in_list(lst): 
    m = reduce(max, lst) 
    return m 

max_in_list([10, 81, 9, 54, 72])

#27.
def map_word_len_a(wlst): 
    mwl = []
    for w in wlst: 
        mwl.append(len(w))
    return mwl
    
def map_word_len_b(wlst): 
    mwl = map(len, wlst)
    return mwl
    
def map_word_len_c(wlst): 
    mwl = [len(w) for w in wlst]
    return mwl
wlst = ["paavni", "aneesh", "rattan", "sood"]

#28. 
def find_longest_word(wlst): 
    mwl = map(len,wlst)
    wl =max(mwl)
    return wl
find_longest_word(wlst)

#29.
def filter_long_words(wlst, n):
    longwl = filter(lambda x: len(x)>=n, wlst)

    return longwl
filter_long_words(wlst, 5)

#30.
def translate(s): 
    wlst = s.lower()
    wlst = wlst.split()
    lexicon = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} 
    t = map(lambda x: lexicon.get(x, "") , wlst)
    return " ".join(t) 

print translate("Merry Christmas and happy new year")

#31.
def mymap(f, x):
    r = []
    for c in x: 
        r.append(f(c))
    return r

def myreduce(f,x):
    l = []
    for c in x: 
        l.append(c) 
        r = f(l)
    return r
    
def myfilter(f, x):
    r = []
    for c in x: 
        if(f(c)==True): 
            r.append(c)
    return r
    
#32. 
def print_palindromes(): 
    fn = input("Enter the file name: ")
    f = open(fn)
    for line in f: 
        if(palindrome_s(line)): 
            print line 
    f.close()
        
print_palindromes()
"C:\Users\parattan\Documents\print_palindromes_test.txt"

#33.
def semordnilap():
    l = []
    fn = input("Enter the file name: ")
    f1 = open(fn)
    for line in f1:
        for word in line.split(): 
            l.append(word[::-1].lower())
    f2 = open(fn)
    for line in f2:
        for word in line.split(): 
            if(word.lower() in l):
                l.remove(word[::-1])
                print word + " " + word[::-1]
    f1.close()
    f2.close()
                
semordnilap()
"C:\Users\parattan\Documents\print_semordnilap_test.txt"

#34.
def char_freq_table(): 
    freq_table = {}
    fn = input("Enter the file name: ")
    f = open(fn)
    for line in f: 
        for word in line.split(): 
            for character in word: 
                freq_table[character] = freq_table.get(character, 0) + 1
    for c in freq_table: 
        print c +"-----" + str(freq_table.get(c,0))
    f.close()

char_freq_table()
"C:\Users\parattan\Documents\print_char_freq_table_test.txt"

#35.
#import pyttsx
import time 
def speak_ICAO(fn, pause1, pause2): 
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    f = open(fn)
    for line in f: 
        for word in line.split(): 
            for character in word: 
                character = character.lower()
                print d.get(character, "") 
                time.sleep(pause1)
        time.sleep(pause2)

speak_ICAO("C:\Users\parattan\Documents\speak_ICAO_test.txt", 0.1, 1)

#36.   
def hapax(): 
    freq_table = {}
    l = []
    fn = input("Enter the file name: ")
    f = open(fn)
    for line in f: 
        for word in line.split():
            word = word.lower()
            freq_table[word] = freq_table.get(word, 0) + 1
    for w in freq_table: 
        if(freq_table.get(w) == 1): 
            l.append(w)
    f.close()
    return l
    
print hapax()
"C:\Users\parattan\Documents\print_hapax_test.txt"

#37.
def number_lines(): 
    fn = input("Enter file name: ")
    fr = open(fn)
    fw = open("write.txt", 'w')
    i = 1
    for line in fr: 
        fw.write(str(i) +": ")
        fw.write(line)
        fw.write("\n")
        i = i+1
    fr.close()
    fw.close()

number_lines()
"C:\Users\parattan\Documents\print_hapax_test.txt"

#38. 
def avg_word_length():
    fn = input("Enter file name: ")
    f = open(fn)
    len_sum = 0
    words_sum = 0
    for line in f: 
        for word in line.split():
            len_sum = len_sum + len(word)
            words_sum = words_sum+1
    return len_sum/words_sum
    
avg_word_length()
"C:\Users\parattan\Documents\print_hapax_test.txt"

#39. 
import numpy 
def guess_number(): 
    i = 0 
    n = raw_input("Hello! What is your name? ")
    print "Well, " + str(n) + ", I am thinking of a number between 1 and 20.\n"
    y = numpy.random.randint(1,20)
    while(True): 
        i = i+1
        x = input("Take a guess\n")
        if(x<y): 
            print("Your guess is too low.\n")
            continue
        elif(x>y): 
            print("Your guess is too high.\n")
            continue
        else:  
            print "Good job, " + str(n) + "! You guessed my number in " + str(i) + " guesses!"
            break
    
guess_number()

#40. 
import numpy
def anagram(low):
    rw = numpy.random.randint(0, len(low)-1)
    ow = list(low[rw])
    numpy.random.shuffle(ow)
    sw = ''.join(ow)
    print "Colour word anagram: " +sw
    while(True):
        w = raw_input("Guess the colour word! \n")
        w = w.strip()
        if(w.lower()==low[rw].lower()): 
            print "Correct!"
            break 

anagram(["Pink", "Yellow", "Orange", "Brown", "Blue"])

#41.
def lingo(wtg):
    print "-----LINGO-----"
    counter = 0 
    while(counter<=5): 
        guess = raw_input()
        guess = guess.strip()
        if(len(guess)!=5): 
            print "Enter five letter word only"
            continue
        clue = ""
        for j in range(0, len(guess)): 
            if(guess[j] in wtg): 
                if(guess[j]==wtg[j]):
                    clue = clue+"["+guess[j]+"]"
                    counter = counter+1
                else: 
                    clue = clue+"("+guess[j]+")"
            else: 
                clue = clue+guess[j]
        print "Clue: "+clue

lingo("tiger")
    
            
    