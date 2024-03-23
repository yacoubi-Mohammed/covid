from django.shortcuts import render

from django.utils import timezone
import csv
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta
import datetime
#import telepot
from .forms import FormChoice
from .models import Patient
def dht_tab(request):
    tab = Patient.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)

def test(request):
    return HttpResponse('iot project')

def table_view(request):
    data = Patient.objects.all()  # récupérer toutes les données du modèle
    data = Patient.objects.filter(id__gte=1, id__lte=17)
    # form =FormChoice()
    if request.method == 'POST':
        form = FormChoice(request.POST)
        if form.is_valid():
            # print(request.POST.get('select'))
            num_rows = str(request.POST.get('select'))
            print(num_rows)
            if num_rows is not None:
                # Filtrer les options en fonction de la valeur sélectionnée
                start, end = map(int, num_rows.split('-'))
                data = Patient.objects.filter(id__gte=start, id__lte=end)
                return render(request, 'table.html', {'form': form, 'data': data})

    else:
        form = FormChoice()

    return render(request, 'table.html', {'form': form, 'data': data})

def table(request):
    derniere_ligne = Patient.objects.last()
    derniere_date = Patient.objects.last().dt
    delta_temps = timezone.now() - derniere_date
    difference_minutes = delta_temps.seconds // 60
    temps_ecoule = ' il y a ' + str(difference_minutes) + ' min'
    if difference_minutes > 60:
        temps_ecoule = 'il y ' + str(difference_minutes // 60) + 'h' + str(difference_minutes % 60) + 'min'
    valeurs = {'date': temps_ecoule, 'id': derniere_ligne.id, 'temp': derniere_ligne.temp, 'oxygene_level': derniere_ligne.oxygene_level,'respiratoryRate': derniere_ligne.respiratoryRate, 'heartRate': derniere_ligne.heartRate}
    return render(request, 'value.html', {'valeurs': valeurs})

def download_csv(request):
    model_values = Patient.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patient.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'oxygene_level', 'respiratoryRate', 'heartRate', 'dt'])
    for patient in model_values:
        writer.writerow([patient.id, patient.temp, patient.oxygene_level, patient.respiratoryRate, patient.heartRate, patient.dt])
    return response


#pour afficher navbar de template
def index_view(request):
    return render(request, 'index.html')

#pour afficher les graphes
def graphique(request):
    return render(request, 'Chart.html')

# récupérer toutes les valeurs de température et humidité sous forme d'un fichier json
from django.http import JsonResponse
from .models import Patient

def chart_data(request):
    patients = Patient.objects.all()

    data = {
        'temps': [patient.dt for patient in patients],
        'temperature': [patient.temp for patient in patients],
        'oxygene_level': [patient.oxygene_level for patient in patients],
        'respiratoryRate': [patient.respiratoryRate for patient in patients],
        'heartRate': [patient.heartRate for patient in patients]
    }
    return JsonResponse(data)

# pour récupérer les valeurs de température et humidité des dernières 24 heures et les envoyer sous forme JSON
from django.http import JsonResponse
from django.utils import timezone
from .models import Patient


def chart_data_jour(request):
    now = timezone.now()

    # Récupérer l'heure il y a 24 heures
    last_24_hours = now - timezone.timedelta(hours=24)

    # Récupérer tous les objets de Patient créés au cours des 24 dernières heures
    patients = Patient.objects.filter(dt__range=(last_24_hours, now))

    data = {
        'temps': [patient.dt for patient in patients],
        'temperature': [patient.temp for patient in patients],
        'oxygene_level': [patient.oxygene_level for patient in patients],
        'respiratoryRate': [patient.respiratoryRate for patient in patients],
        'heartRate': [patient.heartRate for patient in patients]
    }
    return JsonResponse(data)


# pour récupérer les valeurs de température et humidité de la dernière semaine et les envoyer sous forme JSON
from django.http import JsonResponse
from django.utils import timezone
import datetime
from .models import Patient


def chart_data_semaine(request):
    # calcul de la date de début de la semaine dernière
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=7)

    # filtrer les enregistrements créés depuis le début de la semaine dernière
    patients = Patient.objects.filter(dt__gte=date_debut_semaine)

    data = {
        'temps': [patient.dt for patient in patients],
        'temperature': [patient.temp for patient in patients],
        'oxygene_level': [patient.oxygene_level for patient in patients],
        'respiratoryRate': [patient.respiratoryRate for patient in patients],
        'heartRate': [patient.heartRate for patient in patients]
    }

    return JsonResponse(data)


# pour récupérer les valeurs de température et humidité du dernier mois et les envoyer sous forme JSON
from django.http import JsonResponse
from django.utils import timezone
import datetime
from .models import Patient


def chart_data_mois(request):
    # calcul de la date de début du mois dernier
    date_debut_mois = timezone.now().date() - datetime.timedelta(days=30)

    # filtrer les enregistrements créés depuis le début du mois dernier
    patients = Patient.objects.filter(dt__gte=date_debut_mois)

    data = {
        'temps': [patient.dt for patient in patients],
        'temperature': [patient.temp for patient in patients],
        'oxygene_level': [patient.oxygene_level for patient in patients],
        'respiratoryRate': [patient.respiratoryRate for patient in patients],
        'heartRate': [patient.heartRate for patient in patients]
    }

    return JsonResponse(data)


def sendtele():
    token = '6963081452:AAGOcK18Sfo5ktc8tNn31f6Ii3dpNEfBlvo'
    rece_id = 1414583679
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, 'la température depasse la normale')
    print(bot.sendMessage(rece_id, 'OK.'))
