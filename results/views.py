from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Ward, PollingUnit


# class ResultCreateView(LoginRequiredMixin, CreateView):
    # model = PollingBooth
    # fields = ['ward', 'polling_unit', 'apc', 'pdp', 'accord', 'remarks']
    # template_name = 'add-results.html'
    # success_url = 'results'


# @login_required
# def results(request):
#     apc_results = PollingBooth.objects.values('apc')
#     pdp_results = PollingBooth.objects.values('pdp')

#     apc_final_result = 0
#     for result in apc_results:
#         results = result.get('apc')
#         apc_final_result += results

#     pdp_final_result = 0
#     for result in pdp_results:
#         results = result.get('pdp')
#         pdp_final_result += results

#     context = {
#         'apc_final_result':apc_final_result,
#         'pdp_final_result':pdp_final_result
#     }
#     return render(request, 'results.html', context)

class WardListView(LoginRequiredMixin, ListView):
    model = Ward
    context_object_name = 'wards'
    template_name = 'ward_list.html'

@login_required
def ward_detail(request, pk):
    ward = Ward.objects.get(id=pk)
    polling_units = PollingUnit.objects.filter(ward=ward)
    return render(request, 'ward_detail.html', {'ward':ward, 'polling_units':polling_units})
