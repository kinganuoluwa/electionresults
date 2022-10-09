from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Agent, Result


class ResultCreateView(LoginRequiredMixin, CreateView):
    model = Result
    fields = ['apc', 'pdp', 'agent']
    template_name = 'add-results.html'
    success_url = 'results'


@login_required
def results(request):
    apc_results = Result.objects.values('apc')
    pdp_results = Result.objects.values('pdp')

    apc_final_result = 0
    for result in apc_results:
        results = result.get('apc')
        apc_final_result += results

    pdp_final_result = 0
    for result in pdp_results:
        results = result.get('pdp')
        pdp_final_result += results

    context = {
        'apc_final_result':apc_final_result,
        'pdp_final_result':pdp_final_result
    }
    return render(request, 'results.html', context)

class AgentListView(LoginRequiredMixin, ListView):
    model = Agent
    template_name = 'agents.html'
    context_object_name = 'agents'
    ordering = ['ward_number']
