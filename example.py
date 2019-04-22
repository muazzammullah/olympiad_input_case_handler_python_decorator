import sys
import time

def case(orig_func):
	def wrapper(*args,**kwargs):
		cases=int(input())
		cases_array=[]
		for x in range(0,cases):
			case=input()
			cases_array.append(case)
		kwargs['arr']=cases_array
		result=orig_func(*args,**kwargs)
		return result
	return wrapper()

@case
def myfunc(arr):
	for x in range(0,len(arr)):
		case_atr=arr[x].split(" ")
		m=int(case_atr[0])
		s=int(case_atr[1])
		ms=int(m/s)
		casestr="Case #"+str(x+1)+":"
		print(casestr,ms)
		
	
