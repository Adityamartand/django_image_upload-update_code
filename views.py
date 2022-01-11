import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image


def uplpoad_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def edit_image(request, pk):
    prod = Image.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.save()
        messages.success(request, " Updated Successfully")
        return redirect('/')

    context = {'prod': prod}
    return render(request, 'edit.html', context)
