import requests

response = requests.get('https://fakestoreapi.com/products/categories')
categories = response.json()

print("В магазине имеется следующая категория товаров:")
for i, category in enumerate(categories):
    print(f"{i + 1}. {category}")

cat_product = int(input("Информацию о какой категории товара Вы хотите получить? Введите номер категории: ")) - 1

if 0 <= cat_product < len(categories):
    selected_category = categories[cat_product]
    response = requests.get(f'https://fakestoreapi.com/products/category/{selected_category}')
    products = response.json()
    print(f"\nТовары в категории: '{selected_category}':")
    for product in products:
        print(f"\nНазвание: {product['title']}")
        print(f"Цена: ${product['price']}")
        print(f"Описание: {product['description']}")
        print(f"Рейтинг: {product['rating']['rate']} (на основе {product['rating']['count']} отзывов)")
else:
    print("Нет такого номера категории!")