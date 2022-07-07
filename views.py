from django.http.response import JsonResponse
from datetime import datetime
from django.db.models.functions import Extract, Trunc
from django.db.models import DateTimeField
from vuln.models import Experiment
from django.core import serializers

def vuln_extract(request):
    payload = request.GET.get('lookup_name')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__year=Extract('end_datetime', payload))
    return JsonResponse({"res": serializers.serialize("json", experiments)})

def vuln_trunc(request):
    payload = request.GET.get('kind')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__date=Trunc('start_datetime', payload))
    return JsonResponse({"res": serializers.serialize("json", experiments)})
