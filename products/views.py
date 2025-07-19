from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Car
from products.forms.create import CreateProduct
from products.forms.edit import EditProduct
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, "index.html", {"cars": cars})



@login_required(login_url="/admin/login/")
def catalog(request):
    products = Car.objects.all().order_by("id")

    return render(
        request, "catalog.html", {"products": products, "count": len(products)}
    )


def delete(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")

    itemToDelete = get_object_or_404(Car, pk=id)

    itemToDelete.delete()

    return redirect("/list")

def create(request):
    # GET - відкриття сторінки для створеня
    # POST - створення продукту

    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect("/list")

    return render(request, "create.html", {"form": form})


def edit(request, id):
    product = Car.objects.get(id=id)

    if product is None:
        return HttpResponse("Car not found")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = EditProduct(request.POST, request.FILES, instance=product)

        # If the product has an image, delete the old one
        if request.FILES and product.image:
            product.image.delete(save=False)

        if form.is_valid():
            form.save()

            messages.success(request, "Product updated successfully!")
            return redirect("/list")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "edit.html", {"form": form})

def show(request, id):
    itemToDelete = get_object_or_404(Car, pk=id)

    if itemToDelete.image:
        itemToDelete.image.delete(save=False)

    return render(request, "show.html", {"car": itemToDelete})
