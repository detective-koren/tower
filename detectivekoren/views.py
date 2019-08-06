from django.shortcuts import redirect



def index(request):
    return redirect('tower:place_list')