from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.db.models import PROTECT


class Conference(models.Model):
    conference_id = models.AutoField(primary_key=True)
    conference_name = models.CharField(max_length=10)

    def __str__(self):
        return self.conference_name

    def get_absolute_url(self):
        return reverse('nhlinfo_conference_detail_urlpattern',
                       kwargs={'requested_conference_id': self.conference_id})

    class Meta:
        ordering = ['conference_name']


class Division (models.Model):
    division_id = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=20)
    conference = models.ForeignKey(Conference, related_name='divisions',on_delete=PROTECT)

    def __str__(self):
        return self.division_name

    def get_absolute_url(self):
        return reverse('nhlinfo_division_detail_urlpattern',
                       kwargs={'requested_division_id' : self.division_id})

    class Meta:
        ordering = ['division_name']


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=25)
    team_abv = models.CharField(max_length=3)
    division = models.ForeignKey(Division, related_name='teams', on_delete=PROTECT)


    def __str__(self):
        return '%s - (%s)' % (self.team_name, self.team_abv)

    def get_absolute_url(self):
        return reverse ('nhlinfo_team_detail_urlpattern',
                        kwargs={'requested_team_id':self.team_id})

    class Meta:
        ordering = ['team_name','team_abv']


class Forward(models.Model):
    forward_id = models.AutoField(primary_key=True)
    forward_abv = models.CharField(max_length=3)
    forward_fname = models.CharField(max_length=25)
    forward_lname = models.CharField(max_length=25)
    forward_wt = models.CharField(max_length=25, default=None)
    forward_ht = models.CharField(max_length=25, default=None)
    forward_pts = models.CharField(max_length=25, default=None)
    forward_toi = models.CharField(max_length=25, default=None)
    forward_nat = models.CharField(max_length=25, default=None)
    forward_com = models.TextField(default=None, null=True)

    def __str__(self):
        return '%s, %s - (%s)' % (self.forward_lname, self.forward_fname,self.forward_abv)

    def get_absolute_url(self):
        return reverse('nhlinfo_forward_detail_urlpattern',
                       kwargs={'requested_forward_id':self.forward_id})

    def get_update_url(self):
        return reverse('nhlinfo_forward_update_urlpattern',
                       kwargs={'pk':self.forward_id})

    class Meta:
        ordering = ['forward_lname','forward_fname','forward_abv']


class Defense(models.Model):
    defense_id = models.AutoField(primary_key=True)
    defense_abv = models.CharField(max_length=3)
    defense_fname = models.CharField(max_length=25)
    defense_lname = models.CharField(max_length=25)
    defense_wt =models.CharField(max_length=25, default=None)
    defense_ht = models.CharField(max_length=25, default=None)
    defense_ga = models.CharField(max_length=25, default=None)
    defense_toi = models.CharField(max_length=25, default=None)
    defense_nat = models.CharField(max_length=3)
    defense_com = models.TextField(default=None, null=True)


    def __str__(self):
        return '%s, %s - (%s)' %(self.defense_lname, self.defense_fname, self.defense_abv)

    def get_absolute_url(self):
        return reverse('nhlinfo_defense_detail_urlpattern',
                       kwargs={'requested_defense_id':self.defense_id})

    def get_update_url(self):
        return reverse('nhlinfo_defense_update_urlpattern',
                       kwargs={'pk':self.defense_id})

    class Meta:
        ordering = ['defense_lname','defense_fname','defense_abv']


class Goalie(models.Model):
    goalie_id = models.AutoField(primary_key=True)
    goalie_abv = models.CharField(max_length=3, default=None)
    goalie_fname = models.CharField(max_length=25, default=None)
    goalie_lname = models.CharField(max_length=25, default=None)
    goalie_wt = models.CharField(max_length=25, default=None)
    goalie_ht = models.CharField(max_length=25, default=None)
    goalie_ga = models.CharField(max_length=25, default=None)
    goalie_sp = models.CharField(max_length=25, default=None)
    goalie_nat = models.CharField(max_length=3, default=None)
    goalie_com = models.TextField(default=None, null=True)

    def __str__(self):
        return '%s, %s - (%s)' %(self.goalie_lname, self.goalie_fname, self.goalie_abv)

    def get_absolute_url(self):
        return reverse('nhlinfo_goalie_detail_urlpattern',
                       kwargs={'requested_goalie_id': self.goalie_id })

    def get_update_url(self):
        return reverse('nhlinfo_goalie_update_urlpattern',
                       kwargs={'pk':self.goalie_id})

    class Meta:
        ordering = ['goalie_lname', 'goalie_fname', 'goalie_abv']