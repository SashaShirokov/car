from django.shortcuts import render


posts = [
    {
        'author': 'Shirokov',
        'title': 'Blog post1',
        'content': 'Hello my friends',
        'date': 'August 5, 2019'
    },
    {
        'author': 'Goldman',
        'title': 'Blog post3',
        'content': 'Check our cars',
        'date': 'August 7, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О нас'})
