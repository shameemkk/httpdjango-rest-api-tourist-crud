from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Destination
from .serializers import *
import requests
from .forms import destinationForm
from django.contrib import messages


# Create your views here.

#-------------------- api views --------------------

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
    
#-------------------- template views using api --------------------

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

def createDestination(request):
    if request.method == 'POST':
        api_url = 'http://127.0.0.1:8000/api/create/'
        form = destinationForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                # Prepare the data from the form
                data = {
                    'place_name': form.cleaned_data['place_name'],
                    'weather': form.cleaned_data['weather'],
                    'location': form.cleaned_data['location'],
                    'google_map_link': form.cleaned_data['google_map_link'],
                    'description': form.cleaned_data['description']
                }
                
                # Handle the image file
                files = {'image': request.FILES['image']} if 'image' in request.FILES else {}
                
                # Make the API request
                response = requests.post(api_url, data=data, files=files)
                
                if response.status_code == 201:  # 201 is standard status code for successful creation
                    messages.success(request, 'Destination created successfully!')
                    return redirect('index')
                else:
                    messages.error(request, 'Failed to create destination. Please try again.')
            
            except requests.RequestException as e:
                messages.error(request, f'Network error: {str(e)}')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Please check your form inputs.')
    
    return render(request, 'add-destination.html')






def editDestination(request, pk):
    try:
        if request.method == 'POST':
            api_url = f'http://127.0.0.1:8000/api/update/{pk}/'
            form = destinationForm(request.POST, request.FILES)
            
            if form.is_valid():
                # Prepare the data from the form
                data = {
                    'place_name': form.cleaned_data['place_name'],
                    'weather': form.cleaned_data['weather'],
                    'location': form.cleaned_data['location'],
                    'google_map_link': form.cleaned_data['google_map_link'],
                    'description': form.cleaned_data['description']
                }
                
                # Handle the image file
                files = {'image': request.FILES['image']} if 'image' in request.FILES else {}
                
                # Make the PUT request
                response = requests.put(api_url, data=data, files=files)
                
                if response.status_code == 200:
                    messages.success(request, 'Destination updated successfully!')
                    return redirect('index')
                else:
                    messages.error(request, f'Failed to update destination. Server returned status code: {response.status_code}')
            else:
                messages.error(request, 'Please correct the errors in the form.')
                return render(request, 'edit-destination.html', {'form': form})
              
        else:
            # GET request - fetch destination data
            api_url = f'http://127.0.0.1:8000/api/retrieve/{pk}/'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                return render(request, 'edit-destination.html', {'data': data})
            else:
                messages.error(request, 'Failed to retrieve destination data.')
                return redirect('index')
                
    except requests.RequestException as e:
        messages.error(request, f'Network error occurred: {str(e)}')
        return redirect('index')
    except Exception as e:
        messages.error(request, f'An unexpected error occurred: {str(e)}')
        return redirect('index')

    return render(request, 'edit-destination.html')

def viewDestination(request, pk):
    try:
        api_url = f'http://127.0.0.1:8000/api/retrieve/{pk}/'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            return render(request, 'view-destination.html', {'data': data})
        else:
            messages.error(request, 'Failed to retrieve destination data.')
            return redirect('index')
            
    except requests.RequestException as e:
        messages.error(request, f'Network error occurred: {str(e)}')
        return redirect('index')
    except Exception as e:
        messages.error(request, f'An unexpected error occurred: {str(e)}')
        return redirect('index')

def deleteDestination(request, pk):
    try:
        if request.method == 'POST':
            api_url = f'http://127.0.0.1:8000/api/delete/{pk}/'
            response = requests.delete(api_url)
            
            if response.status_code == 204:  # 204 is standard response for successful deletion
                messages.success(request, 'Destination deleted successfully!')
                return redirect('index')
            else:
                messages.error(request, f'Failed to delete destination. Server returned status code: {response.status_code}')
                return redirect('viewDestination', pk=pk)
                
    except requests.RequestException as e:
        messages.error(request, f'Network error occurred: {str(e)}')
    except Exception as e:
        messages.error(request, f'An unexpected error occurred: {str(e)}')
    
    return redirect('index')



