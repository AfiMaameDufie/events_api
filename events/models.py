from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) 

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.category_name}'

    
EVENT_TYPES = [
    ('CF', 'Conference'),
    ('SM', 'Summit'),
    ('HK', 'Hackathon'),
    ('CJ', 'CodeJam'),
    ('EX', 'Expo'),
    ('SC', 'StartupCompetition'),
    ('DC', 'DeveloperConference'),
    ('WS', 'Workshop'),
    ('MT', 'Meetup'),
    ('UG', 'UserGroup'),
    ('OC', 'OnlineConferences'),
    ('WB', 'Webinar'),
]

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default='')
    categories = models.ManyToManyField(to=Category, blank=True, related_name='categories')
    duration = models.DateTimeField(null=True)
    country = models.CharField(max_length=40, null=True)
    location = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.event_name}, {self.event_type}, {self.country}'