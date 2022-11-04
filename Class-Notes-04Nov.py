#11/04/2022 Class Notes, Cody Brown

#Counting characters in a word using dictionary, from class 10/31/2022
def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

h = {'milk':1, 'butter':2, 'egg':6, 'bread':1, 'cheese':3, 'jam':8}

#More on sorted()
h = sorted(h)
h
#this returns ['bread', 'butter', 'cheese', 'egg', 'jam', 'milk']
type(h)
#this returns <class 'list'>
#h is now a list!

#Using sorted() Safely
h = {'milk':1, 'butter':2, 'egg':6, 'bread':1, 'cheese':3, 'jam':8}

for key in sorted(h):
    print(key, h[key])
#this returns:
#bread 1
#butter 2
#cheese 3
#egg 6
#jam 8
#milk 1

#Set a for loop over a list, it will asks

#Now, if you type h again, it will still be a dictionary
h
#this returns {'milk': 1, 'butter': 2, 'egg': 6, 'bread': 1, 'cheese': 3, 'jam': 8}
type(h)
#this returns <class 'dict'>

#List VS dict
#Lists:
    #work with indices, and the indices are integer
    #item repetition is allowed
    #values are available through using indices
#Dictionary:
    #works with keys and keys can be anything
    #repition can be problematic
    #keys give the values

#Class Activities

#dictionary differences
d1 = {'d':'london','a':'michigan','b':'paris','c':'tehran','a':'newyork'}
d1
#this returns {'d': 'london', 'a': 'newyork', 'b': 'paris', 'c': 'tehran'}
#Why? Why isn't 'a' 'michigan'? We override it later in the dictionary,
#and so that is it's most updated value

#More
dict1 = {'a1':'egg','a2':2,'a3':0.05,'a4':False}
dict2 = sorted(dict1)
dict2['a1']
#this returns a TypeError: list indices must be integers or slices, not str
#because it is a list
vals2 = dict2.values()
#this returns a AttributeError: 'list' object has no attribute 'values'
vals1=dict1.values()
vals1
#this returns:
    dict_values(['egg', 2, 0.05, False])
    #this returns the values of the dict1
type(vals1)
#this returns:
    <class 'dict_values'>


#Reverse Lookup
#given a dictionary 2 and key k, can find corresponding
#value v = d[k], which is called a lookup

#But what if you havea value and want the key?
    #1) there could be more than one key that maps the value v
    #depending on the application, you might be able to pick one
    #or list the ones that contain it
    #2) no simple syntax to reverse lookup

#Reverse lookup function
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
        #raise LookupError() ?
        #raise causes an exception, here, it indicates that
        #a lookup failed
exception LookupError: #the base class for the exceptions that are raised when a key
                       #or index used on a mapping or sequence is invalid

#Class activity: Errors and why
#KeyError:  key is not found in a dictionary
#KeyboardInterrupt: the user hits the interrup key (ctrl + c or delete)
#ImportError: the imported module is not found
#LookupError: a key ot index used on a mapping or sequence is invalida

#Back to Histogram code
def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

h = histogram('parrot')
h
#this returns {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}

key = reverse_lookup(h,2)
key
#this returns 'r'

key = reverse_lookup(h,3)
#this returns:
#Traceback (most recent call last):
 # File "<pyshell#38>", line 1, in <module>
#    key = reverse_lookup(h,3)
 # File "<pyshell#30>", line 5, in reverse_lookup
#    raise LookupError()
#LookupError


#go over last slides***
