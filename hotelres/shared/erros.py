from django.http import JsonResponse
class DataBaseErrors:
  class DataBaseExeption(Exception):
    pass
  class FormatingError(DataBaseExeption):
    pass
  class ExecuteQuery(DataBaseExeption):
    pass
  class SelectOneError(DataBaseExeption):
    pass
  class SelectAll(DataBaseExeption):
    pass
  class AddinRoomsError(DataBaseExeption):
    pass
  class UpdatingRoomsError(DataBaseExeption):
    pass

def handel_errors(error_type,custom_comment):
  if isinstance(error_type,DataBaseErrors.FormatingError):
    return JsonResponse({'error':str(error_type)},status=400)
  elif isinstance(error_type,DataBaseErrors.ExecuteQuery):
    return JsonResponse({'error':str(error_type)},status=400)
  elif isinstance(error_type,DataBaseErrors.SelectOneError):
    return JsonResponse({'error':str(error_type)},status=400)
  elif isinstance(error_type,DataBaseErrors.SelectAll):
    return JsonResponse({'error':str(error_type)},status=400)
  elif isinstance(error_type,DataBaseErrors.AddinRoomsError):
    return JsonResponse({'error':str(error_type)},status=400)
  elif isinstance(error_type,DataBaseErrors.UpdatingRoomsError):
    return JsonResponse({'error':str(error_type)},status=400)
  else:
    return JsonResponse({'error':f'there seems to be error --> {custom_comment} {str(error_type)}'},status=400)
    