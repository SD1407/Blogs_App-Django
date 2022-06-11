from django.shortcuts import render # django provides this (import render) this render can render the template whiler returning
# from django.http import HttpResponse  # we are rendering hhtpresponse from django.http

# as we know that ths is gonna be a blog app we let us create some dummy posts by creating some dummy posts by creating a dictionary

posts = [
    {
        'author': 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2020'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 28, 2020'
    }

]


# VERY VERY IMPORTANT DUJANGO THROWS ERROR FOR UNCLEAR SYNTAX (SPACING AND EVERTHING MATTERS)
def home(request):  # defining a function which will return the http response
     context = {   # here inside this function we have created a dictionary which will basically store the elements of the dictionary named "posts" as name 'posts' we can access that through name posts in the templates section
        'posts' : posts
     }
     # return HttpResponse('<h1>Blog Home<h1/>') # we nned to create the urls.py from which it will be directed here
     return render(request, 'blog/home.html', context) # (1st argument is 'request' and 2nd one is the template path) ( here the 3rd argument is that context dictionary)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  # here we have passed default argument for about page by defining a dictionary as a 3rd argument
