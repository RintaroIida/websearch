from django.shortcuts import render, get_object_or_404, redirect 
from .models import Product, Category, BikeType
from .forms import ProductForm, SearchForm 
from django.core.paginator import Paginator 

 
def product_create(request): 
    if request.method == 'POST': 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('product_list') 
    else: 
        form = ProductForm() 
    return render(request, 'product_form.html', {'form': form}) 
 
def product_detail(request, pk): 
    product = get_object_or_404(Product, pk=pk) 
    return render(request, 'product_detail.html', {'product': product}) 
 
def product_update(request, pk): 
    product = get_object_or_404(Product, pk=pk) 
    if request.method == 'POST': 
        form = ProductForm(request.POST, instance=product) 
        if form.is_valid(): 
            form.save() 
            return redirect('product_detail', pk=product.pk) 
    else: 
        form = ProductForm(instance=product) 
    return  render(request,  'product_form.html',  {'form':  form,  'product': product})

def product_delete(request, pk): 
    product = get_object_or_404(Product, pk=pk) 
    if request.method == 'POST': 
        product.delete() 
        return redirect('product_list') 
    return render(request, 'product_confirm_delete.html', {'product': product}) 
 
def product_list(request, category_id=None):
    # カテゴリ一覧を取得
    categories = Category.objects.all()
    
    # 初期状態で全製品を表示
    all_products = Product.objects.all()  # 全製品を取得
    
    # カテゴリが指定されていれば、そのカテゴリの製品を取得
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
    else:
        category = None
        products = all_products

    # ページネーションの設定(カードをいじるやつ)
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'product_list.html', {
        'categories': categories,  # カテゴリ一覧
        'category': category,  # 現在選択されているカテゴリ
        'products': products,  # 表示する製品（フィルタリングされたもの）
        'all_products': all_products,  # すべての製品
        'page_obj': page_obj,  # ページネーション
        'selected_category': category_id,
    })

 
def search_view(request):
    query = request.GET.get('query', '')  # 商品名
    category_id = request.GET.get('category', '')  # メーカー
    bike_type_id = request.GET.get('bike_type', '')  # バイクタイプ
    min_price = request.GET.get('min_price', '')  # 最低価格
    max_price = request.GET.get('max_price', '')  # 最高価格
    displacement_range = request.GET.get('displacement', '')  # 排気量の選択肢

    products = Product.objects.all()

    # 商品名でフィルタリング
    if query:
        products = products.filter(name__icontains=query)

    # メーカー（カテゴリ）でフィルタリング
    if category_id:
        products = products.filter(category_id=category_id)

    # バイクタイプでフィルタリング
    if bike_type_id:
        products = products.filter(bike_type_id=bike_type_id)

    # 価格でフィルタリング
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # 排気量でフィルタリング
    if displacement_range:
        if displacement_range == '50':
            products = products.filter(displacement__lte=50)
        elif displacement_range == '125':
            products = products.filter(displacement__gte=51, displacement__lte=125)
        elif displacement_range == '250':
            products = products.filter(displacement__gte=126, displacement__lte=250)
        elif displacement_range == '400':
            products = products.filter(displacement__gte=251, displacement__lte=400)
        elif displacement_range == '1000':
            products = products.filter(displacement__gte=401, displacement__lte=1000)
        elif displacement_range == '1000plus':
            products = products.filter(displacement__gte=1000)

    # ページネーション（例: 12件ずつ表示）
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # カテゴリ（メーカー）とバイクタイプのリストを取得
    categories = Category.objects.all()
    bike_types = BikeType.objects.all()

    return render(request, 'search.html', {
        'page_obj': page_obj,
        'categories': categories,
        'bike_types': bike_types,
        'query': query,
        'selected_category': category_id,
        'selected_bike_type': bike_type_id,
        'min_price': min_price,
        'max_price': max_price,
        'selected_displacement': displacement_range,
    })

def performance_view(request):
    return render(request, 'performance.html')

def about_site_view(request):
    return render(request, 'about_site.html')