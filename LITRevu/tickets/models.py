from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from authentication.models import User


class Ticket(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to='ticket_images/',
        null=True,
        blank=True
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket,
                               on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    follower = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='following')
    followed = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='followers')
    blocked = models.BooleanField(default=False)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('follower', 'followed', )
