from django.urls import path

from . import views

urlpatterns = [
    path('groups/', views.index, name='all-groups'),  # our-domain.com/groups
    path('groups/<slug:group_slug>', views.group_details, name='group-details'),  # our-domain.com/groups/dinamico
    path('lp/', views.landing_page, name='landing-page'),
    path('questionario/', views.questionario, name='questionario'),
    path('error/', views.csrf_failure, name='error'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
]