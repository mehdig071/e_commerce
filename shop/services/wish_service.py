
from shop.models import Product  # Importez votre mod�le Product ici

class WishService:
    @staticmethod
    def add_product_to_wish(request, product_id):
        wish_products = request.session.get('wish', [])

        if product_id not in wish_products:
            wish_products.append(product_id)
            request.session['wish'] = wish_products

    @staticmethod
    def remove_product_from_wish(request, product_id):
        wish_products = request.session.get('wish', [])

        if product_id in wish_products:
            wish_products.remove(product_id)
            request.session['wish'] = wish_products

    @staticmethod
    def get_wished_products(request):
        return request.session.get('wish', [])

    @staticmethod
    def get_wished_products_details(request):
        wish_products = request.session.get('wish', [])
        wished_details = []

        for product_id in wish_products:
            product = Product.objects.filter(id=product_id).first()

            if product:
                wished_details.append({
                    'id': product.id,
                    'slug': product.slug,
                    'name': product.name,
                    'description': product.description,
                    'solde_price': product.solde_price,
                    'regular_price': product.regular_price,  # Typo corrected: 'solde_price'
                    'image': product.images.first().image.url,
                    'stock': product.stock,
                    # Ajoutez d'autres attributs du produit ici
                })

        return wished_details

    @staticmethod
    def clear_wished_products(request):
        request.session.pop('wish', None)

    