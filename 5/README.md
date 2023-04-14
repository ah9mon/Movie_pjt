
# PJT 05

## Apps

> 생성한 앱 목록

- movies

- accounts
1. `python manage.py startapp` 으로 app생성

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-16-20-27-image.png)

2. `settings.py` 의 `INSTALLED_APPS` 에 추가한 앱 작성
   
   ```python
   INSTALLED_APPS = [
       'movies', # movies app 추가
       'accounts', # 추
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

## Model

> 생성한 모델 

- Movie -> movies(app)/ models.py 에 생성
  
  ```python
  from django.db import models
  
  # Create your models here.
  class Movie(models.Model):
      title = models.CharField(max_length=20)
      description = models.TextField()
  ```

- User -> accounts(app)/models.py 에 생성
  
  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser # AbstractUser 불러오기 
  
  # Create your models here.
  class User(AbstractUser):
      pass
  ```
  
  - 주의할점 
  - `AUTH_USER_MODEL = 'accounts.User'`을 settings.py에 작성해줘야함 
  - 기본적으로 django에서 제공하는 User 모델이 아닌 
  - 내가 app내에 생성한 모델을 사용할 것이기 때문  

## URL

> url 작성

1. 각각의 앱에 urls.py 를 만들어 각자의 url 관리하게 함 

2. mypjt/urls.py 에서  include를 사용해서 각자 관리하는 urls.py 로 이동하도록 함 
   
   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('movies/', include('movies.urls')),
       path('accounts/', include('accounts.urls')),
   ]
   ```

3. movies/urls.py
   
   ```python
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       path('', views.index, name='index'),
       path('create/', views.create, name = 'create'),
       path('<int:pk>/', views.detail, name = 'detail'),
       path('<int:pk>/update/', views.update, name = 'update'),
       path('<int:pk>/delete/', views.delete, name = 'delete'),
   ]
   ```

4. accounts/urls.py
   
   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   urlpatterns = [
       path('login/', views.user_login, name='login'),
       path('logout/', views.user_logout, name = 'logout'),
       path('signup/', views.signup, name = 'signup'),
       path('delete/', views.delete, name = 'delete'),
       path('update/', views.update, name = 'update'),
       path('password/', views.password, name = 'password'),
   ]
   ```

## views

1. movies/views.py

```python
# Create your views here.
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe # 추가 기능을 위한 데코레이터 
from django.contrib.auth.decorators import login_required # 로그인 상태에서만 가능한 view들 제한하기 위한 데코레이터 



@require_safe # get 허용 
def index(request): 
    '''
    index.html에서 등록된 영화들을 나열해서 보여줘야함 
    따라서 모델 Movies의 모든 데이터를 movies에 할당하고 
    context에 넣어서 render를 통해 index.html에 보내줌 
    '''
    print('>>>')
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context) 

@login_required
@require_http_methods(['GET','POST']) # get, post 둘다 허용 
def create(request):
    '''
    생성하는 기능을 위한 view
    '''
    if request.method == "POST": # post 로 왓으면 
        form = MovieForm(request.POST) # 담아서 
        if form.is_valid(): # 유효성 체크하고 
            movie = form.save() # 저장한다음 
            return redirect('movies:detail', movie.pk) # detail 페이지로 가려면 pk가 필요하니까 담아서 같이 주기
    else: # get으로 왓으면 
        form = MovieForm()  # 영화 등록 form을 form에 담고 
    context = {
        "form" : form,
    } # context에 넣고 
    return render(request, 'movies/create.html', context) # create.html로 같이 보냄 

@require_safe # get 허용
def detail(request, pk): # detail page는 특정 데이터를 꺼내 봐야 하기 때문에 pk 같이 받음 
    movie = Movie.objects.get(pk = pk) # 특정 pk의 데이터 따로 꺼내서 movie에 할당 
    context = { 
        'movie' : movie,
    } # context에 담음 
    return render(request, 'movies/detail.html', context) # detail page에 movie의 데이터를 쓸거기 때문에 같이 보냄 

@login_required
@require_http_methods(['GET','POST']) # get post 둘다 허용  
def update(request, pk): # 특정 데이터를 수정하는 거기 때문에 데이터를 특정할 pk 같이 받음 
    movie = Movie.objects.get(pk = pk) # 특정 pk의 데이터 할당 

    if request.method == "POST": # post로 오면 (수정되면)
        form = MovieForm(request.POST, instance=movie) #
        if form.is_valid(): # 유효성 검사 하고 
            form.save() # 저장 
            return redirect('movies:detail', movie.pk) # 다시 detail로 가려면 pk필요하니까 같이 보냄 
    else: # get으로 오면 (수정한게 아니고 수정 페이지 요청한거 )

        form = MovieForm(instance = movie)

    context = {
        'form' : form,
        'movie' : movie,
    }

    return render(request, 'movies/update.html', context)

@login_required
@require_POST # POST만 허용 
def delete(request, pk): 
    movie = Movie.objects.get(pk = pk)
    movie.delete() # 삭제 
    return redirect('movies:index')
```

2. accounts/views.py

```python
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash # django에는 로그인 , 로그아웃 편하개 구현할 수 있슴 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required # 로그인 상태에서만 가능한 view들 제한하기 위한 데코레이터 
from django.views.decorators.http import require_http_methods, require_POST, require_safe 


@require_http_methods(['GET','POST'])
def user_login(request):
    if request.method == 'POST': # 로그인 요청 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 유효성 검사 
            login(request, form.get_user()) # 로그인 -> 유저 정보 담아서 줘야함 
            return redirect('movies:index')

    else: # 로그인 페이지 요청 
        form = AuthenticationForm()

    context = {
        "form" : form
    }

    return render(request, 'accounts/login.html', context)

@login_required # 로그인 상태가 요구되는 view -> 로그인 안하면 안됨 
@require_POST
def user_logout(request):
    logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST': # 회원가입 요청 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효성 검사 
            user = form.save()
            login(request, user) 
            return redirect('movies:index')

    else: # 회원가입 페이지 요청 
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)

@login_required # 로그인 필요함 
@require_http_methods(['GET','POST'])
def update(request):
    print('>>>update')
    if request.method == 'POST': # 수정 요청 
        form = CustomUserChangeForm(request.POST, instance = request.user) # 기존에 있던 정보 넣어주려면 instance 사용해야함 안그럼 새로 만듬 
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    else: # 수정 페이지 요청 
        form = CustomUserChangeForm(instance = request.user) # 기존 정보 instance로 담아서 form 데이터 할당 

    context = {
        'form' : form,
    }

    return render(request, 'accounts/update.html', context)

@login_required # 로그인 필요한 기능 
@require_POST
def delete(request):
    request.user.delete() # 먼저 데이터 삭제 후 
    logout(request)  # 쿠키 삭제
    '''
    먼저 로그아웃하면 인증상태 풀려서 뭘 삭제해야할지 모름 
    '''
    return redirect('movies:index')

@login_required # 로그인 필요한 기능 
@require_http_methods(['GET','POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # 비밀번호 바꾸면 데이터가 바뀌는거라 같은 사람이라고 인식못하고 로그인 풀림 / 이거 이용해서 즉시 데이터 업데이트 해주자  
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form ,
    }

    return render(request, 'accounts/change_password.html', context)
```

### 어려웠던 점

- pk가 필요한 view들이 어려웟음 
- 그리고 구현 방법이 너무 많아서 어떤 것을 사용해서 구현해야하는지 헷갈리고 고민됐음 
- Html에서 form을 통해 pk 넘겨 받고 다시 view에서 사용하고 다시 html에 보내주는 흐름이 복잡했다 

## Admin

> 모델 Movie, User 등록하기 

### Movies/admin.py

```python
from django.contrib import admin
from .models import Movie
# Register your models here.
admin.site.register(Movie)
```

### Accounts/admin.py

```python
from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
```

### 결과

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-12-27-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-13-06-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-13-23-image.png)

- 생성, 조회, 수정, 삭제 다됨 

## Form

### 요구사항

A.
Movie
모델의 데이터 검증 , 저장 , 에러메시지 , HTML 을
모두 관리하기 위해 적절한 ModelForm 을 사용합니다
B.
User
모델의 데이터 검증 , 저장 , 에러메시지 , HTML 을 모두 관리하기 위해
적절한 Form 과 ModelForm 그리고 커스텀 ModelForm 을 사용합니다

### Movies/forms.py

```python
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__' # 모델 Movie의 모든 필드를 사용 
```

### Accounts/forms.py

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model 

'''
UserCreationForm 을 그대로 사용하더라도
CustomUserCreationForm의 형태로 작성하도록 장고가 추천함
'''
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'password']
```

## Template

1. base.html 생성 
   
   ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-30-40-image.png)

2. settings.py에 base.html 경로 추가 
   
   ```python
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # -> BASE_DIR의 templates도 열어볼 수 있게 경로 작성한거임 
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

3. movies/templates/movies
   
   ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-29-35-image.png)

4. accounts/templates/accounts
   
   ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-07-17-30-05-image.png)

### base.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        {% if user.is_authenticated %} # 로그인 상태면 
        <h1>Hi {{user}}, this is BASE.html</h1>
        <ul>
            <a href="{% url 'accounts:update' %} " >회원정보수정</a>
            <form action="{% url 'accounts:logout' %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="Logout">
            </form>
            <form action="{% url 'accounts:delete'  %} " method="POST">
                {% csrf_token %}
                <input type="submit" value="회원탈퇴">
            </form>
        </ul>
        {% else %} # 로그아웃 상태면 
        <ul>
            <a href="{% url 'accounts:login'%}">Login</a>
            <a href="{% url 'accounts:signup'%}">Signup</a>
        </ul>

        {% endif %}
    </nav>
    <hr>
    {% block content %}


    {% endblock content %}
</body>
</html>
```

- `{% if user.is_authenticated %}` 로 로그인 상태인지 확인하는게 중요 포인트 

### Movies

#### index.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'movies:create' %}">CREATE</a>
  <hr>
  {% for movie in movies  %}
    <a href="{% url 'movies:detail' pk=movie.pk %}"> {{movie.title}} </a>
    <hr>
  {% endfor %}

{% endblock content %}
```

#### detail.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <hr>
  <h2> {{movie.title}} </h2>
  <p> {{movie.description}} </p>
  <a href="{% url 'movies:update' pk=movie.pk %}">UPDATE</a>
  <form action="{% url 'movies:delete' pk=movie.pk %}" method = 'POST'>
      {% csrf_token %}
      <input type="submit" value = "DELETE">
  </form>  
  <a href="{% url 'movies:index'%}">BACK</a>
{% endblock content %}
```

#### create.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method = "POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value = "Submit">
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```

#### update.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method = "POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="reset" value = "Reset">
    <input type="submit" value = "Submit">
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>

{% endblock content %}
```

### accounts

#### login.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="{% url 'accounts:login' %}" method = "POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value = "Submit">
  </form>
{% endblock content %}
```

#### signup.html

```python
{% extends 'base.html' %}

{% block content %}
  <h1>Signup</h1>
  <form action="{% url 'accounts:signup' %}" method = 'POST'>

    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value = 'Submit'>
  </form>
{% endblock content %}
```

#### update.html

```python
{% extends 'base.html' %}


{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %} user.pk">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value='submit'>
  </form>

{% endblock content %}
```

#### password.html

```python
{% extends 'base.html' %}


{% block content %}
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:password' %} " method = "POST">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" value = "Submit">
  </form>

{% endblock content %}
```

## 추가 요구사항

- 로그인한 회원만 영화 정보를 생성, 수정, 삭제할 수 있습니다
  -> movies/views.py 에서 create, update, delete 함수에 @login_required 데코레이터 붙여서 해결완료

- 비밀번호 변경 직후 로그인 상태를 유지해야 합니다.

- -> 
  
  ```python
            update_session_auth_hash(request, form.user) # 비밀번호 바꾸면 데이터가 바뀌는거라 같은 사람이라고 인식못하고 로그인 풀림 / 이거 이용해서 즉시 데이터 업데이트 해주자  
  ```

# 후기

복습이 시급하다
