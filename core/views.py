from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import SingupForm
# Create your views here.
def index(request):
    #burada index.html içindeki jinjaya gönderiyoruz for döngüsüne alıp items ve catagories i
    items= Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'core/index.html',{
        'categories': categories,
        'items':items
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method=='POST':
        form=SingupForm(request.POST)

        if form.is_valid():
            form.save() 
            return redirect('/login/')
    else:
        form= SingupForm()

    return render(request,'core/singup.html',{
        'form':form
    })


