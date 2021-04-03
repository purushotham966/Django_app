from django.shortcuts import render


from pymongo import MongoClient 
  

client= MongoClient('mongo_address') 
final=[]
db1= client["TN_Restaurants"]
collection1=db1["Restaurants"]
db = client["image-Tennessee"]
collection=db["Tennessee_images"]
y=[]
for i in collection1.find()[:20]:
    id_=i['restaurantId']
    x=list(collection.find({'restaurantId':id_}))
    z=[]
    if x:
        for j in x:
            y.append(j["imageUrl"])
            z.append(j["imageUrl"])
        d={'id_': i['restaurantId'],'name':i['name'],'web':i['website'],'add':i['oldAddress'],'phone':i['phone'][0],'imageUrl':z[0],'cuisine':i['cuisine'][0]}
        final.append(d)
    else:
        continue







def home(request):
    
    return render(request, 'blog/home.html', {'final':final})

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
