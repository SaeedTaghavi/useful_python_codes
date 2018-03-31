# Lists as an iterable

# collection = ['hey', 5, 'd' , 2.67]
# for x in collection:
#     print x

list = []
m_min = 1.0
m_max = 5.0
step = .5
N = (m_max - m_min)/step

for i in range (0,int(N)+1):
    list = list + [ m_min + i*step ]
print list
