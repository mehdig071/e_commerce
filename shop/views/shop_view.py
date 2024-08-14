from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from shop.models.Slider import Slider
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Page import Page
from shop.models.Category import Category

def index(request):
    sliders = Slider.objects.all()
    collections = Collection.objects.all()
    
    best_sellers = Product.objects.filter(is_best_seller=True)[:8]
    new_arrivals = Product.objects.filter(is_new_arrival=True)[:8]
    featured = Product.objects.filter(is_featured=True)[:8]
    special_offers = Product.objects.filter(is_special_offer=True)[:8]
    
    return render(request, 'shop/index.html', {
        'sliders': sliders, 
        'collections':collections,
        'new_arrivals':new_arrivals,
        'best_sellers':best_sellers,
        'featured':featured,
        'special_offers':special_offers,
        })
    
    
def display_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    return render(request, 'shop/page.html', {
        'page': page, 
        })
    
    
def display_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    return render(request, 'shop/single_product.html', {
        'product': product, 
        })

    
def shop(request):
    # Récupération de tous les produits
    
    categories = Category.objects.all()

    # Récupération du paramètre de tri par prix depuis la session, avec une valeur par défaut de 'asc'
    sort_by_price = request.session.get('sort-price', 'asc')

    # Récupération du nombre d'éléments à afficher par page depuis la session, avec une valeur par défaut de 6
    showing = int(request.session.get('showing', 6))
    
    
    category_id = request.GET.get('category_id', 'all')
    
    if category_id and category_id != 'all':
        category = get_object_or_404(Category, id=category_id)
        products = category.product_set.all()
    else:
        products = Product.objects.all()

    # Mise à jour du nombre d'éléments à afficher par page si présent dans les paramètres de requête
    if 'showing' in request.GET and request.GET['showing'] != "":
        showing = int(request.GET['showing'])
        request.session['showing'] = showing
        

    # Mise à jour du paramètre de tri par prix si présent dans les paramètres de requête
    if 'sort-price' in request.GET and request.GET['sort-price'] != "":
        sort_by_price = request.GET['sort-price']
        request.session['sort-price'] = sort_by_price

    # Récupération du mode d'affichage (grid/list) depuis la session, avec une valeur par défaut de 'grid'
    display = request.session.get('display', 'grid')

    # Mise à jour du mode d'affichage si présent dans les paramètres de requête
    if 'display' in request.GET:
        display = request.GET['display']
        request.session['display'] = display
    
    # Tri des produits en fonction du paramètre sort_by_price
    if sort_by_price == "asc":
        products = products.order_by('solde_price')
    elif sort_by_price == "desc":
        products = products.order_by('-solde_price')

    # Utilisation de la pagination avec le nombre d'éléments à afficher par page
    paginator = Paginator(products, showing)

    try:
        # Tentative de récupération de la page demandée
        products_page = paginator.page(request.GET.get('page', 1))
    except (PageNotAnInteger, EmptyPage):
        # En cas d'erreur de pagination, affichez la première page
        products_page = paginator.page(1)

    return render(request, 'shop/shop_list.html', {
        'products': products_page,
        'categories': categories,
        'display': display,
        'sort_by_price': sort_by_price,
        'default_category_id': int(category_id) if category_id.isdigit() else category_id,
    })