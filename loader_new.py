#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
import django
from django.core.files import File


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    try:
        from shop.models import Category, Collection, Slider, Product, Image
        from shop.models.Navcollection import Navcollection
        from shop.models.Social import Social
        from shop.models.Carrier import Carrier
        from shop.models.Setting import Setting
        from shop.models.Page import Page
        
        files_path = [
            #'databases/settings.json',
            #'databases/products.json',
            #'databases/images.json',
            #'databases/carriers.json',
            #'databases/navcollections.json',
            #'databases/socials.json',
            #'databases/categories.json',
            #'databases/collections.json',
            #'databases/sliders.json',
            #'databases/product_category.json',
            'databases/pages.json',
        ]
        models = {
            #'categories': Category,
            #'collections': Collection,
            #'sliders': Slider,
            #'products': Product,
            #'images': Image,
            #'carriers': Carrier,
            #'navcollections': Navcollection,
            #'settings': Setting,
            #'socials': Social,
            #'product_category': 'product_category',
            'pages': Page
        }
        
        for file_path in files_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                entity = file_path.split('/')[1].split('.')[0]
                model = models.get(entity)
                
                if model : 
                    data = json.load(file)
                    if entity == 'product_category':
                        for item in data:
                            header = item.get('header', [])
                            rows = item.get('rows', [])
                            for row in rows: 
                                entry_data = {header[i]: row[i] for i in range(len(header))}   
                                category_id = entry_data.get('category_id', None)
                                product_id = entry_data.get('product_id', None)
                                
                                if category_id is not None and product_id is not None:
                                    try:
                                        product = Product.objects.get(id=product_id)
                                    except Product.DoesNotExist:
                                        # Gérer le cas où le produit avec l'ID spécifié n'existe pas
                                        print(f"Le produit avec l'ID {product_id} n'existe pas.")
                                        continue

                                    product.categories.add(category_id)
                                    
                                else:
                                    print("Les données ne contiennent pas 'category_id' ou 'product_id'.")
                    else:
                        for item in data:
                            header = item.get('header', [])
                            rows = item.get('rows', [])
                            for row in rows: 
                                entry_data = {header[i]: row[i] for i in range(len(header))}   
                                model.objects.create(**entry_data)
                   
                else:
                    print(f"Model '{entity}' not found.")
                
         
        
    except ImportError as exc:
        print(exc)
        sys.ecit(1)


if __name__ == '__main__':
    main()
