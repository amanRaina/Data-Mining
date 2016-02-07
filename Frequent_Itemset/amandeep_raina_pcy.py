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
num_value={}
candidatebucketset=set()
hashgenList=[]
pass3Dic={}
#list3.setdefault(key, []).append(value)

def display(values,key):
	sorted(values)
	for v in values:
		temList=','.join(v)
		print(temList)


def getHashForPair(pairs):
	
	hash_value=""
	hash_list=[]
	for items in pairs:
		hash_list.append(num_value.get(items))

	hash_list2=sorted(hash_list)
	#print(hash_list2)
	hash_value=''.join((str(x) for x in hash_list2))
	#print(hash_value)	
	return hash_value
			


def generate_Hash(buckets1,support,size,hash_size):
	i=0
	for items in buckets1:
		for i in items:
			list2.add(i)
	
	list4=sorted(list2)
	#print(list3)
	count=1
	for x in list4:
		num_value[x]=count
		count=count+1
	

	pass2Dic={}

	for items in buckets1:
		#print(items)
		candidate_temp=set(itertools.combinations(items, (size+1)))
		candidatebucketset=candidate_temp

		for pairs in candidate_temp:
			#print(pairs)
			hash_value=getHashForPair(pairs)
			hash_value=int(hash_value)
			hash_size=int(hash_size)
			ModVal=hash_value%hash_size
			#print(ModVal)
			if pass2Dic.get(ModVal)==None:
				pass2Dic[ModVal]=1
			else:
				pass2Dic[ModVal]+=1

	#print(pass2Dic)
	for keys in pass2Dic:
		if(pass2Dic.get(keys)>=int(support)):	
			pass2Dic[keys]=1
		else:
			pass2Dic[keys]=0	

	return pass2Dic				


def pcy(data,support,hash_size):
	size=1
	for line in data:
		buckets.append(line.rstrip('\n').split(','))

	buckets1=sorted(buckets)
	#print(buckets1)
	pass3Dic={}
	pass3Dic=generate_Hash(buckets1,support,size,hash_size)
	#print(pass3Dic)

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
		#print()
		print(item)

		
	size=size+1
	#print(freqSetList)
	while(len(freqSetList[size-2])>=size):
		list1=[]
		
		for key in freqDicList[0]:
			list1.append(key)
		#print(list1)	
		temp_candi=set(itertools.combinations(list1, size))
		candidateSet=temp_candi

		tempDic={}
		passDic={}
		passSet=set()

		#pass3Dic=generate_Hash(buckets1,support,size,hash_size)

		for candidate in candidateSet:
			for row in buckets1:
				if set(candidate).issubset(row):
					hash_value=getHashForPair(candidate)
					#print(hash_value)
					hash_value=int(hash_value)
					hash_size=int(hash_size)
					ModVal=hash_value%hash_size
					#print(pass3Dic[ModVal]==1)
					if(pass3Dic[ModVal]==1):
						if tempDic.get(candidate)==None:
							tempDic[candidate]=1
						else:
							tempDic[candidate]+=1
					#else:
						#print("reject")
		for key in tempDic:
			if int(tempDic[key])>=int(support):
				passDic[key]=tempDic[key]
				element=key
				#print(key)
				passSet.add(key)
				passList.append(sorted(key))
				#print(passList)
		freqDicList.append(passDic)
		freqSetList.append(passSet)
		freqitemsList=sorted(freqitemsList)
		size+=1

	sortedList=sorted(passList)
	sortedList=sorted(sortedList,key=len)
	#print(sortedList)
	x=len(sortedList)


	for i in range(x):
		temp_list=sortedList[i]
		length=len(sortedList[i])
		list3.setdefault(len(sortedList[i]), []).append(sortedList[i])
		sorted(list3)
		

	for key in list3:
		print()
		print("\nFequent Items Sets of Size " + str(key))
		display(list3.get(key),key)

	pass3Dic=generate_Hash(buckets1,support,size,hash_size)
	#print(pass3Dic)		

def main():
	data=open(sys.argv[1])
	data=set(data)
	min_support=sys.argv[2]
	hash_size=sys.argv[3]

	pcy(data,min_support,hash_size)	

if __name__ == '__main__':
	main()

