from django.shortcuts import render

# Create your views here.
import json

from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# from api.models import Category
from api1.models import Company, Vacancy

def hello(request):
    return HttpResponse('hello')


def api(request):
    return HttpResponse('<h3 style="color: red">Here is your api</h3>')

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        # categories = Category.objects.filter(name='category 5')
        # categories = Category.objects.filter(name__startswith='cat')
        # categories = Category.objects.filter(name__endswith='ed')
        # categories = Category.objects.filter(name__contains='update')
        # categories = Category.objects.filter(id__in=[1, 2, 3, 4])
        companies = Company.objects.filter()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        # categories = Category.objects.filter(name='category 5')
        # categories = Category.objects.filter(name__startswith='cat')
        # categories = Category.objects.filter(name__endswith='ed')
        # categories = Category.objects.filter(name__contains='update')
        # categories = Category.objects.filter(id__in=[1, 2, 3, 4])
        vacancies = Vacancy.objects.filter()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            vacancy = Vacancy.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data['name']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


def vacancy_topten(request):
    vacancies = Vacancy.objects.filter().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def company_vacancy(request, company_id):
    vacancies = Vacancy.objects.all().filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

#def product(request):
    # p = NewProduct.objects.all()
    # p_json = [ps.to_json() for ps in p]
    # data = serializers.serialize("json", p)
    # d_data = serializers.deserialize("json", data)
    # return JsonResponse(p_json, safe=False)

# def category(request):
#     c = NewCategories.objects.all()
#     c_json = [cs.to_Json() for cs in c]
#     return JsonResponse(c_json, safe=False)
#
#
# def category_detail(request, category_id):
#     c = NewCategories.objects.all()
#     c_json = [cs.to_Json() for cs in c]
#     try:
#         return JsonResponse(c_json[category_id])
#     except:
#         return HttpResponse("SADSa")
#
#
# def product_detail(request, product_id):
    #for i in products:
    #    if i['id'] == product_id:
    #        return JsonResponse(i)
    # p = NewProduct.objects.all()
    # p_json = [ps.to_json() for ps in p]
    #
    # try:
    #     return JsonResponse(p_json[product_id])
    # except:
    #     return HttpResponse('<h3 style= "color:blue;">Hi, man! It could not be found.</h3>')





















#
#
# products = [
#     {
#         'id': 1,
#         'name': 'Microsoft Surface Laptop Go - 12.4" Touchscreen - Intel Core i5 - 8GB Memory - 128GB SSD - Ice Blue',
#         'image': 'https://images-na.ssl-images-amazon.com/images/I/61Cycl-ymmL._AC_SL1500_.jpg',
#         'rating': '4.6',
#         'link': 'https://www.amazon.com/Microsoft-Surface-Laptop-Go-Touchscreen/dp/B08GZKZ95X/ref=sr_1_7?dchild=1&keywords=laptop&qid=1614102483&sr=8-7',
#         'price': 674,
#         'description': 'Surface Laptop Go display has rounded corners within a standard rectangle. When measured as a standard rectangular shape the screen is 12.45” diagonally (actual viewable area is less). Some accessories and software sold separately.',
#         'full': 'Make the most of every day with the sleek style, performance, and all-day battery life you need in our lightest Surface Laptop, all at an exceptional value. Ultra-light and portable profile, the apps you use every day, premium materials, and a choice of must-have colors will make this your go-to laptop.'
#     },
#     {
#         'id': 2,
#         'name': 'Razer Blade 15 Base Gaming Laptop 2020: Intel Core i7-10750H 6-Core, NVIDIA GeForce GTX 1660 Ti, 15.6" FHD 1080p 144Hz, 16GB RAM, 256GB SSD, CNC Aluminum, Chroma RGB Lighting, Thunderbolt 3, Black',
#         'image': 'https://images-na.ssl-images-amazon.com/images/I/71r5254QPZL._AC_SL1500_.jpg',
#         'rating': '4.6',
#         'link': 'https://www.amazon.com/Razer-Blade-Base-Gaming-Laptop/dp/B086MGY9TZ/ref=sr_1_2?dchild=1&keywords=laptop&qid=1614102483&sr=8-2',
#         'price': 1370.78,
#         'description': 'More power: The 10th Gen Intel Core i7-10750H processor provides the ultimate level of performance with up to 5.0 GHz max turbo and 6 cores.',
#         'full': 'Supercharger: The NVIDIA GeForce GTX 1660 Ti graphics is a blazing-fast supercharger for today’s most popular games More frames: Incredible performance paired with the fast 144Hz 15. 6" full HD thin bezel display helps edge out the win.'
#     },
#     {
#         'id': 3,
#         'name': 'Acer Nitro 5 Gaming Laptop, 10th Gen Intel Core i5-10300H,NVIDIA GeForce GTX 1650 Ti, 15.6" Full HD IPS 144Hz Display, 8GB DDR4,256GB NVMe SSD,WiFi 6, DTS X Ultra,Backlit Keyboard,AN515-55-59KS',
#         'image': 'https://images-na.ssl-images-amazon.com/images/I/81Z8NvO2TFL._AC_SL1500_.jpg',
#         'rating': '4.6',
#         'link': 'https://images-na.ssl-images-amazon.com/images/I/81Z8NvO2TFL._AC_SL1500_.jpg',
#         'price': 820.56,
#         'description': '10th Generation Intel Core i5-10300H Processor (Up to 4.5GHz)',
#         'full': '10th Generation Intel Core i5-10300H Processor (Up to 4.5GHz). 15" Full HD Widescreen IPS LED-backlit 144Hz Refresh Display | NVIDIA GeForce GTX 1650 Ti Graphics with 4 GB of dedicated GDDR6 VRAM'
#     },
#     {
#         'id': 4,
#         'name': 'Lenovo IdeaPad 3 Intel i5-1035G1 Quad Core 12GB RAM 256GB SSD 15.6-inch Touch Screen Laptop',
#         'image': 'https://images-na.ssl-images-amazon.com/images/I/61DrCbSkM4L._AC_SL1500_.jpg',
#         'rating': '4.6',
#         'link': 'https://www.amazon.com/Lenovo-IdeaPad-i5-1035G1-15-6-inch-Screen/dp/B08NXSJVCR/ref=sr_1_4?dchild=1&keywords=laptop&qid=1614102483&sr=8-4',
#         'price': 490,
#         'description': '10th generation Intel Core i5-1035G1 processor. Dual-core, four-way intelligent processing performance. Intel Turbo Boost Technology delivers dynamic extra power when you need it, while increasing energy efficiency when you dont',
#         'full': '10th generation Intel Core i5-1035G1 processor. Dual-core, four-way intelligent processing performance. Intel Turbo Boost Technology delivers dynamic extra power when you need it, while increasing energy efficiency when you dont.15.6-inch touchscreen for convenient control. Tap, tap, swipe and get the most out of Windows 10. HD TruBrite technology that expands color and clarity. 1366 x 768 typical HD resolution. Supports 720p content. Energy efficient LED backlighting.'
#     },
#     {
#         'id': 5,
#         'name': 'ASUS F512JA-AS34 VivoBook 15 Thin and Light Laptop, 15.6” FHD Display, Intel i3-1005G1 CPU, 8GB RAM, 128GB SSD, Backlit Keyboard, Fingerprint, Windows 10 Home in S Mode, Slate Gray',
#         'image': 'https://images-na.ssl-images-amazon.com/images/I/81fstJkUlaL._AC_SL1500_.jpg',
#         'rating': '4.5',
#         'link': 'https://www.amazon.com/ASUS-F512JA-AS34-VivoBook-i3-1005G1-Fingerprint/dp/B0869L1326/ref=sr_1_5?dchild=1&keywords=laptop&qid=1614102483&sr=8-5',
#         'price': 395,
#         'description': '15.6 inch Full HD (1920x1080) 4-way NanoEdge bezel display with a stunning 88% screen-to-body ratio',
#         'full': '15.6 inch Full HD (1920x1080) 4-way NanoEdge bezel display with a stunning 88% screen-to-body ratio.Compatible with Google Classroom; run Google Classroom on Microsoft Edge or Internet Explorer 11Latest 10th Gen Intel Core i3-1005G1 CPU (4M Cache, up to 3.4 GHz)'
#     }
#
# ];
#
# category_list = [
#     {
#         'name': 'Laptops'
#     },
#     {
#         'name': 'New Gen Laptops'
#     },
#     {
#         'name': 'Phone'
#     }
# ]

