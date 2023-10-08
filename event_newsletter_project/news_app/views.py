from django.shortcuts import render
from django.contrib import messages  # Import messages framework
from .forms import NewsForm
from .models import NewsArticle
from .news import News


def get_news(request):
    """
    View function to handle the retrieval and display of news articles based on user input.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response displaying news articles and a form.

    Raises:
        N/A

    This view function handles both GET and POST requests. When a POST request is received,
    it validates the user-submitted form containing country and category selections. If the
    form is valid, it retrieves news articles based on the user's choices and stores them
    in the database. If the form is not valid, it displays appropriate error messages.
    In case of invalid country or category, it catches the specific exceptions
    (CountryNotFoundError and CategoryNotFoundError) and displays user-friendly error messages.
    For GET requests or after processing a POST request, it renders the 'news.html' template
    with the form and the retrieved news articles.

    """
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            category = form.cleaned_data["category"]

            try:
                news = News(country, category)
                articles = news.save_get_news()
                NewsArticle.objects.all().delete()
                for article in articles.itertuples():
                    NewsArticle.objects.create(
                        author=article.author, title=article.title, url=article.url
                    )
            except Exception as e:
                messages.error(request, f"Reason: {str(e)}")

    else:
        form = NewsForm()
    articles = NewsArticle.objects.all()
    return render(request, "news.html", {"form": form, "articles": articles})
