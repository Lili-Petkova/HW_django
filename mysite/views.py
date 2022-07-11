from django.shortcuts import render

from mysite.forms import GetForm


def triangle(request):
    if 'submit' in request.GET:
        _get_form = GetForm(request.GET)
        if _get_form.is_valid():
            first = _get_form.cleaned_data['first_cathetus']
            second = _get_form.cleaned_data['second_cathetus']
            hypotenuse = first ** 2 + second ** 2
            answer = round(hypotenuse ** 0.5)
            return render(request, 'mysite/answer_mysite.html', {'hypotenuse': answer, 'get_form': _get_form},)

    else:
        _get_form = GetForm()
    return render(request, 'mysite/base_mysite.html', {'get_form': _get_form})
