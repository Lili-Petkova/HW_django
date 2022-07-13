from django.shortcuts import get_object_or_404, redirect, render

from mysite.forms import GetForm, PersonModelForm
from mysite.models import Person


def index(request):
    return render(request, 'mysite/index.html')


def select(request):
    objects = Person.objects.all()
    return render(request, 'mysite/select.html', {'objects': objects, })


def triangle(request):
    hypotenuse = None
    if 'submit' in request.GET:
        _get_form = GetForm(request.GET)
        if _get_form.is_valid():
            first = _get_form.cleaned_data['first_cathetus']
            second = _get_form.cleaned_data['second_cathetus']
            third = first ** 2 + second ** 2
            hypotenuse = round(third ** 0.5)
    else:
        _get_form = GetForm()
    return render(request, 'mysite/answer_mysite.html', {'get_form': _get_form, "hypotenuse": hypotenuse})


def new_person(request):
    if request.method == 'POST':
        person_form = PersonModelForm(data=request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('mysite:index')
    else:
        person_form = PersonModelForm()
    return render(
        request,
        'mysite/person_form.html',
        {
            'person_form': person_form,
        }
    )


def update_person(request, pk):
    user = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonModelForm(data=request.POST, instance=user)
        if person_form.is_valid():
            person_form.save()
            return redirect('mysite:index')
    else:
        person_form = PersonModelForm(instance=user)
    return render(
        request,
        'mysite/update_person.html',
        {
            'person_form': person_form,
            'user': user,
        }
    )
