from shop.models.Setting import Setting
from shop.models.Social import Social
from shop.models.Page import Page
from shop.models.Category import Category
from shop.models.Navcollection import Navcollection
from shop.services.cart_service import CartService



def site_settings(request):
    site_settings = Setting.objects.first()
    socials = Social.objects.all()
    head_pages = Page.objects.filter(is_head=True)
    foot_pages = Page.objects.filter(is_foot=True)
    mega_categories = Category.objects.filter(is_mega=True)
    navs = Navcollection.objects.all()[:3]
    cart_data = CartService.get_cart_details(request)
    
    my_socials = []
    my_head_pages = []
    my_foot_pages = []
    my_mega_categories = []
    nav_collections = []
    
    for nav_item in navs:
        nav_collections.append({
            'title': nav_item.title,
            'description': nav_item.description,
            'button_text': nav_item.button_text,
            'button_link': nav_item.button_link,
            'imageUrl': nav_item.image.url,
        })
    for item in socials:
        my_socials.append({
            'name': item.name,
            'icon': item.icon,
            'link': item.link,
        })
    for item in head_pages:
        my_head_pages.append({
            'name': item.name,
            'slug': item.slug
        })
    for item in foot_pages:
        my_foot_pages.append({
            'name': item.name,
            'slug': item.slug
        })
    for category in mega_categories: 
        products = category.product_set.all()[:4]
        product_arr = []
        
        for product in products:
            image = None
            if product.images.exists():
                image = product.images.first()
                product_arr.append({
                    'name': product.name, 
                    'slug': product.slug,
                    'image': image.image.url})
        
        
        my_mega_categories.append({
            'name': category.name,
            'products': product_arr
        })
        
    context = {
        'name' : site_settings.name,
        'description' : site_settings.description,
        'email' : site_settings.email,
        'currency' : site_settings.currency,
        'phone' : site_settings.phone,
        'street' : site_settings.street,
        'city' : site_settings.city,
        'code_postal' : site_settings.code_postal,
        'state' : site_settings.state,
        'copyright' : site_settings.copyright,
        'socials': my_socials,
        'head_pages': my_head_pages,
        'foot_pages': my_foot_pages,
        'mega_categories': my_mega_categories,
        'nav_collections': nav_collections,
        'cart_data': cart_data,
    }
    request.session.update(context)
    
    return context