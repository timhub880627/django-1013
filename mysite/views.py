from django.shortcuts import render
import random 

def index(request):

    name = "何敏煌"
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    return render(request, 'index.html', locals())