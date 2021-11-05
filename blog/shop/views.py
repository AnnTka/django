from django.shortcuts import render
from shop.forms import ProductFiltersForm
from shop.models import Product
from django.db.models import F, Sum
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from shop.task import run_products_update


def products_view(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        if filters_form.cleaned_data["cost__gt"]:
            products = products.filter(cost__gt=filters_form.cleaned_data["cost__gt"])
        if filters_form.cleaned_data["cost__lt"]:
            products = products.filter(cost__lt=filters_form.cleaned_data["cost__lt"])

        if filters_form.cleaned_data["order_by"]:
            order_by = filters_form.cleaned_data["order_by"]
            if order_by == "cost_asc":
                products = products.order_by("cost")
            if order_by == "cost_desc":
                products = products.order_by("-cost")
            if order_by == "max_count":
                products = products.annotate(
                    total_count=Sum("purchases__count")
                ).order_by("-total_count")
            if order_by == "max_cost":
                products = products.annotate(
                    total_cost=Sum("purchases__count") * F("cost")
                ).order_by("-total_cost")

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(
        request,
        "products/list.html",
        {"products": products, "filters_form": filters_form},
    )


def run_products_update_task(request):
    run_products_update.delay()
    return HttpResponse("OK")
