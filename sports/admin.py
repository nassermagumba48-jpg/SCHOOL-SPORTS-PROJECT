from django.contrib import admin


from .models import Tournament,Sport,Team,Fixture,Result,Stat


class TournamentAdmin(admin.ModelAdmin):
    list_display=("tournament_name","start_date","end_date","tournament_status")

admin.site.register(Tournament,TournamentAdmin)


class SportAdmin(admin.ModelAdmin):
    list_display=("sport_name","tournament")

admin.site.register(Sport,SportAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display=("team_name","coach","tournament")

admin.site.register(Team,TeamAdmin)


class FixtureAdmin(admin.ModelAdmin):
    list_display=("team_1","team_2","fixture_date","venue","sport")

admin.site.register(Fixture,FixtureAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display=("tournament_points","team","sport")

admin.site.register(Result,ResultAdmin)


class StatAdmin(admin.ModelAdmin):
    list_display=("score","conceded","team","fixtures","results")

admin.site.register(Stat,StatAdmin)


