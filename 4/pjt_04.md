>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 04

### 이번 pjt 를 통해 배운 내용

* django의 기초

-----

## A. base.html

- 요구사항 

- • 공통 부모 템플릿
  • 모든 템플릿 파일은 base.html을 상속받아 사용합니다.
  • 주어진 header.jpg를 화면 상단에 보여줍니다.

- 문제 접근 방법 및 코드 

- ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- ```python
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/
  ```
  
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
  
      BASE_DIR /'static',
  
  ]

```
- static 폴더 생성

- 최고 위치에 templates 폴더 생성

- templates/base.html 생성

- ```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BASE</title>
</head>
<body>
  <img src="{% static 'header.jpg' %}" alt="header">
  {% block content %}
  {% endblock content %}

</body>
</html>
```

- 어려웠던 점 

- static을 통해 사진을 불러오는 것이 익숙하지 않아서 어려웠고 setting도 쉽지 않았다

----

## B. index.html

- 요구 사항 :

- 전체 영화 목록 조회 페이지”
  • 데이터베이스에 존재하는 모든 영화의 목록을 표시합니다.
  • 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며,
  제목을 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동합니다.

- 결과 :
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-24-14-10-17-image.png)
  
  - 문제 접근 방법 및 코드 설명이 문제에서 어려웠던점
  
  - ```python
    # movies/views.py
    
    # Create your views here.
    def index(request):
        print('왜')
        movies = Movie.objects.all()
        context = {
            'movies' : movies,
        }
        return render(request, 'movies/index.html', context)
    ```

- ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>전체 영화 목록 조회 페이지</h1>
    <a href="{% url 'movies:create' %}">CREATE</a>
    <hr>
    {% for movie in movies  %}
      <a href="{% url 'movies:detail' movie.pk %}"> {{movie.title}} </a>
      <p> {{movie.score}} </p>
      <hr>
    {% endfor %}
  
  {% endblock content %}
  ```

- 내가 생각하는 이 문제의 포인트

원하는 데이터를 변수에 담아서 context에 넣어준 뒤 return에 같이 넘겨주는 것

---

## C. detail.html

- 요구사항  

- •“영화 상세 정보 페이지”
  • 특정 영화의 상세 정보를 표시합니다.
  • 해당 영화의 수정 및 삭제 버튼을 표시합니다.
  • 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.

- 접근 방법 및 코드

- ```python
  # movies/urls.py
  ```
  
  path('<int:pk>/', views.detail,name='detail'),

```
- ```python
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)
```

- ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>영화 상세 정보 페이지</h1>
    <hr>
    '''
    영화정보 
    제목
    관객수 :
    개봉일 :
    장르 :
    평점 : 
    포스터 URL :
    배우 : (대충 사진)
    줄거리 : 
    ''' 
    <div>
      <p><b> {{movie.title}} </b></p>
      <p>Audience : {{movie.audience}} </p>
      <p>Release Dates : {{movie.release_date}} </p>
      <p>Genre : {{movie.genre}} </p>
      <p>Score : {{movie.score}} </p>
      <p>Poster URL: {{movie.poster_url}} </p>
      <p>Actor: </p>
      {% if movie.actor_image %}
        <img src=" {{movie.actor_image.url}} " alt="{{movie.actor_image.url}}">
      {% endif %}
      <p> {{movie.description}} </p>
    </div>
    # 수정 및 삭제 버튼 
    # 목록으로 돌아가기 
    <div>
      <hr>
      <a href="{% url 'movies:update' movie.pk %}">UPDATE</a>
      <form action="{% url 'movies:delete' movie.pk %}" id="delete-form">
        {% csrf_token %}
        <input type="submit" value="DELETE" id="delete-btn" />
      </form><br>
      <hr>
      <a href="{% url 'movies:index' %}">BACK</a>
    </div>
  
  {% endblock content %}
  ```

- 이 문제의 포인트 
  
  `movie = Movie.objects.get(pk=pk) `를 통해 특정 pk값의 데이터만 꺼내오기

## D. create.html

- 요구사항 

- •
  “영화 생성 페이지”
  • 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
  • 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
  • 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는
  URL로 요청과 함께 전송됩니다.
  • 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크(back)를 표시합니다.
  • actor_image에 해당하는 이미지는 직접 업로드할 수 있습니다.

- 코드

- ```python
  # models/forms.py
  ```
  
  from django import forms
  from .models import Movie
  from django.forms.widgets import Select, DateInput
  
  class MovieForm(forms.ModelForm):
  
      class Meta:
          model = Movie
          fields = '__all__'
          widgets = {
              'score': forms.NumberInput(attrs={'step': 0.5}),
              'genre': Select(choices=Movie.GENRE_CHOICES),
              'release_date': DateInput(),
          }

```
- ```python
# models/models.py

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
```

- ```python
  # movies/urls.py
  ```
  
  path('create/', views.create, name = 'create'),

```
- ```python
# movies/views.py


def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        print('<<<')
        print(form)
        if form.is_valid : # 유효성 검사
            print('>>>')
            movie = form.save()
            return redirect('movies:detail', movie.pk)
        pass
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)
```

- ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>영화 생성 페이지</h1>
    <hr>
    <form action="{% url 'movies:create' %}" method = "POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{form.as_p}}
      <input type="submit" value = "Submit">
    </form>
  
  {% endblock content %}
  ```

- 이 문제의 포인트 

- model 생성 및 field 설정 및 조작 

- modelform 사용

- html에서 받은 입력값을 url로 다시 넘겨서 db에 추가하기 

## E. update.html

- 요구사항

- •
  “영화 수정 페이지”
  • 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
  • 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 합니다.
  • HTML input 요소에는 기존 데이터를 출력합니다.
  • Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정 합니다.
  • 작성한 정보는 제출(submit)시 단일 영화 데이터를 수정하는
  URL로 요청과 함께 전송됩니다.
  • 영화 상세 정보 페이지(detail.html)로 이동하는 링크(back)를 표시합니다.
  E. update.html (1/2)

- 코드

- ```python
  # models/urls.py
  path('<int:pk>/update/', views.update, name = 'update'),
  ```

- ```python
  def update(request, pk):
      movie = Movie.objects.get(pk=pk)
  
      if request.method == "POST":
          form = MovieForm(request.POST, request.FILES, instance=movie) #instance 주
          if form.is_valid() :
              form.save()
              return redirect('movies:detail', pk = movie.pk)
      else:
          form = MovieForm(instance=movie)
  
      context = {
          'form' : form,
          'movie' : movie,
      }
      return render(request, 'movies/update.html', context)
  ```

- ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>영화 수정 페이지</h1>
    <hr>
    <form action="{% url 'movies:update' movie.pk %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{form.as_p}}
      <input type="submit" value = "Submit">
    </form>
    <hr>
    <a href="{% url 'movies:detail' movie.pk %}">BACK</a>
  {% endblock content %}
  ```

- 이 문제의 포인트 

- create와의 차이점 숙지 (instance)

# 후기

* 아직 백지에서 시작하라하면 못하겠다 
* 이전에 만들어뒀던 django를 참고했고 chat GPT도 이용해서 서칭했다 
* 아무것도 안보고 할 수 있을 만큼 흐름과 사용법을 숙지해야겠다 
