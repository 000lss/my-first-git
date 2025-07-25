# ex2 wk2-1 Example 2
import math
import numpy as np

# define matrix for wind data
wspeed=np.array([[113, 142, 121, 110], [117, 137, 127, 118], \
                 [117, 145, 125, 119], [95, 98, 113, 91], \
                 [88, 113, 93, 58], [86, 89, 84, 85], \
                 [96, 98, 110, 103], [97, 99, 93, 85], \
                 [129, 96, 93, 95], [136, 158, 113, 97], \
                 [110, 92, 110, 119], [104, 122, 124, 129]])

print(wspeed)

# March 2007 wind speed m/s
# 1 knot = 1609.34 m / 3600 s
a=wspeed[2,2]*1609.34/3600
print('March 2007 wind speed (m/s)')
print(a)

# average July peak wind speed (during 2005–2008)
b=(wspeed[6,1]+wspeed[6,2]+wspeed[6,3])/4
b=b*1609.34/3600
print('Average July peak wind speed (m/s)')
print(b)
print("김밥 먹고싶다")