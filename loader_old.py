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
        files_path = [
            # 'databases/products.json',
            # 'databases/categories.json',
            # 'databases/collections.json',
            # 'databases/sliders.json',
        ]
        models = {
            'categories': Category,
            'collections': Collection,
            'sliders': Slider,
            'products': Product,
        }
        
        for file_path in files_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                entity = file_path.split('/')[1].split('.')[0]
                model = models.get(entity)
                
                if model : 
                    data = json.load(file)
                    if entity != 'products':
                        for item in data:
                            header = item.get('header', [])
                            rows = item.get('rows', [])
                            for row in rows: 
                                entry_data = {header[i]: row[i] for i in range(1, len(header))}   
                                model.objects.create(**entry_data)
                    else:
                        products = Product.objects.all()
                        products.delete()
                        for item in data:
                            header = item.get('header', [])
                            rows = item.get('rows', [])
                            header.pop(9)
                            for row in rows: 
                                images = json.loads(row.pop(9))
                                product_data = {header[i]: row[i] for i in range(1, len(header))}   
                                product = Product.objects.create(**product_data)
                                for image_path in images:   
                                    try:
                                        full_path = f'static/assets/{image_path}'
                                        with open(full_path, 'rb') as file:
                                            new_image = Image()
                                            new_image.product = product
                                            django_file = File(file)
                                            file_name = image_path.split("/").pop()
                                            new_image.image.save(file_name, django_file)
                                            
                                    except:
                                      print('An exception occurred')
                                # if int(row[0]) > 2:
                                #     break
                else:
                    print(f"Model '{entity}' not found.")
                
         
        
    except ImportError as exc:
        print(exc)
        sys.ecit(1)


if __name__ == '__main__':
    main()
