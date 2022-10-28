from django.http import JsonResponse

def user(request):
    header = {"Access-Control-Allow-Origin":"*"}
    data = { "slackUsername": 'Geewill',
             "backend": True,
             "age": 22,
              "bio": 'Godswill is a Backend developer with a proven ability to develop efficient back-end services for web applications.'
            }

    return JsonResponse(data, headers=header)