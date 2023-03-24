from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20) 
    audience = models.IntegerField()
    release_date = models.DateTimeField(verbose_name='ReleaseDate')
    genre = models.CharField(max_length=30, verbose_name='Genre')
    COMEDY = '코미디'
    HORROR = '공포'
    ROMANCE = '로맨스'
    GENRE_CHOICES = [
        (COMEDY, '코미디'),
        (HORROR, '공포'),
        (ROMANCE, '로맨스'),
    ]

    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.5,
        help_text="Enter a number between 0.0 and 5.0",
    )
    
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True)



