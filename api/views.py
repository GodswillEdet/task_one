import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def user(request):
  header = {"Access-Control-Allow-Origin":"*"}
  data = { 
    "slackUsername": 'Geewill',
    "backend": True,
    "age": 22,
    "bio": 'Godswill is a Backend developer with a proven ability to develop efficient back-end services for web applications.'
    }

  return JsonResponse(data, headers=header)

@csrf_exempt
def math(request):
  if request.method == 'POST':
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    if body['operation_type'] == 'subtraction':
      result = body['x'] - body['y']
    elif body['operation_type'] == 'addition':
      result = body['x'] + body['y']
    elif body['operation_type'] == 'multiplication':
      result = body['x'] * body['y']
    elif body['operation_type'] == 'division':
      result = body['x'] / body['y']
    return JsonResponse({"slackUsername": "Geewill", "operation_type": body['operation_type'], "result": result})