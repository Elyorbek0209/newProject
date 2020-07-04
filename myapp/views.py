from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'name': "Sadaf",
        'lastName': "Abdujalilova",
        'nationality':'Uzbek',
        'DOB':'July 26th, 2015',
        'dad': "Elyorbek",
        'mom': "Makhina",
        'sister': "Aisha",
    }
    return render(request, 'myapp/home.html', context)