# lectur workspace for 6.00 6.100L | Fall 2022 | Undergraduate
# Introduction To CS And Programming Using Python

# lecture 11
# l = [1,2,3,4]
# lcopy = l[:]
#  now we have two lists that are the same but are different objects
# print(lcopy)
l = [1,4,4]
e = 2
def remove_all(l,e): # type: ignore
    l1 = l[:]
    l.clear()
    for i in l1:
        if e != i:
            print(i)
            l.append(i)
    return l

# remove_all(l,e)
# print(a)n 
# print(l)

def remove_all(l,e):
    while e in l:
            l.remove(e) # removes the first instance of the element and has no return value
 
# remove_all(l,4)
# print(l)
# del l[0] # removes the first element and has no return value


# just removed the last element and also returned it 

def duplicate_list(l1,l2):

    for i in l1:
        l2.remove(i)
    return l2   

# l1 = [1,2,3,4]
# l2 = [1]
# l2 = duplicate_list(l1,l2)
# print(l2)










# alias


#  list that contain list itself
import copy
old = [[1,2,3],[4,5,6],[7,'hello','jaan']]

new_copy = copy.copy(old)

old.append(7)
old[1][1] = 'hello'

# print(new_copy)

# print(old)

# shallow



# deep 



# list comprehension

def f():
    listt = []
    for i in range(10):
        listt.append(i**2)

    return listt
#  here we are creating a list of list which output is a list of list
lnew = [[e,e**2] for e in range(10) if e%2 == 0]
# print(lnew )

lnew1= [len(l) for x in ['xy','abcd',7,'4.0'] if type(x) == str]
# print(lnew1)
# print(type(lnew1))
#########################

# default parameters
# include the bisection function for guessing the number

# what is the best epsilon to use for bisection search
#  we can have a default value for the epsilon
def make(a):
    def g(b):
        return a+b
    return g
# here the code calls the inner function g and returns the value of a+b ,
#  here we are chaining the value of a and then calling the inner function g

# val= make(3)(2)
dobler = make(2)
val = dobler(3)
# print(val)

#################
#lecture 13
#################

# Exception handling 

def divide_nums3():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("Could not convert to a number.")
    except ZeroDivisionError:
        print("Can't divide by zero")
        print("a/b = infinity")
        print("a+b =", a + b)
    except:
        print("Something went very wrong.")

# flag a terminal and stop the program
def sum_digits(s):
    total = 0
    for char in s:
        try :
            val = int(char)
            total += val
        except:
            raise ValueError("string contained a character")
    return total

# print(sum_digits("123"))


def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    # your code here
    # challenge: write this with list comprehension!

#     lnew  = []
#     for i in range(len(Lnum)):
#         if Ldenom[i] == 0:
#             raise ValueError("denominator is zero")
#         lnew.append(Lnum[i]/Ldenom[i])
#     return lnew

# print(pairwise_div([4,5,6],[1,2,3]))
    assert len(Lnum) == len(Ldenom), "lists are not of equal length"
    lnew = []
    lnew = [Lnum[i]/Ldenom[i] for i in range(len(Lnum)) if Ldenom[i] != 0 ] # Close the square bracket here
    return lnew

# print(pairwise_div([4,5,6],[1,2,3]))


# Assertions

def sum_digits1(s):
    assert len(s) != 0, "string is empty"
    total = 0
    for char in s:
        try :
            val = int(char)
            total += val
        except:
            raise ValueError("string contained a character")
    return total

# print(sum_digits1("123"))

# students in list of list and check the avg of student grades

test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
                [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                [['captain', 'america'], [80.0, 70.0, 96.0]],
                [['deadpool'], []]]

def get_stats(test_grades):
    new_list = []
    for i in test_grades:
        print(i)
        name = i[0]
        grades = i[1]
        # assert len(grades) != 0, "no grades data"
        print(grades)
        try :
            avg = sum(grades)/len(grades)
            print(sum(grades))
        except ZeroDivisionError:
            return 0.0
        new_list.append([name,grades,avg])
    return new_list

# print(get_stats(test_grades))

###############
# lecture 14: dictionaries 

# we wil be using list to store students name 

name= ["n","a","b"]
grades = [1,2,3]

def get_stats1(name,grades):
    list1 =[]
    for i in range(len(name)):
        list1.append([name[i],grades[i]])
    return list1

grades_students = get_stats1(name,grades)

print(grades_students)

# 

eric = ['eric',['ps',[8,4,5]],['mq',[6.7]]]
desire = ['desire',['ms',[8,4,5]],['mq',[6.7]]]
grades = [eric,desire]
def read_grades(who,what,data):
    for i in data:
        if i[0]==who:
            for j in i[1:]:
                if j[0]== what:
                    return who ,j
                
print(read_grades('desire','ms',grades))


# #################

my_dict = {
    'numaan': 'name',
    'race': 'indian',
    'age': 27,


}

print(my_dict['age'])


