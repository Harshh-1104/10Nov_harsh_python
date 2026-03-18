from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Item

def item_list(request):
    return render(request, 'Q14/item_list.html')

@csrf_exempt
@require_http_methods(["GET"])
def api_item_list(request):
    items = Item.objects.all().values('id', 'name', 'description')
    return JsonResponse(list(items), safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def api_item_create(request):
    data = json.loads(request.body)
    item = Item.objects.create(name=data['name'], description=data['description'])
    return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})

@csrf_exempt
@require_http_methods(["PUT"])
def api_item_update(request, item_id):
    data = json.loads(request.body)
    item = Item.objects.get(id=item_id)
    item.name = data['name']
    item.description = data['description']
    item.save()
    return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})

@csrf_exempt
@require_http_methods(["DELETE"])
def api_item_delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return JsonResponse({'status': 'deleted'})
