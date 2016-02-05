#__author__ = Amandeep Raina
#Assignment 1 part 4
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
	key = record[0]
	value = record[1]
	for x in value:
		pair_list=[key,x]
		pair_list.sort()
		pair_key=('').join(pair_list) 
		mr.emit_intermediate(pair_key,value)


def reducer(key, values):
	mutual_friends= []
	if len(values) > 1:
	 for friend in values[0]:
	  if friend in values[1]:
	   mutual_friends.append(friend)
	 if len(mutual_friends)>0:
	  mr.emit((key, mutual_friends))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)