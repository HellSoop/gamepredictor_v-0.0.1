from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .models import *
from .forms import *
from . import ml_utils
from . import ml_model


class HomeView(TemplateView):
    template_name = 'gamepredictor/choose_games.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        get_games = self.request.GET.get('g') if self.request.GET.get('g') is not None else ''
        games = []
        if get_games:
            for t in set(get_games.split(',')):
                games += Games.objects.filter(name=t)
        return {'title': 'Главная страница', 'get_g': get_games, 'games': games}


def get_user_interests(games_titles):
    '''Не является представлением. Инкапсулирует выбор игр из базы по интересам пользователя.'''
    games = [ml_utils.get_characteristics(Games.objects.get(name=g)) for g in games_titles]
    users_interests = []  # предыдущая строка создаёт спискок со списками с характеристиками каждой игры в запросе
    for i in range(len(games[0])):
        users_interests.append(sum([g[i] for g in games]) / len(games))
    res_games = [Games.objects.get(name=g) for g in ml_utils.get_closest(users_interests, 4) if not g in games_titles]
    # в предыдущей строке по названиям игр ищутся их объекты в базе данных
    return res_games


class ResultView(TemplateView):
    template_name = 'gamepredictor/result_games.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.GET.get('g') == '':
            return Http404
        games_titles = set(self.request.GET.get('g').split(','))
        return {'title': 'Результаты', 'games': get_user_interests(games_titles)}


def search_view(request):
    '''Представление. Используется для реализации живого поиска.'''
    q = request.GET.get('q')
    if not q:
        raise Http404
    games = request.GET.get('g')
    titles = Games.objects.filter(name__iregex=q)[:4]
    return render(request, 'gamepredictor/search-help.html', context={'titles': titles, 'games': games})


class ReportView(FormView):
    form_class = ReportForm
    template_name = 'gamepredictor/report.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Не понравилась игра'}

    def get_context_data(self, **kwargs):
        raise Http404

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
