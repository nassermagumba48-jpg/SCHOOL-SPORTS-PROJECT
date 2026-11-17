"""
URL configuration for schoolsports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from sports.views import home_view,tournament_view,sports_view,fixtures_view,team_view,results_view,stats_view,add_tournament_view ,edit_tournament_view,delete_tournament_view,edit_sport_view, delete_sport_view,edit_fixture_view,delete_fixture_view,delete_team_view,edit_team_view,edit_result_view,delete_result_view,delete_stat_view,edit_stat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('',home_view,name="home_page"),
    path('tournament/',tournament_view,name='tournament_page'),
    path('sports/',sports_view,name='sports_page'),
    path('fixtures/',fixtures_view,name='fixtures_page'),
    path('team/',team_view,name='team_page'),
    path('results/',results_view,name='results_page'),
    path('stats/',stats_view,name='stats_page'),
    path('add_tournament_view/',add_tournament_view,name='add_tournament_page'),
    path('edit_tournament/<int:tournament_id>/',edit_tournament_view,name="edit_tournament_page"),
    path('delete_tournament/<int:tournament_id>/',delete_tournament_view,name="delete_tournament_page"),
    path('edit_sport/<int:sport_id>/',edit_sport_view,name="edit_sport_page"),
    path('delete_sport/<int:sport_id>/',delete_sport_view,name="delete_sport_page"),
    path('edit_fixture/<int:fixture_id>/',edit_fixture_view,name="edit_fixture_page"),
    path('delete_fixture/<int:fixture_id>/',delete_fixture_view,name="delete_fixture_page"),
    path('delete_team/<int:team_id>/',delete_team_view,name="delete_team_page"),
    path('edit_team/<int:team_id>/',edit_team_view,name="edit_team_page"),
    path('delete_result/<int:result_id>/',delete_result_view,name="delete_result_page"),
    path('edit_result/<int:result_id>/',edit_result_view,name="edit_result_page"),
    path('delete_stat/<int:stat_id>/',delete_stat_view,name="delete_stat_page"),
    path('edit_stat/<int:stat_id>/',edit_stat_view,name="edit_stat_page")
]
