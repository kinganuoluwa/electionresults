from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import PollingBooth, Result, Ward


# class ResultCreateView(LoginRequiredMixin, CreateView):
    # model = PollingBooth
    # fields = ['ward', 'polling_unit', 'apc', 'pdp', 'accord', 'remarks']
    # template_name = 'add-results.html'
    # success_url = 'results'


@login_required
def total_result(request):
    apc_results = Result.objects.values('apc')
    pdp_results = Result.objects.values('pdp')
    accord_results = Result.objects.values('accord')

    # final result calculator
    def final_result(party_results, party_name):
        party_final_result = 0
        for result in party_results:
            results = result.get(party_name)
            party_final_result += results
        return party_final_result

    apc_final_result = final_result(apc_results, 'apc')
    pdp_final_result = final_result(pdp_results, 'pdp')
    accord_final_result = final_result(accord_results, 'accord')

    context = {
        'apc_final_result':apc_final_result,
        'pdp_final_result':pdp_final_result,
        'accord_final_result':accord_final_result,
    }
    return render(request, 'total_result.html', context)

class WardListView(LoginRequiredMixin, ListView):
    model = Ward
    context_object_name = 'wards'
    template_name = 'ward_list.html'

@login_required
def ward_detail(request, pk):
    ward = Ward.objects.get(id=pk)
    polling_units = PollingBooth.objects.filter(ward=ward)
    return render(request, 'ward_detail.html', {'ward':ward, 'polling_units':polling_units})
