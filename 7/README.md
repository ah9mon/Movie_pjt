# 07_pjt
## Installation 
```
pip install djangorestframework
django-admin startproject mypjt
python manage.py startapp movies
```

`settings.py`

```python
INSTALLED_APPS = [
    # Local apps
    'movies',

    # 3rd party
    'rest_framework',

    # native
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Model
> 구성할 모델 <br> 
A. Actor <br>
B. Movie <br>
C. Review

### A. Actor
|필드명|데이터 유형|역할|
|------|---|---|
|name|varchar(100)|배우 이름|

### B. Movie
|필드명|데이터 유형|역할|
|------|---|---|
|title|varchar(100)|영화 제목|
|overview|text|줄거리|
|release_date|datetime|개봉일|
|poster_path|text|포스터 주소|

### C. Review
|필드명|데이터 유형|역할|
|------|---|---|
|title|varchar(100)|리뷰 제목|
|content|text|리뷰 내용|
|movie_id|integer|외래 키(Movie 클래스 참조)|

### ERD (Entity-Relationship Diagram)
[ERD](ERD.png "ERD")

### movies/models.py
```python
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor)

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="reviews")
```

## URLs
`mypjt/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls'))
]
```

`movies/urls.py`
```python
from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('actor_list/', views.actor_list, name="actor_list"),
    path('actor_list/<int:actor_pk>/', views.actor_detail, name="actor_detail"),
    path('movie_list/', views.movie_list, name="movie_list"),
    path('movie_list/<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('review_list/', views.review_list, name="review_list" ),
    path('review_list/<int:review_pk>/', views.review_detail, name="review_detail"),
    path('movie_list/<int:movie_pk>/create_review/', views.create_review, name="create_review"),
]
```
- review는 외래 키 movie로 Movie class를 참조하기 때문에 movie의 pk가 필요하다
따라서, url 경로를 `'movie_list/<int:movie_pk>/create_review/'`와 같이해서 movie_pk를 받을 수 있도록 설정했다.

## Serializer

- 모든 필드를 (`fields = '__all__'`) JSON의 속성으로 만들어도 되지만 
사용하지 않을 데이터까지 모두 보내는 것은 `큰 데이터 용량` -> `다운로드 속도 저하` -> `UX 하락`으로 이어지기 때문에 필요한 정보만으로 목록을 구성한다.

```python
from rest_framework import serializers
from .models import Actor, Movie, Review

################################################
#################### review #####################
################################################

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

        read_only_fields = ('movie',)

class ReviewlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

class ReviewdetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_movie(self, review):

        movie = review.movie

        return [{"title" : movie.title}]
```
- 첫번째 serializer는 리뷰의 PUT, POST를 위한 것이다.
수정 및 생성을 할때 어떤 movie를 리뷰할지는 사용자가 직접 입력하여 정하는 것이 아니고 해당 movie 게시글 페이지에서 입력하는 것이기 때문에 movie column은 수정 및 입력하지 않고 자동으로 넘겨주도록 할 것이다.
따라서, `read_only_fields = ('movie',)`를 작성해줬다.

- 세번째 serializer는 리뷰 상세보기 페이지를 위한 것이다.
해당 페이지는 어떤 영화의 리뷰인지 보여주기 위해
JSON의 속성에 movie 인스턴스의 모든 필드가 아닌
'title'만을 넘겨줄 것이기 때문에 
`movie = serializers.SerializerMethodField()` 를 통해 빈 속성을 만들어주고 
```python
def get_movie(self, review)
    movie = review.movie
    return [{"title" : movie.title}]
```
를 통해 'title'만을 지정해주어 해당 속성의 value로 넣어줫다. 


```python
################################################
#################### movie #####################
################################################

class MovieslistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'overview')

class MoviesdetailSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_actors(self, movie):
        actors = movie.actors.all() # 정참조
        return [{"name" : actor.name} for actor in actors]
    
    def get_reviews(self, movie):
        reviews = movie.reviews.all() # 역참조
        return [{"title" : review.title, "content" : review.content} for review in reviews]
```
- 세번쨰 serializer는 영화 상세 보기 페이지를 위한 것이다.
해당 detail 페이지에는 해당 영화의 배우들 이름과 리뷰 목록을 담아서 줄 것이기 떄문에 이것도 `serializers.SerializerMethodField()` 를 이용해 빈 속성을 만들어 거기에 원하는 데이터를 담아주었다.

```python
################################################
#################### actor #####################
################################################

class ActorMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)



class ActorslistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class ActorsdetailSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    
    class Meta:
        model = Actor
        fields = '__all__'

    def get_movies(self, actor):
        movies = actor.movie_set.all() # 역참조 
        return [{"title" : movie.title} for movie in movies]
```
- 세번쨰 serializer는 영화 배우 상세 정보 페이지를 위한 것이다.
영화 배우 정보 페이지에서 해당 배우가 출연한 영화들의 제목 데이터를 추가적으로 보내줘야했다. 하지만 출연한 영화가 여러 개인 경우가 있었다.
이를 위해, `serializers.SerializerMethodField()`를 사용해서 빈 속성을 만들고
반복문을 이용해 영화의 제목들을 담았다.

### Serailizer 리뷰 
- 각 모델의 views를 위해 8개의 serializer가 필요했다.
하지만, 한 파일(`movies/serializer.py`)에 모든 serializer 클래스를 모아두어
단일 파일에 너무 많은 코드가 들어감으로써 가독성을 떨어뜨리게 되는 것을 간과했다. 
다음부턴 모델별 필요한 serializer를 분리 해야겠다.

- 외래키를 통해서 review에서 Movie 클래스를 참조하게 되는데 
sqlite3를 열어봤을 때 테이블에 movie 행에 movie의 FK(PK)가 담겨있는 것을 보고 `review.movie`는 해당 movie의 key만 가져오는 것인줄 알았다
하지만 직접 구현해보며 인스턴스를 통채로 참조해주는 것임을 확실히 알게됐다.


