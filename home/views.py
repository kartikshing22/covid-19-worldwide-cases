
from django.shortcuts import render,HttpResponse
import requests
import json  
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4cb79c88bdmshe098dfe52132315p1ba520jsn2600c91e9768",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
# Create your views here.
def index(request):
    noofresults=int(response["results"])
    mylist=[]
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        noofresults=int(response["results"])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recoverd=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths= int(total)- int(active)-int(recoverd)
        context={'selectedcountry':selectedcountry, 'mylist':mylist,'new':new,'active':active,'critical':critical,'recoverd':recoverd,'total':total,'deaths':deaths}
        return render(request, "index.html",context)

    context={'mylist':mylist}
    return render(request, "index.html",context)