#__author__ = Amandeep Raina
import sys
import itertools

buckets=[]
countforItem={}
supportForItem={}
frequentItemsSet=set()
freqitemsList=[]
freqDicList=[]
freqSetList=[]
passList=[]
temp_list=[]
candidateSet=set()
list2=set()
list3={}

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def display(values,key):
	sorted(values)
	for v in values:
		temList=','.join(v)
		print(temList)


def Apriori(data,support):
	size=1
	for line in data:
		buckets.append(line.rstrip('\n').split(','))

	buckets1=sorted(buckets)

	for items in buckets1:
		for i in items:
			if(supportForItem.get(i)==None):
				supportForItem[i]=1
			else:
				supportForItem[i]+=1	
			# print(supportForItem)

			if(supportForItem[i]>=int(support)):
				countforItem[i]=supportForItem[i]
				for key in countforItem.keys():
					frequentItemsSet.add(key)

			
	freqitemsList=frequentItemsSet	
	freqitemsList=sorted(freqitemsList)
	#print(freqitems)
	freqDicList.append(countforItem)
	freqSetList.append(frequentItemsSet)
	print("Frequent Item set of size 1")					
	for item in freqitemsList:
		print(item)

		
	size=size+1
	while(len(freqSetList[size-2])>=size):
		
		list1=[]
		
		for key in freqDicList[0]:
			list1.append(key)	
		temp_candi=set(itertools.combinations(list1, size))
		candidateSet=sorted(temp_candi)
		
		tempDic={}
		passDic={}
		passSet=set()
		for candidate in candidateSet:
			for row in buckets1:
				if set(candidate).issubset(row):
					if tempDic.get(candidate)==None:
						tempDic[candidate]=1
					else:
						tempDic[candidate]+=1
	
		for key in tempDic:
			if int(tempDic[key])>=int(support):
				passDic[key]=tempDic[key]
				element=key
				passSet.add(key)
				passList.append(sorted(key))
		freqDicList.append(passDic)
		freqSetList.append(passSet)
		freqitemsList=sorted(freqitemsList)
		size+=1
	

	sortedList=sorted(passList)
	sortedList=sorted(sortedList,key=len)
	x=len(sortedList)
	for i in range(x):
		temp_list=sortedList[i]
		length=len(sortedList[i])
		list3.setdefault(len(sortedList[i]), []).append(sortedList[i])
		sorted(list3)
		

	for key in list3:
		print("\nFequent Items Sets of Size " + str(key))
		display(list3.get(key),key)
		

def main():
	data=open(sys.argv[1])
	data=set(data)
	min_support=sys.argv[2]
	Apriori(data,min_support)

			
if __name__ == '__main__':
	main()

