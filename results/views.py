from django.shortcuts import render
from django.views.generic import ListView
from .models import Result, Ward


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

    results = Result.objects.all()
    context = {
        'apc_final_result':apc_final_result,
        'pdp_final_result':pdp_final_result,
        'accord_final_result':accord_final_result,
        'results':results
    }
    return render(request, 'total_result.html', context)

class WardListView(ListView):
    model = Ward
    context_object_name = 'wards'
    template_name = 'ward_list.html'
