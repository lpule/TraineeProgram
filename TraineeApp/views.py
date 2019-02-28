from django.shortcuts import render

from .forms import PostForm
from .models import Post


def home(request):
    form = PostForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, "TraineeApp/default_form.html", context)
