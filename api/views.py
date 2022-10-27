from django.http import JsonResponse

def endpoint(request):
    data = { "slackUsername": 'Geewill',
             "backend": True, 
             "age": 22,
              "bio": 'Godswill is a Backend developer with a proven ability to develop efficient back-end services for web applications. Experienced in Python, Django, Django REST framework.'  
            }

    return JsonResponse(data, safe=False)