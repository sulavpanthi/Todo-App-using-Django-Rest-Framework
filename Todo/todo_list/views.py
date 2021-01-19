from django.shortcuts import render

from .models import TodoList
from .serializers import TodoListSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todo_list_view(request, list_id=None):
    if request.method == 'GET':

        if list_id != None:
            try:
                todo_list_all = TodoList.objects.get(id = list_id)
                serializer = TodoListSerializer(instance=todo_list_all)
            except TodoList.DoesNotExist:
                return Response({"error":"Does not exist"}, status=404)

        else:
            todo_list_all = TodoList.objects.all()
            serializer = TodoListSerializer(instance=todo_list_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoListSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print("serializer list name", serializer['list_name'])
        list_name = serializer['list_name']

        obj = TodoList.objects.create(list_name = list_name)
        return Response(serializer.data, status=201)
    
    elif request.method == 'PUT':
        try:
            obj = TodoList.objects.get(id = list_id)
        except TodoList.DoesNotExist:
            return Response({'error': 'Does not exist'}, status=404)

        serializer = TodoListSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        list_name = serializer.validated_data['list_name']

        obj.list_name = list_name
        obj.save()

        return Response({'status': 'ok put'})

    elif request.method == 'DELETE':
        try:
            obj = TodoList.objects.get(id = list_id)
        except TodoList.DoesNotExist:
            return Response({'error': 'Does not exist'}, status=404)

        obj.delete()
        return Response({'status': 'ok deleted'})

    else:
        return Response({'status': 'bad request'}, status=400)
    


