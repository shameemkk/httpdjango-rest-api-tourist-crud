from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Destination
from .serializers import *
import requests


# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset=Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes=[AllowAny]
class RetrieveView(generics.RetrieveAPIView):
    queryset = Destination.objects.all() 
    serializer_class = DestinationSerializer

class RetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class=DestinationSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class=DestinationSerializer

class Search(generics.ListAPIView):
    serializer_class = DestinationSerializer
    def get_queryset(self):
        name=self.kwargs.get('search')
        return Destination.objects.filter(place_name__icontains=name)
    


def index(request):
    def fetch_data(api_url):
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return  None

    if request.method == 'POST':
        search = request.POST.get('search')
        api_url = f'http://127.0.0.1:8000/api/search/{search}/'
        data = fetch_data(api_url)
    else:
        api_url = 'http://127.0.0.1:8000/api/create/'
        data = fetch_data(api_url)
    return render(request, 'index.html', {'data': data})
