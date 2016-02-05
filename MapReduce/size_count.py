"""__Author__ = Amandeep Raina
Assignment 1 Part 1"""

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
    #print key
    value = record[1]
    words = value.split(" ")
    total1=0
    total2=0
    total3=0
    total4=0
    size_list1=["large",0]
    size_list2=["medium",0]
    size_list3=["small",0]
    size_list4=["tiny",0]
    for w in words:
     length=len(w)
     if length>=10:
      size1="large"
      total1=total1+1
      size_list1=[size1,total1]
     elif length>=5 and length <=9:
      size2="medium"
      total2=total2+1
      size_list2=[size2,total2]
     elif length>=2 and length <=4:
      size3="small"
      total3=total3+1
      size_list3=[size3,total3]
     elif length==1:
      size4="tiny" 
      total4=total4+1
      size_list4=[size4,total4]
    mr.emit_intermediate(key,size_list1)
    mr.emit_intermediate(key,size_list2)
    mr.emit_intermediate(key,size_list3)
    mr.emit_intermediate(key,size_list4)


def reducer(key,size_list):
    # key: word
    # value: list of occurrence counts
    total1=0
    total2=0
    total3=0
    total4=0
    tuple1=[]
    tuple2=[]
    tuple3=[]
    tuple4=[]
    for x in size_list:
     size=x[0]
     v=x[1]
     if size=="large":
      total1+=v
      tuple1=[size,total1]
     elif size=="medium":
      total2+=v
      tuple2=[size,total2]
     elif size=="small":
      total3+=v
      tuple3=[size,total3]
     elif size=="tiny": 
      total4+=v
      tuple4=[size,total4]
    mr.emit((key,[tuple1,tuple2,tuple3,tuple4]))  
     

# Do not modify below this line
# =============================
if __name__ == "__main__":
 inputdata = open(sys.argv[1])
 mr.execute(inputdata, mapper, reducer)
