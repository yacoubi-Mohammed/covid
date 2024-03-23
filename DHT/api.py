"""from .models import Patient
from .serializers import DHT11serialize
from rest_framework import status, generics
from rest_framework.response import Response
import rest_framework
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
@api_view(['GET','POST'])
def Dlist(request):
    all_data = Patient.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({'data': data})

class Dhtviews(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = DHT11serialize
"""
"""@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True)
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            derniere_temperature = Dht11.objects.last().temp
            print(derniere_temperature)
            if (derniere_temperature > 10):
                subject = 'Alerte'
                message = 'Il y a une alerte importante sur votre Capteur la température dépasse le seuil'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['asmazehmoune2@gmail.com']
                send_mail(subject, message, email_from, recipient_list)
                return Response(serial.data, status=status.HTTP_201_CREATED)
            else : return Response(serial.id, status=status.HTTP_400_CREATED)"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import DHT11serialize

class Dhtviews(APIView):
    def get(self, request, *args, **kwargs):
        # Récupérer tous les objets Patient de la base de données
        queryset = Patient.objects.all()
        # Serializer les données
        serializer = DHT11serialize(queryset, many=True)
        # Retourner la réponse avec les données sérialisées
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Sérialiser les données reçues dans la requête POST
        serializer = DHT11serialize(data=request.data)
        if serializer.is_valid():
            # Enregistrer les données dans la base de données si elles sont valides
            serializer.save()
            # Retourner une réponse de succès avec les données sérialisées
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retourner une réponse d'erreur si les données ne sont pas valides
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
