###problem:


##solution:
'''
* 1918 was the year of changing for calander

*3 cases:
	* before 1918: For 256th day.There are to cases , either year is leap year or not.
		*If it is leap year(leap years are divisible by 4), Feb will have 29 days.
			So, 31 (Jan) + 29 (Feb) +31 (March) +30 (April) + 31 (May) + 30(June) + 31(July) + 31 (Aug) + 12 (Sept) = 256 days = 12.09.yyyy (respective year)
		* If year is not leap year, Feb month have 28 days.So, 256th day is 13.09.yyyy (respective year)

	* In 1918: If Year given is 1918,then Days will be 1st Jan to 31st Jan (Julian calander) then, then 14th to 31st Dec (Gregorian calander).As 1918 is neither "divisible by 400" nor "Divisible by 4 and not divisible by 100".So 1918 is not leap year for Gregorian calander.
	Then 256th day in 1918 will be = 31 days(Jan) + 14 days (14Feb to 28 Feb) + 30 days (March) + 31 days (April) + 30 days (May) + 31 days (June) + 30 days (July) + 31 days (Aug) + 27 days (sept). So day is 27.09.1918.

	* After 1918: For 256th day.There are to cases , either year is leap year or not.
		* If year is leap year( either "divisible by 400" or "Divisible by 4 and not divisible by 100"): 
			So, 31 (Jan) + 29 (Feb) +31 (March) +30 (April) + 31 (May) + 30(June) + 31(July) + 31 (Aug) + 12 (Sept) = 256 days = 12.09.yyyy (respective year)
		* If year is not leap year, Feb month have 28 days.So, 256th day is 13.09.yyyy (respective year)
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if int(year) == 1918:
        return "26.09.1918"
    elif int(year) < 1918:
        if int(year) % 4 == 0:
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    else:
        if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) %100 != 0):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
