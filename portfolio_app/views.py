from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'portfolio_app/index.html')

def posts(request):

    posts = [
        {
            'headline':'Django Portfolio Site',
            'sub_headline':'I gave my static HTML/CSS portfolio site a Django makeover.'
         },
         {
            'headline':'Second Project',
            'sub_headline':'Text describing my second project. Probably an online store.'
         },
         {
            'headline':'Third Project',
            'sub_headline':'Text describing my second project. Probably a food delivery API.'
         },
    ]
    context = {'posts': posts}
    return render(request, 'portfolio_app/posts.html', context)

def post(request):
    return render(request, 'portfolio_app/post.html')

def profile(request):
    return render(request, 'portfolio_app/profile.html')

