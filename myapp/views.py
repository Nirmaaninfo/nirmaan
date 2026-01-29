from django.shortcuts import render,get_object_or_404
from .models import Category,Location,Vendor,SubCategory

def home(request):
    categories = Category.objects.all().order_by("name")
    locations = Location.objects.all().order_by("city", "area")
    return render(request, "home.html", {
        "categories": categories,
        "locations": locations,
    })
def vendor_list(request):
    location_id = request.GET.get("location")
    subcategory_slug = request.GET.get("subcategory")

    vendors = Vendor.objects.all()

    selected_location = None
    selected_subcategory = None

    if location_id:
        selected_location = Location.objects.filter(id=location_id).first()
        if selected_location:
            vendors = vendors.filter(location=selected_location)

    if subcategory_slug:
        selected_subcategory = SubCategory.objects.filter(slug=subcategory_slug).first()
        if selected_subcategory:
            vendors = vendors.filter(subcategory=selected_subcategory)

    return render(request, "vendor_list.html", {
        "vendors": vendors,
        "selected_location": selected_location,
        "selected_subcategory": selected_subcategory,
    })

def vendor_detail(request, slug):
    vendor = get_object_or_404(Vendor, slug=slug)

    return render(request, "vendor_detail.html", {
        "vendor": vendor
    })

def categories_by_location(request):
    location_id = request.GET.get("location")
    location = Location.objects.get(id=location_id)

    categories = Category.objects.filter(
        vendor__location=location
    ).distinct()

    return render(request, "level1_categories.html", {
        "categories": categories,
        "location": location,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    location_id = request.GET.get("location")

    vendors = Vendor.objects.filter(category=category)
    selected_location = None

    if location_id:
        selected_location = Location.objects.filter(id=location_id).first()
        if selected_location:
            vendors = vendors.filter(location=selected_location)

    return render(request, "vendor_list.html", {
        "vendors": vendors,
        "selected_category": category,
        "selected_location": selected_location,
    })

def subcategory_page(request, slug):
    print(request.GET)
    location_id = request.GET.get("location")
    location = None

    if location_id and location_id.isdigit():
        location = Location.objects.get(id=int(location_id))

    category = get_object_or_404(Category, slug=slug)
    subcategories = SubCategory.objects.filter(category=category)

    return render(request, "level2_subcategories.html", {
        "category": category,
        "subcategories": subcategories,
        "location": location,
    })


