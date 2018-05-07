from django import forms

from nhlinfo.models import Forward, Defense, Goalie


class ForwardForm(forms.ModelForm):
    class Meta:
        model = Forward
        fields = ('forward_com',
                  )

    def clean_comment(self):
        return self.cleaned_data['forward_com'].strip()

class DefenseForm(forms.ModelForm):
    class Meta:
        model = Defense
        fields = ('defense_com',
                  )

    def clean_comment(self):
        return self.cleaned_data['defense_com'].strip()

class GoalieForm(forms.ModelForm):
    class Meta:
        model = Goalie
        fields = ('goalie_com',
                  )

    def clean_comment(self):
        return self.cleaned_data['goalie_com'].strip()


