from django.shortcuts import render
import json


# Create your views here.
def users(request):
    try:
        with open('users.json', 'r') as file:
            temp = json.load(file)
            return render(request, 'users.html', {'data': temp})


    except:
        return render(request, 'users.html', {'data': [{'name': "this file doesn't exist", 'age': ''}]})


def create(request, *args, **kwargs):

    try:
        with open('users.json', 'r') as file:
            temp = json.load(file)
            temp.append(kwargs)
        with open('users.json', 'w') as file:
            json.dump(temp, file)
        return render(request, 'create.html', {'data': [temp[-1]]})

    except:
        with open('users.json', 'w') as file:
            json.dump([kwargs], file)
            return render(request, 'create.html', {'data': [kwargs]})

