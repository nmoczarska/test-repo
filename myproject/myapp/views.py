from django.shortcuts import render

from django.http import HttpResponse
import datetime


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

from .models import Person

def person_list(request):
    persons = Person.objects.all()
    return HttpResponse(persons)

from django.shortcuts import render

def person_list(request):
    persons = Person.objects.all()

    return render(request,
                  "myapp/person/list.html",
                  {'persons': persons})
# dodajemy brakujący import na początku pliku (modyfikacja)
from django.http import Http404, HttpResponse

def person_detail(request, id):
    # pobieramy konkretny obiekt Person
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "myapp/person/detail.html",
                  {'person': person})
