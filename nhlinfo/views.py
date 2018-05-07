from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import Context, loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from nhlinfo.decorators import require_authenticated_permission
from nhlinfo.forms import ForwardForm, DefenseForm, GoalieForm
from .utils import PageLinksMixin
from .models import Conference, Division, Goalie, Team, Defense, Forward


class ConferenceList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Conference


class ConferenceDetail(View):
    def get(self, request, requested_conference_id):
        conference = get_object_or_404(
            Conference,
            conference_id=requested_conference_id
        )
        division_list = conference.divisions.all()
        return render(
            request,
            'nhlinfo/conference_detail.html',
            {'conference': conference, 'division_list': division_list}
        )


class DivisionList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Division


class DivisionDetail(View):
    def get(self, request, requested_division_id):
        division = get_object_or_404(
            Division,
            division_id=requested_division_id
        )
        team_list = division.teams.all()
        return render(
            request,
            'nhlinfo/division_detail.html',
            {'division': division, 'team_list': team_list}
        )


class TeamList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Team


class TeamDetail(View):
    def get(self, request, requested_team_id):
        team = get_object_or_404(
            Team,
            team_id=requested_team_id
        )
        goalie_list = Goalie.objects.filter(goalie_abv=team.team_abv)
        defense_list = Defense.objects.filter(defense_abv=team.team_abv)
        forward_list = Forward.objects.filter(forward_abv=team.team_abv)
        return render(
            request,
            'nhlinfo/team_detail.html',
            {'team': team, 'goalie_list': goalie_list, 'defense_list': defense_list, 'forward_list': forward_list}
        )

class ForwardList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Forward

class ForwardDetail(View):
    def get(self, request, requested_forward_id):
        forward = get_object_or_404(
            Forward,
            forward_id=requested_forward_id
        )

        team_list = Team.objects.filter(team_abv=forward.forward_abv)
        return render(
            request,
            'nhlinfo/forward_detail.html',
            {'forward': forward, 'team_list': team_list}
        )

@require_authenticated_permission(
    'nhlinfo.change_forward'
)
class ForwardUpdate(UpdateView):
    form_class=ForwardForm
    model=Forward
    template_name='nhlinfo/forward_form_update.html'


class DefenseList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Defense

class DefenseDetail(View):
    def get(self, request, requested_defense_id):
        defense = get_object_or_404(
            Defense,
            defense_id=requested_defense_id
        )

        return render(
            request,
            'nhlinfo/defense_detail.html',
            {'defense': defense}
        )


@require_authenticated_permission(
    'nhlinfo.change_defense'
)
class DefenseUpdate(UpdateView):
    form_class=DefenseForm
    model=Defense
    template_name='nhlinfo/defense_form_update.html'

class GoalieList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Goalie

class GoalieDetail(View):
    def get(self, request, requested_goalie_id):
        goalie = get_object_or_404(
            Goalie,
            goalie_id=requested_goalie_id
        )

        return render(
            request,
            'nhlinfo/goalie_detail.html',
            {'goalie': goalie}
        )

@require_authenticated_permission(
    'nhlinfo.change_goalie'
)
class GoalieUpdate(UpdateView):
    form_class=GoalieForm
    model=Goalie
    template_name='nhlinfo/goalie_form_update.html'

