from datetime import date

from django.shortcuts import render

all_posts = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Peter",
    "date": date(1960, 10, 1),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happended whilst I was enjoying the view!",
    "content": """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Soluta ipsa, optio quaerat
        quidem delectus, pariatur aperiam, exercitationem omnis suscipit provident ratione 
        aspernatur consequuntur harum. Ullam officiis molestiae illo architecto deleniti!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Soluta ipsa, optio quaerat
        quidem delectus, pariatur aperiam, exercitationem omnis suscipit provident ratione 
        aspernatur consequuntur harum. Ullam officiis molestiae illo architecto deleniti!

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Soluta ipsa, optio quaerat
        quidem delectus, pariatur aperiam, exercitationem omnis suscipit provident ratione 
        aspernatur consequuntur harum. Ullam officiis molestiae illo architecto deleniti!
    """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Peter",
        "date": date(2023, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Peter",
        "date": date(1980, 5, 3),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
] 

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    lastest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": lastest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })

