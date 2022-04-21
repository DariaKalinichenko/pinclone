from django.http import HttpResponse

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница со списком постов
def posts_list(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном посте;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Пост {pk}') 