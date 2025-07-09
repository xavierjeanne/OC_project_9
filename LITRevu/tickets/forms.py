from django import forms
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 0,
                'max': 5,
                'type': 'number'
            }),
            'headline': forms.TextInput(attrs={
                'placeholder': 'Titre de votre critique'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Votre critique ici…',
                'rows': 5
            })
        }
        labels = {
            'rating': 'Note (0 à 5)',
            'headline': 'Titre',
            'body': 'Commentaire'
        }


class UserFollowsForm(forms.ModelForm):

    followed_username = forms.CharField(
        label='Utilisateur à suivre',
        help_text='Commencez à taper un nom d\'utilisateur.',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = UserFollows
        fields = ['followed_username']
