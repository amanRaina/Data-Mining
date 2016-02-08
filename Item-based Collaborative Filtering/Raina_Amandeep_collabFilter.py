#author Amandeep Raina
import sys
import json
import string
import math
from operator import itemgetter

ratings = {} # initialize an empty ratings dictionary
movies=[]
users=[]
average={}
similarit_list=[]
similarity_list=[]
sim_list=[]
movies_rated=[]
prediction_list=[]

#for caculating average of two movies. 
#we get the dictionary of users+ratings for both the items
def avg(value_dic,value_dic2):
    num=0  #to count number of users that have rated both the items
    total=0
    for user1 in value_dic:
        for user2 in value_dic2:
            if(user1==user2):
                #increment the count of corated users
                num+=1
                #get the corresponding rating
                total+=value_dic.get(user1)   

    #if no corarted users then num=0            
    if(num!=0):         
        return total/num    
    

def recommendation(ratings_file,user1,n,k):
     
    newfile=ratings_file.splitlines()
    movies_unrated=[]


    for line in newfile:
        v=line.split("\t")
        ratings.setdefault(str(v[2]),{})
        #created dictionary of dictionary of movie,user and ratings
        ratings[str(v[2])][str(v[0])]=float(v[1])

        #created database for movie
        movie=[str(v[2])]
        if movie not in movies:
            movies.append(movie)
        #created database for user  
        user=[str(v[0])]    
        if user not in users:
            users.append(user)  

    print(ratings)        

    #creates a list of rated and unrated movies     
    for movie in movies:
        if (ratings[movie[0]]).get(user1)!=None:
            movies_rated.append(movie[0])
        else:
            movies_unrated.append(movie[0])

    #sort the list of unrated movies        
    movies_unrated=sorted(movies_unrated)

    prediction_list=[]

    for user in users:
       # print(user[0])
        if user[0]==user1:
        #calculate prediction of all unrated movies
            for movie_unrated in movies_unrated:
        #get the nearest neigbour based on weights for each unrated movies
                nearest=nearestNeighbors(movie_unrated,ratings)
        #make the predictions based on nearest neighbours and their weights
                prediction=predict(user1,nearest,ratings,n)
        #create a list for prediction
                prediction_list.append((movie_unrated,round(prediction,5)))
            

            prediction_list=sorted(prediction_list,key=itemgetter(0))
            prediction_list=sorted(prediction_list,key=itemgetter(1),reverse=True)
            
            #reduce the list to top k reccomendations
            prediction_list=prediction_list[0:k]

            #for printing the final prediction list on the screen
            for movie in prediction_list:
                print(movie[0],movie[1])
            
#function for finding similarity
def similarity(item1,item2):

    num_up=0
    num_down=0
    sim_count=0
    value=[]
    i_value=[]
    j_value=[]
    avg_item1=avg(ratings[item1],ratings[item2])
    avg_item2=avg(ratings[item2],ratings[item1])


    for key in (ratings[item1]):
        for key2 in (ratings[item2]):
            #if the users have both the items then proceed
            if(key==key2):
                sim_count+=1;
                var1=(ratings[item1]).get(key)-avg_item1
                var2=(ratings[item2]).get(key)-avg_item2
                value.append((var1,var2))
                i_value.append(var1**2)
                j_value.append(var2**2)

        #if no users in common then return 0        
        if sim_count==0:
            similarity_val=0.0
    #calculating the numerator for all the users
    for v in value:
        num_up+=v[0]*v[1]

    i_down=0;
    j_down=0;
    # calculating denominator for all the users
    for v in i_value:
        i_down+=v
    for v in j_value:
        j_down+=v   
    i_down1=math.sqrt(i_down)
    j_down1=math.sqrt(j_down)   
    num_down=i_down1*j_down1
    

    if(num_down!=0):
        #calulating similaity value w(i,j)
        similarity_val=num_up/num_down
        
    else:
        similarity_val=0.0
        
    return similarity_val

#function for finding nearest neighnours
def nearestNeighbors(item1, all_user_ratings):
    nearest=[]
    #print(item1)
    for key in all_user_ratings:
        #print(key)
        if key!=item1:
            
            nearest.append((key,(similarity(item1,key))))

    nearest=sorted(nearest,key=itemgetter(0))       
    nearest=sorted(nearest,key=itemgetter(1),reverse=True)      
    # nearest=sorted(nearest,key=lambda x:(x[1],x[0]),reverse=True)

    return nearest


#function to get the predictions nased on n nearest neighbours
def predict(user1, k_nearest_neighbors, ratings,n):
    total_similarity=0
    total_up=0
    count=0
    movies_ratedByUser=[]
    prediction=0
    
    #print("k_neigbours",k_nearest_neighbors)
    for u in k_nearest_neighbors:
        #print(ratings[u[0]].get(user1))
        if (ratings[u[0]]).get(user1)!=None:
            #take a counter to find top n neighbours
            count+=1
            movies_ratedByUser.append((u[0],u[1]))
            if(count==n):
                for x in movies_ratedByUser:
                    total_similarity+=x[1]
                    total_up+=x[1]*(ratings[x[0]]).get(user1)
                    if(total_similarity!=0):
                        prediction=(total_up/abs(total_similarity))
                    else:
                        prediction=0

    return prediction

def main():

    ratings_file = open(sys.argv[1]).read()
    user1 = str(sys.argv[2])
    n = int(sys.argv[3])
    k = int(sys.argv[4])

    #calling the recommendation method that reads the file and prints the top k predictions
    recommendation(ratings_file,user1,n,k)


if __name__ == '__main__':
    main()   