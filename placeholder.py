# %s , %d , %f , %g are used for formatting strings in python, simply they are named place holders.
# placeholders can be used everywhere a string exists, such as plot legends, plot titles, print command and etc.
# In print('description: %s' % descrip) the %s operator will be replaced by the text string stored in the descrip variable.

name ='giacomo'
number = 4.3
print('%s %s %d %f %g' % (name, number, number, number, number))

#check the out put.

# as you can see %d will truncate to integer, %s will maintain formatting,
# %f will print as float and %g is used for generic number
# everything you may face is explained in this link: https://docs.python.org/3/library/stdtypes.html#string-formatting-operations