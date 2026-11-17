from django.db import models



class Tournament (models.Model):
    T_STATUS=[
        ("Ongoing","Ongoing"),
        ("Ended","Ended")
    ]
    tournament_name=models.CharField( max_length=50)
    start_date=models.DateField(auto_now=False)
    end_date=models.DateField(auto_now=False)
    tournament_status=models.CharField(max_length=20,choices=T_STATUS)

    def __str__(self):
        return self.tournament_name


class Sport (models.Model):
    sport_name=models.CharField(max_length=20)
    tournament=models.ForeignKey( Tournament,on_delete=models.CASCADE)

    def __str__(self):
        return self.sport_name

    


class Team(models.Model):
    team_name = models.CharField(max_length=20)
    coach = models.CharField(max_length=50)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

    def total_points(self):
        return sum(result.tournament_points for result in self.result_set.all())




class Fixture (models.Model):
    team_1=models.CharField( max_length=50)
    team_2=models.CharField( max_length=50)
    fixture_date=models.DateField(auto_now=False)
    venue=models.CharField(max_length=20)
    sport=models.ForeignKey( Sport,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_1} Vs {self.team_2}"


    
class Result (models.Model):
    tournament_points=models.IntegerField()
    team=models.ForeignKey( Team,  on_delete=models.CASCADE)
    sport=models.ForeignKey( Sport,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team}-{self.tournament_points}"

    


class Stat(models.Model):
    score = models.IntegerField()
    conceded = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    fixtures = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    results = models.ForeignKey(Result, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
       
        if self.score > self.conceded:
            self.results.tournament_points = 3
        elif self.score == self.conceded:
            self.results.tournament_points = 1
        else:
            self.results.tournament_points = 0
        
        self.results.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.results}-{self.team}-{self.fixtures}"


    


 

