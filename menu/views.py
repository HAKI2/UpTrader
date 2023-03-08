from django.shortcuts import render


def test_example(request):
    return render(request, 'test_example.html')