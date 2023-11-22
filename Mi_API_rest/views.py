from django.http import JsonResponse
from .models import Mi_API_rest as API
from .serializers import APISerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def Mi_API_rest(request):

    if request.method == 'GET':
        # obtener objetos
        apis = API.objects.all()

        # crea un nuevo serializer
        serializer = APISerializer(apis, many=True)

        # retorna el valor en tipo json
        return JsonResponse({'valores': serializer.data}) 
    
    if request.method == 'POST':
        # crea un nuevo serializer
        serializer = APISerializer(data=request.data)

        if serializer.is_valid():
            # guarda objetos
            serializer.save()

            # retorna el valor en tipo json
            return Response(serializer.data, status=status.HTTP_201_CREATED)