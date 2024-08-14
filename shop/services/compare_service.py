
from shop.models import Product  # Importez votre mod�le Product ici

class CompareService:
    @staticmethod
    def add_product_to_compare(request, product_id):
        compare_products = request.session.get('compare', [])

        if product_id not in compare_products:
            compare_products.append(product_id)
            request.session['compare'] = compare_products

    @staticmethod
    def remove_product_from_compare(request, product_id):
        compare_products = request.session.get('compare', [])

        if product_id in compare_products:
            compare_products.remove(product_id)
            request.session['compare'] = compare_products

    @staticmethod
    def get_compared_products(request):
        return request.session.get('compare', [])

    @staticmethod
    def get_compared_products_details(request):
        compare_products = request.session.get('compare', [])
        compared_details = []

        for product_id in compare_products:
            product = Product.objects.filter(id=product_id).first()

            if product:
                compared_details.append({
                    'id': product.id,
                    'slug': product.slug,
                    'name': product.name,
                    'description': product.description,
                    'solde_price': product.solde_price,
                    'regular_price': product.regular_price,  # Typo corrected: 'solde_price'
                    'images': product.images,
                    'stock': product.stock,
                    # Ajoutez d'autres attributs du produit ici
                })

        return compared_details

    @staticmethod
    def clear_compared_products(request):
        request.session.pop('compare', None)

    