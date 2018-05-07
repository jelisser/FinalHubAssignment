"""ez_university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from nhlinfo.views import ConferenceList, ConferenceDetail, DivisionDetail, DivisionList, TeamList, TeamDetail, \
    ForwardList, ForwardDetail, DefenseList, DefenseDetail, GoalieList, GoalieDetail, ForwardUpdate, DefenseUpdate, \
    GoalieUpdate

urlpatterns = [
    url(r'^conference/$',
        ConferenceList.as_view(),
        name='nhlinfo_conference_list_urlpattern'
        ),
    url(r'conference/(?P<requested_conference_id>[\d]+)/$',
        ConferenceDetail.as_view(),
        name='nhlinfo_conference_detail_urlpattern'),
    url(r'^division/$',
        DivisionList.as_view(),
        name='nhlinfo_division_list_urlpattern'
        ),
    url(r'division/(?P<requested_division_id>[\d]+)/$',
        DivisionDetail.as_view(),
        name='nhlinfo_division_detail_urlpattern'),
    url(r'^team/$',
        TeamList.as_view(),
        name='nhlinfo_team_list_urlpattern'
        ),
    url(r'team/(?P<requested_team_id>[\d]+)/$',
        TeamDetail.as_view(),
        name='nhlinfo_team_detail_urlpattern'),
    url(r'^forward/$',
        ForwardList.as_view(),
        name='nhlinfo_forward_list_urlpattern'
        ),
    url(r'forward/(?P<requested_forward_id>[\d]+)/$',
        ForwardDetail.as_view(),
        name='nhlinfo_forward_detail_urlpattern'),
    url(r'forward/(?P<pk>[\d]+)/update/$',
        ForwardUpdate.as_view(),
        name='nhlinfo_forward_update_urlpattern'),
    url(r'^defense/$',
        DefenseList.as_view(),
        name='nhlinfo_defense_list_urlpattern'
        ),
    url(r'defense/(?P<requested_defense_id>[\d]+)/$',
        DefenseDetail.as_view(),
        name='nhlinfo_defense_detail_urlpattern'),
    url(r'defense/(?P<pk>[\d]+)/update/$',
        DefenseUpdate.as_view(),
        name='nhlinfo_defense_update_urlpattern'),
    url(r'^goalie/$',
        GoalieList.as_view(),
        name='nhlinfo_goalie_list_urlpattern'
        ),
    url(r'goalie/(?P<requested_goalie_id>[\d]+)/$',
        GoalieDetail.as_view(),
        name='nhlinfo_goalie_detail_urlpattern'),
    url(r'goalie/(?P<pk>[\d]+)/update/$',
        GoalieUpdate.as_view(),
        name='nhlinfo_goalie_update_urlpattern'),
]
