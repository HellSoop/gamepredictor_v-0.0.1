from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class ReportForm(forms.Form):
    shooter = forms.ChoiceField(label='Понравилась ли вам шутер составляющая игры?',
                                choices=((0, 'Да'), (-1, 'Нет, мне было слишком просто'),
                                (1, 'Нет, мне было слишком сложно')), widget=forms.RadioSelect, initial=0)
    rpg = forms.ChoiceField(label='Понравилась ли вам РПГ составляющая игры?',
                            choices=((0, 'Да'), (-1, 'Нет, система слишком простая'),
                            (1, 'Нет, система слишком сложная')), widget=forms.RadioSelect, initial=0)
    story = forms.ChoiceField(label='Понравился ли вам сюжет игры?',
                              choices=((0, 'Да'), (-1, 'Нет, она слишком простая'),
                                (1, 'Нет, она слишком запутанная')), widget=forms.RadioSelect, initial=0)
    gloominess = forms.ChoiceField(label='Достаточно ли игра мрачная?',
                                   choices=((0, 'Да'), (-1, 'Нет, она слишком светлая'),
                                    (1, 'Нет, она слишком мрачная')), widget=forms.RadioSelect, initial=0)
    aesthetics = forms.ChoiceField(label='Понравилась ли вам эстетика игры?',
                                   choices=((0, 'Да'), (-1, 'Нет, она некрасивая'),
                                    (1, 'Нет, она слишком много внимания уделяет внешнему виду')), widget=forms.RadioSelect, initial=0)
    survival = forms.ChoiceField(label='Понравилась ли вам составляющая выживания в игре?',
                                 choices=((0, 'Да'), (-1, 'Нет, она недостаточно проработанная'),
                                    (1, 'Нет, система слишком сложная')), widget=forms.RadioSelect, initial=0)
    fullness_of_world = forms.ChoiceField(label='Достаточно ли мир наполненный?',
                                          choices=((0, 'Да'), (-1, 'Нет, он слишком пустой'),
                                            (1, 'Нет, он переполненный')), widget=forms.RadioSelect, initial=0)
    creative_potential = forms.ChoiceField(label='Достаточно ли игра позволила раскрыть ваш творческий потенциал?',
                                           choices=((0, 'Да'), (-1, 'Нет, мне не хватило творчества в игре'),
                                            (1, 'Нет, игра требует слишком много творчества')), widget=forms.RadioSelect, initial=0)
    fighting_system = forms.ChoiceField(label='Понравилась ли вам боевая система игры?',
                                        choices=((0, 'Да'), (-1, 'Нет, она не достаточно проработанная'),
                                            (1, 'Нет, она слишком сложная')), widget=forms.RadioSelect, initial=0)
    puzzles = forms.ChoiceField(label='Понравились ли вам головоломки в игре?',
                                choices=((0, 'Да'), (-1, 'Нет, они слишком простые'),
                                (1, 'Нет, они сишком сложные')), widget=forms.RadioSelect, initial=0)
    quests = forms.ChoiceField(label='Понравились ли вам квесты в игре?',
                               choices=((0, 'Да'), (-1, 'Нет, они слишком простые, короткие и скучные'),
                                (1, 'Нет, они слишком сложные и затянутые')), widget=forms.RadioSelect, initial=0)
    moral = forms.ChoiceField(label='Понравился ли вам посыл игры?',
                              choices=((0, 'Да'), (-1, 'Нет, он слишком прост и примитивен'),
                                (1, 'Нет, он слишком сложный и непонятный')), widget=forms.RadioSelect, initial=0)
    horror = forms.ChoiceField(label='Понравилась ли вам хоррор составляющая игры?',
                               choices=((0, 'Да'), (-1, 'Нет, игра нелостаточно страшная'),
                                (1, 'Нет, игра слишком страшная')), widget=forms.RadioSelect, initial=0)
    action = forms.ChoiceField(label='Понравился ли вам динамика игры?',
                               choices=((0, 'Да'), (-1, 'Нет, игра слишком затянутая'),
                                (1, 'Нет, игра слишком динамичная')), widget=forms.RadioSelect, initial=0)
    emotionality = forms.ChoiceField(label='Понравилась ли вам эмоциональность игры?',
                                     choices=((0, 'Да'), (-1, 'Нет, в игре недостаточно эмоциональности'),
                                        (1, 'Нет, в игра слишком драматичная')), widget=forms.RadioSelect, initial=0)
    reality = forms.ChoiceField(label='Достаточно ли игра реальная?',
                                choices=((0, 'Да'), (-1, 'Нет, игра не достаточно реальная'),
                                    (1, 'Нет, игра слишком реалистична')), widget=forms.RadioSelect, initial=0)
    atmosphere = forms.ChoiceField(label='Понравилась ли вам атмосфера игры?',
                                   choices=((0, 'Да'), (-1, 'Нет, игра недостаточно атмосферная'),
                                    (1, 'Нет, игра слишком атмосферная')), widget=forms.RadioSelect, initial=0)
    difficulty = forms.ChoiceField(label='Достаточно ли игра сложная?',
                                   choices=((0, 'Да'), (-1, 'Нет, она слишком простая'),
                                    (1, 'Нет, она слишком сложная')), widget=forms.RadioSelect, initial=0)

    def __init__(self, *args, **kwargs): # Всё это нужно, чтобы везде изначально было выбрано 'да'
        super().__init__(*args, **kwargs)
    #
    # class Meta:
    #     model = Games
    #     fields = ['shooter', 'rpg', 'story', 'gloominess', 'aesthetics', 'survival', 'fullness_of_world',
    #               'creative_potential', 'fighting_system', 'puzzles', 'quests', 'moral', 'horror', 'action',
    #               'emotionality', 'reality', 'atmosphere', 'difficulty']
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-input'}),
    #         'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
    #     }
