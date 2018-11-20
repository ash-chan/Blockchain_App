from django.shortcuts import render
from django.views import generic
from django.db.models import *
from .models import Mentor, Mentee


def overview(request):
    total_inv_zco = Mentor.objects.aggregate(sum=Sum('inv_zco'))['sum']
    total_inv_usd = Mentor.objects.aggregate(sum=Sum('inv_usd'))['sum']
    mentee_count = Mentee.objects.count()
    next_grad_date = Mentee.objects.latest('grad_date').grad_date
    return render(request, 'dashboard/overview.html',
                  {'total_inv_zco': total_inv_zco,
                    'total_inv_usd': total_inv_usd,
                   'mentee_count': mentee_count,
                   'next_grad_date': next_grad_date}
                  )

def batches(request):
    return render(request, 'dashboard/current_batches.html')

def batchinfo(request):
    return render(request, 'dashboard/mixed.html')
