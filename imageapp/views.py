from django.shortcuts import render
from .helpers import search_image


def app(request):
    image_data = []
    if request.GET.get("search"):
        search_query = request.GET.get("search")
        quantity = request.GET.get("quantity")
        image_data = search_image(
            search_query=search_query,
            quantity=quantity
        )
        image_data = [ images["urls"]["full"] for images in image_data["results"]]

    context = {"images": image_data}
    return render(request, "app.html", context=context)
