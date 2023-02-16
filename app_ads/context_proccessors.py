from app_ads.models import Category


def load_menu(request):
    try:
        root_category = Category.objects.get(id=1)
        sub_categories = root_category.get_descendants(include_self=False)
        base_categories = Category.objects.filter(parent_id=root_category.id).only('name', 'slug')
    except AttributeError as exc:
        sub_categories = {}
        base_categories = {}
    return {'main_menu': sub_categories, 'base_menu': base_categories}