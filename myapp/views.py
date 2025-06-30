from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'current_date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    }
    return render(request, 'myapp/index.html', context)