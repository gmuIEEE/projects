def find_all_years	(db) :
#create empty list to store years
    lists=[]
#for loop through db to get key and value
    for key, value in db.items():
#nested for loop to get year
        for i in value:
#store years into list
            lists.append(i[0])
#convert and revert from list to set to list to get rid of duplicates
    sets=set(lists)
    list1=list(sets)
#return sorted list
    return sorted(list1)

def total_count_for_name(db,name,gender) :
#initial condition for sum of counts
    sum=0
#for loop to go through key and values in db
    for key, value in db.items():
#condiitonal to match name
        if key[0]==name:
#conditional to match gender
            if key[1]== gender:
#for loop once conditionals are met to add the counts
                for i in value:
                    sum+= i[1]
    return sum

def names_by_year(db,year):
#empty dictionary/database
    newdb={}
#for loop to go through key and value
    for key,value in db.items():
#empty list to reset for every key
        list = []
#for loop to go through values to match year
        for i in value:
            if i[0]==year:
#if year matches, append to list
                list.append(i)
#exception for if no years are in db
        if len(list)!=0:
            newdb[key]=list

    return newdb

def largest_count_for_year(db,	year):
#two empty lists
    list1=[]
    anslist=[]
#initial condition for info is None
    info=None
#for loop to go through key and value
    for key, value in db.items():
#nested for loop to go through each value
        for i in value:
#conditional to match year
            if i[0]== year:
#append count
                list1.append(i[1])
#sort stored list
    srtlist = sorted(list1)
#another for loop to get the largest count
    for key,value in db.items():
#nested loop to go through values
        for i in value:
#conditional to match year
            if i[0]==year:
#conditional to match largest count
                if i[1]== srtlist[-1]:
#store key into info var
                    info= key
#if info is not None
        if info!= None:
#set name,gender, count to their respective values and append it into anslist
            name=info[0]
            gender=info[1]
            count= srtlist[-1]
            anslist.append((name,gender,count))
#sort anslist and remove duplicates
    ans= sorted(list(set(anslist)))
    return ans

def add_name(db,name,gender,year,count,rank=None):
#set inital condition for exists as no
    exists="no"
#go through db with for loop with items()
    for key,value in db.items():
#name and gender should match
        if key[0]== name:
            if key[1]== gender:
#nested for loop to go through value
                for i in value:
#if year matches, change count and rank, sort, and change exists to yes
                    if i[0]==year:
                        i[1]= count
                        i[2]= rank
                        db[key].sort()
                        exists = "yes"
#another for loop to check if name, gender matches to add extra years
    for key, value in db.items():
        if key[0] == name:
            if key[1] == gender:
#append year,count,rank and change exists to yes
                db[key].append((year,count,rank))
                db[key].sort()
                exists="yes"
#if exists is no, add the new name and gender as well
    if exists=="no":
        db[(name,gender)]=([(year,count,rank)])

    return None

def get_rank_for_name_year(rdb, name, gender, year):
#initial conditional for ans is None for no rank to return None
    ans=None
#for loop to go through key and value
    for key, value in rdb.items():
#conditionals to match name and gender
        if key[0]== name:
            if key[1]== gender:
#nested for loop to go through value
                for i in value:
#conditional to match year
                    if i[0]==year:
#store rank into ans
                        ans= i[2]
    return ans

def popularity_by_name(rdb, name, gender):
#empty list to store year and rank
    list=[]
#for loop to go through db with key and value
    for key, value in rdb.items():
#conditional to match name and gender
        if key[0]== name:
            if key[1]== gender:
#nested for loop to store year and rank into list
                for i in value:
                    list.append((i[0], i[2]))
    return list

def popularity_by_year(rdb,	gender,	year,	top=10):
#empty list that would store rank and name and other to sort through 1st list
    list=[]
    ans=[]
#for loop to go through db
    for key,value in rdb.items():
#conditional to match gender
        if key[1]==gender:
#nested for loop to go through values
            for i in value:
#conditional to match year
                if i[0]== year:
#append the count and name to list
                    list.append((i[2],key[0]))
#sort list for popularity
    slist=sorted(list)
#for loop to create ans list from sorted list
    for j in range(len(slist)):
#get ans list within top arg
        if j<top:
#new entry separated by conditional
            if slist[j] not in ans:
                ans.append(slist[j])
#conditional to avoid index error
            if j+1<len(slist):
#check if names are same after
                if slist[j][0]== slist[j+1][0]:
#new entry conditional
                    if slist[j+1] not in ans:
#append to ans list
                        ans.append(slist[j+1])

    return ans

def always_popular_names(rdb,	gender,	years=None,	top=10):
#create empty list to list1 and ans
    list1=[]
    ans=[]
#exception if year list is None
    if years== None:
#make year var into a list
        years=[]
#for loop to append all years into year list
        for key,value in rdb.items():
            for i in value:
                years.append(i[0])
#run each year with popularity by year funct and append it
    for j in years:
        list1.append(popularity_by_year(rdb,gender,j, top))
#get the names
    for x in list1:
        for y in x:
            if y[0]<=top:
                    ans.append(y[1])
#new list for ans to store the list of names
    ans1=[]
#go through ans list to get the bounded list of names
    for z in ans:
        counter=0
        for check in ans:
            if z== check:
                counter+=1
        if counter==len(years):
            ans1.append(z)
#get rid of duplicates and sort
    ans2=list(set(ans1))
    ans2.sort()

    return ans2

def rank_names_by_year_gender(db,	year,	gender) :
#create empty store and ranking list
    store=[]
    ranking=[]
#for loop to go through db
    for key,value in db.items():
#conditional to match gender
        if key[1]== gender:
            for i in value:
#conditional to match year, then store count
                if i[0] == year:
                    store.append(i[1])
#sort through store to get rankings later
    store.sort()
#reverse to get highest count
    countlist=store[::-1]
#for loop through this list and add 1 to get ranking
    for places,count in enumerate(countlist):
        ranks=places+1
#if index error, continue
        try:
            if countlist[places]==countlist[places-1]:
                ranks= ranking[places-1][0]
        except:
            continue
        ranking.append((ranks, count))
#if no ranking exception, make sure everything matches
    if len(ranking)==0:
        for key3, value3 in db.items():
            if key3[1] == gender:
                for index, c in enumerate(value3):
                    if c[0] == year:
                        editor = list(c)
                        editor[2] = 1
                        ans = tuple(editor)
                        db[key3][index] = ans
#conditional for rankings, make sure everything matches
    else:
        for rank in ranking:
            for key1,value1 in db.items():
                if key1[1]==gender:
                    for index,j in enumerate(value1):
                        if j[0]==year:
                            if j[1]== rank[1]:
#editor var to list j, then edit db
                                editor=list(j)
                                editor[2]= rank[0]
                                ans=tuple(editor)
                                db[key1][index]=ans


    return None

def read_file(filename):
#open, read ,close file
    f = open(filename)
    content = f.read()
    f.close()
#split content by new line
    strlist = content.split("\n")
#remove empties
    strlist.remove("")
#delete first line
    del strlist[0]
#empty dictionary and listfor values
    dbdict={}
    value=[]
#for loop to get dict
    for i in strlist:
#split by , commas
        j=i.split(",")
#assign year, gender, name, count to respective indexes
        year=j[0][1:len(j[0])-1]
        gender=j[1][1:len(j[1])-1]
        name=j[2][1:len(j[2])-1]
        count=j[3][1:len(j[3])-1]
#key and value vars
        key=(name,gender)
#reset value list if new key
        if key not in dbdict:
            value = []
#append year,count and None to value list
        value.append((int(year), int(count), None))
#change value of key
        dbdict[key]=value
    return dbdict

def rank_names(db):
#run find all years and set it to years var
    years= find_all_years(db)
#go through all years
    for i in years:
        for key, value in db.items():
#run rank names by year funct with each key and value in db
            rank_names_by_year_gender(db,i,key[1])

    return None





