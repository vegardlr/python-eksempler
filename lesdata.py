from pylab import *
import pandas

data = empty([2,4])
print(data)
data = loadtxt("data.txt")
print(data)


data = pandas.read_table("data_no.txt",delimiter="\t")
#data = loadtxt("data_no.txt")
print(data)
print(shape(data))
print(type(data))
