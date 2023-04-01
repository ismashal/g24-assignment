from django.shortcuts import render
import pandas as pd

# Create your views here.
 
# relative import of forms
from .models import City_Info
from .forms import City_Info_form
 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    if request.method=="POST":
        # add the dictionary during initialization
        form = City_Info_form(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,"home.html",{"message":"Your Details Inserted Successfully"})
    else:
        form=City_Info_form()
        return render(request,"create_view.html",{"form":form})
        

def show_all(request):
    all_val=City_Info.objects.all().values()
    df=pd.DataFrame(list(all_val))
    df_html=df.to_html(classes='table table-striped table-hover ', justify='center')
    return render(request,"show_all.html",{"all":df_html})


def update(request):
    if request.method=="POST":
        form = City_Info_form(request.POST or None)
        if request.POST["City"]:
            s=City_Info.objects.get(pk=request.POST["City"])
            form.instance=s
            
        if form.is_valid:
            form.save()
            
        return render(request,"home.html",{"message":"Your Details updated Successfully"})
    else:
        form=City_Info_form()
        return render(request,"create_view.html",{"form":form})