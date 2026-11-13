from django.shortcuts import render

# Create your views here.

# View 1
def estatica(request):
	return render(request,"estatica.html")
# View 2
def dinamica(request):
	return render(request, "dinamica.html")
# View 3
def inicio(request):
    return render(request, 'index.html')