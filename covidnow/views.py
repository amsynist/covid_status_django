from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "362a91af1dmsh39362dad7b9c231p1973d2jsn62606bc58b7c",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def index(request):
    res1 = int(response['results'])
    list1 = []
    for x in range(0,res1):
        list1.append(response['response'][x]['country'])
    if request.method == "POST":
        res1 = int(response['results'])
        countryselection = request.POST['countryselection']
        for x in range(0,res1):
            if countryselection == response['response'][x]['country']:
                country = response['response'][x]['country']
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
        data = {'list1': list1 ,'country': country,'active': active,'critical': critical,'deaths': deaths,'new': new,'total':total,'recovered':recovered}
        return render(request,'index.html',data)
    res1 = int(response['results'])
    list1 = []
    for x in range(0,res1):
        list1.append(response['response'][x]['country'])
    # data1 = {'list1' : 'list1'}

    return render(request,'index.html',{'list1' : list1})

# def home(request):
#       return render(request,'home.html',{'list1' : list1})