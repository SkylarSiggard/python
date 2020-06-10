#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    #lesser_of_two_evens(2,4) --> 2
    #lesser_of_two_evens(2,5) --> 5
#! My Answers
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print("{} is even and greater".format(a))
        else:
            print("{} is even and greater".format(b))
    elif a % 2 != 0 and b % 2 != 0:
        if a > b:
            print("{} is odd and greater".format(a))
        else:
            print("{} is odd and greater".format(b))
    else:
        if a > b:
            print("numbers are mixed but {} is greater".format(a))
        else:
            print("numbers are mixed but {} is greater".format(b))   
lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

#* their answers:
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
#! My Answers
def animal_crackers(text):
    t = text.split()
    if t[0][0] == t[1][0]:
        print(True)
    else:
        print(False)
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

#* their answers:
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
#! My Answers
def makes_twenty(n1,n2):
    num = n1 + n2
    if n1 == 20 or n2 == 20:
        print(True, 'first')
    else:
        if num == 20:
            print(True, 'second')
        else:
            print(False, 'third')
makes_twenty(20,10)
makes_twenty(2,3)

#* their answers:
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'
#! My Answers
def old_macdonald(name):
    index = 0
    mystring = []
    for i in name:
        if index == 0:
            mystring.append(i.upper())
        elif index == 3:
            mystring.append(i.upper())
        else: 
            mystring.append(i)
        index = index + 1
    print(''.join(mystring))
    
#* their answers:
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


#MASTER YODA: Given a sentence, return a sentence with the words reversed¶
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
#Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
#>>> "--".join(['a','b','c'])
#>>> 'a--b--c'
#This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
#>>> " ".join(['Hello','world'])
#>>> "Hello world"
#! My Answers
def master_yoda(text):
    t = text.split()
    r = t[::-1]
    print(' '.join(r))
master_yoda('I am home')
master_yoda('We are ready')

#* their answers:
def master_yoda(text):
    return ' '.join(text.split()[::-1])

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a number
#! My Answers
def almost_there(n):
    if n >= 90 and n <= 110 or n >= 190 and n <= 210:
        print(True)
    else:
        print(False)
almost_there(104)
almost_there(150)
almost_there(209)

#* their answers:
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#FIND 33:¶
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False
#! My Answers
def has_33(nums):
    index = 1
    for i in nums:
        if index == len(nums):
            print("done")
        else:
            if i == nums[index]:
                print(True)
            else:
                print(False)
        index += 1
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

#* their answers:
def has_33(nums):
    for i in range(0, len(nums)-1):
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
#! My Answers
def paper_doll(text):
    t = list(text)
    newStr = []
    for i in t:
        newStr.append(i * 3)
    print(''.join(newStr))
paper_doll('Hello')
paper_doll('Mississippi')

#* their answers:
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19
#! My Answers
def blackjack(a,b,c):
    theSum = a + b + c
    if theSum <= 21:
        print("the sum is:", theSum)
    else:
        if a == 11 or b == 11 or c == 11:
            newSum = theSum - 11
            if newSum > 21:
                print('BUST')
            else:
                print("the sum is:", newSum)
        else:
            print("BUST")
blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

#* their answers:
def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14
#! My Answers
def summer_69(arr):
    numSum = []
    stopper = True
    for i in arr:
        if i == 6:
            stopper = False
        elif i == 9:
            stopper = True
        else:
            if stopper == True:
                numSum.append(i)
            else: 
                pass
    print(sum(numSum))
summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])

#* their answers:
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
#! My Answers
def spy_game(nums):
    index = 0
    jamesBond = bool
    for i in nums:
        if i == 0 and nums[index + 1] == 0 and nums[index + 2] == 7:
            jamesBond = True
        else:
            if jamesBond == True:
                pass
            else:
                jamesBond = False
        index += 1
        if index > len(nums):
            index = 0
    print(jamesBond)
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])

#* their answers:
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
    return len(code) == 1

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.
#! My Answers
def count_primes(num):
    count = []
    for i in range(1, num +1):
        if i % 2 == 0:
            count.append(i)
        else:
            pass
    print(len(count))
count_primes(100)

#* their answers:
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
#* and another way of doing it:
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


#Just for fun:¶
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#print_big('a')
#
#out:   *  
#      * *
#     *****
#     *   *
#     *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".
#! My Answers
def print_big(letter):
    alf = {'a':['  *  ', ' * * ', '*****', '*   *', '*   *'], 'b': ['**** ','*   *','**** ','*   *','**** ']}
    for i in alf:
        if i == letter.lower():
            print('{a}\n{b}\n{c}\n{d}\n{e}'.format(a=alf[letter][0],b=alf[letter][1],c=alf[letter][2],d=alf[letter][3],e=alf[letter][4]))
print_big('b')

#* their answers:
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

