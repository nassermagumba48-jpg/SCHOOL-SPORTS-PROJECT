from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from sports.forms import (
    TournamentForm, SportForm, FixtureForm,
    TeamForm, ResultForm, StatForm
)
from sports.models import (
    Tournament, Sport, Fixture, Team, Result, Stat
)



@login_required(login_url='login')
def home_view(request):
    return render(request, "home.html")


def tournament_view(request):
    return render(request, "tournament.html")


@login_required(login_url='login')
def sports_view(request):
    if request.method == "POST":
        form = SportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sport added successfully! 👍")
            return redirect("sports_page")
        else:
            messages.error(request, "Invalid data submitted!")

    else:
        form = SportForm()

    sports = Sport.objects.all()

    context = {
        "form": form,
        "sport": sports
    }
    return render(request, "sports.html", context)

@login_required(login_url='login')
def edit_sport_view(request, sport_id):
    sport = Sport.objects.get(id=sport_id)

    if request.method == "POST":
        form = SportForm(request.POST, instance=sport)
        if form.is_valid():
            form.save()
            messages.success(request, "Sport updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("sports_page")

    form = SportForm(instance=sport)

    return render(request, "edit_sport.html", {"form": form, "sport": sport})

@login_required(login_url='login')
def delete_sport_view(request, sport_id):
    Sport.objects.get(id=sport_id).delete()
    messages.success(request, "Sport deleted successfully! 🗑️")
    return redirect("sports_page")



@login_required(login_url='login')
def fixtures_view(request):
    if request.method == "POST":
        form = FixtureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fixture added successfully! 👍")
            return redirect("fixtures_page")
        else:
            messages.error(request, "Invalid data submitted!")
    else:
        form = FixtureForm()

    fixtures = Fixture.objects.all()

    return render(request, "fixtures.html", {"form": form, "fixture": fixtures})

@login_required(login_url='login')
def edit_fixture_view(request, fixture_id):
    fixture = Fixture.objects.get(id=fixture_id)

    if request.method == "POST":
        form = FixtureForm(request.POST, instance=fixture)
        if form.is_valid():
            form.save()
            messages.success(request, "Fixture updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("fixtures_page")
    else:

        form = FixtureForm(instance=fixture)
    return render(request, "edit_fixture.html", {"form": form, "fixture": fixture})

@login_required(login_url='login')
def delete_fixture_view(request, fixture_id):
    Fixture.objects.get(id=fixture_id).delete()
    messages.success(request, "Fixture deleted successfully! 🗑️")
    return redirect("fixtures_page")



@login_required(login_url='login')
def team_view(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Team added successfully! 👍")
            return redirect("team_page")
        else:
            messages.error(request, "Invalid data submitted!")
    else:
        form = TeamForm()

    teams = Team.objects.all()

    return render(request, "team.html", {"form": form, "team": teams})

@login_required(login_url='login')
def edit_team_view(request, team_id):
    team = Team.objects.get(id=team_id)

    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, "Team updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("team_page")

    form = TeamForm(instance=team)
    return render(request, "edit_team.html", {"form": form, "team": team})

@login_required(login_url='login')
def delete_team_view(request, team_id):
    Team.objects.get(id=team_id).delete()
    messages.success(request, "Team deleted successfully! 🗑️")
    return redirect("team_page")



@login_required(login_url='login')
def results_view(request):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Result added successfully! 👍")
            return redirect("results_page")
        else:
            messages.error(request, "Invalid data submitted!")
    else:
        form = ResultForm()

    results = Result.objects.all()

    return render(request, "results.html", {"form": form, "result": results})

@login_required(login_url='login')
def edit_result_view(request, result_id):
    result = Result.objects.get(id=result_id)

    if request.method == "POST":
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("results_page")

    form = ResultForm(instance=result)
    return render(request, "edit_results.html", {"form": form, "result": result})

@login_required(login_url='login')
def delete_result_view(request, result_id):
    Result.objects.get(id=result_id).delete()
    messages.success(request, "Result deleted successfully! 🗑️")
    return redirect("results_page")


@login_required(login_url='login')
def stats_view(request):
    if request.method == "POST":
        form = StatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Stat added successfully! 👍")
            return redirect("stats_page")
        else:
            messages.error(request, "Invalid data submitted!")
    else:
        form = StatForm()

    stats = Stat.objects.all()

    return render(request, "stats.html", {"form": form, "stat": stats})

@login_required(login_url='login')
def edit_stat_view(request, stat_id):
    stat = Stat.objects.get(id=stat_id)

    if request.method == "POST":
        form = StatForm(request.POST, instance=stat)
        if form.is_valid():
            form.save()
            messages.success(request, "Stat updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("stats_page")

    form = StatForm(instance=stat)
    return render(request, "edit_stat.html", {"form": form, "stat": stat})

@login_required(login_url='login')
def delete_stat_view(request, stat_id):
    Stat.objects.get(id=stat_id).delete()
    messages.success(request, "Stat deleted successfully! 🗑️")
    return redirect("stats_page")



@login_required(login_url='login')
def add_tournament_view(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tournament added successfully! 👍")
            return redirect("add_tournament_page")
        else:
            messages.error(request, "Invalid data submitted!")
    else:
        form = TournamentForm()

    tournaments = Tournament.objects.all()

    return render(request, "add_tournament_view.html", {
        "form": form,
        "tournaments": tournaments
    })

@login_required(login_url='login')
def edit_tournament_view(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)

    if request.method == "POST":
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            messages.success(request, "Tournament updated successfully! 👍")
        else:
            messages.error(request, "Invalid data submitted!")
        return redirect("add_tournament_page")
    
    else:
        form = TournamentForm(instance=tournament)
    return render(request, "edit_tournament.html", {"form": form, "tournament": tournament})

@login_required(login_url='login')
def delete_tournament_view(request, tournament_id):
    Tournament.objects.get(id=tournament_id).delete()
    messages.success(request, "Tournament deleted successfully! 🗑️")
    return redirect("add_tournament_page")
