from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import jwt
from django.conf import settings

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Custom middleware logic here
        EXAMPT_PATH = ['/login/', '/inserthotel/']
        try:
          if request.path in EXAMPT_PATH:
            return None
          json_web_token =request.headers.get('Authorization').split()[1]
          decoded_json_web_tobken = jwt.decode(json_web_token,settings.JWT_SECRET_KEY,algorithms=["HS256"])
          request.hotel_id = decoded_json_web_tobken
        except IndentationError as e:
            return JsonResponse({'error':f'there is not web token {e}'})
        except AttributeError as e :
          return JsonResponse({'error':f'check your headers {e}'})
        except Exception as e:
          return JsonResponse({'error':f'jwt error {e}'})