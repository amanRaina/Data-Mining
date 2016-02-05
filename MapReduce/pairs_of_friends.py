#__author__ = Amandeep Raina
#Assignment 1 part 3
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
	key = record[0]
	value = record[1]
	#alue.sort()
	for x in value:
		pair_list=[key,x]
		pair_list.sort()
		friend=str(key)
		#to concatenate elements in a list
		pair= ('').join(pair_list)
		mr.emit_intermediate(pair,pair_list)


def reducer(key, values):
	#print key
	#print values
	#values.sort
	if len(values)>1:
	 mr.emit(values[0])


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)