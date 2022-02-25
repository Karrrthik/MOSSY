from django.shortcuts import render, redirect
from .mossy import *
import os
from .models import Files
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serailizers import FileSerializer


# def moss(request):
#     if (request.method == 'POST'):
#         end = os.path.splitext(request.FILES['code'].name)
#         file_path = "files/"
#         request.FILES['code'].name = str(end[0]) + str(len([name for name in os.listdir(file_path) if os.path.isfile(file_path + name)])+1) + str(end[1])
#         f = request.FILES['code']
#         Files.objects.create(file=f, filename=f.name)
#         url = check(f.name) #does this work? 
#         return redirect(url)
#     return render(request, 'mossy.html')


@api_view(['GET', 'POST'])
def moss(request):
    if (request.method == 'GET'):
        data = Files.objects.all()
        serializer = FileSerializer(data, context={'request' : request}, many=True)
        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = FileSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

