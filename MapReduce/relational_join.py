#__Author__= Amandeep Raina
#Assignment 1 part 5
import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    if key=="MovieNames":
     mr.emit_intermediate(record[2],record)
    elif key=="MovieRatings":
     mr.emit_intermediate(record[1],record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    movie_name=""
    movie_ratings=""
    tuple=[]
    tuple1=[]
    tuple2=[]
    tuple3=[]
    for v in list_of_values:
      if v[0]=="MovieNames":
        movie_name=v[1]
        tuple1.append(v[1:])
      elif v[0]=="MovieRatings":
        tuple2.append(v[1:])
        tuple3.append(v[-1])

    avg=float(sum(tuple3))/len(tuple3)

    for i in tuple1:
      for j in tuple2:
        mr.emit(i+j)

    mr.emit((movie_name,avg))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)