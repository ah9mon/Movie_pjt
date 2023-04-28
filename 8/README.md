pjt08

# A. 유저 팔로우 기능 
```html
<!--accounts/profile.html-->
 <div>

          <form id="follow-form" data-user-id="{{person.pk}}">

            {% csrf_token %}

            {% if user in followers %}

              <button id="followBtn">언팔로우</button>

            {% else %}

              <button id="followBtn">팔로우</button>

            {% endif %}

          </form>

        </div>
```
```js
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

<script>

  const form = document.querySelector('#follow-form')

  form.addEventListener('submit', function(event){

    event.preventDefault()

  

    //csrftoken 가져오기

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log(event)

    const userId = event.target.dataset.userId

    console.log(userId)

    axios({

      method: 'post',

      url: `/accounts/${userId}/follow/`,

      headers: {'X-CSRFToken': csrftoken},

    })

    .then((response) => {

      console.log(response)

      const isFollowed = response.data.is_followed

      const followBtn = document.querySelector('#follow-form > button')

      console.log(followBtn)

      if (isFollowed==true) {

        followBtn.innerText = '언팔로우'

  

      } else {

        followBtn.innerText = '팔로우'

      }

      const followersCountTag = document.querySelector('#followers-count')

      const followingsCountTag = document.querySelector('#followings-count')

      const followersCount = response.data.followers_count

      const followingsCount = response.data.followings_count

      followersCountTag.innerText = followersCount

      followingsCountTag.innerText = followingsCount

  

    })

  })

  

</script>
```
- js를 통해 팔로우 수/ 팔로잉 수/팔로우 버튼/ 을 비동기화로 구현했다 
- `event.preventDefault()` 를 통해 버튼을 클릭하면 form이 제출되어 새로고침 되는 현상을 막았다 
```python
# accounts/views.py
@require_POST

def follow(request, user_pk):

    if request.user.is_authenticated:

        person = get_object_or_404(get_user_model(), pk=user_pk)

        user = request.user

        if person != user:

            if person.followers.filter(pk=user.pk).exists():

                person.followers.remove(user)

                is_followed = False

            else:

                person.followers.add(user)

                is_followed = True

  

            # 팔로우 여부 보내주기

            context = {

                "is_followed": is_followed,

                "followers_count": person.followers.count(),

                "followings_count": person.followings.count(),

            }

            return JsonResponse(context)

        return redirect("accounts:profile", person.username)

    return redirect("accounts:login")
```
- 팔로우 여부를 context에 같이 보내줘서 팔로우가 되어있으면 팔로우 취소, 팔로우 안되어있으면 팔로우가 되도록 구현했다.
```python
            # 팔로우 여부 보내주기

            context = {
                "is_followed": is_followed,
            }
```

# B. 리뷰 좋아요 기능
```html
<form class="like-forms" data-review-id="{{review.pk}}">

      {% csrf_token %}

      {% if user in review.like_users.all %}

        <button id="like-{{review.pk}}">좋아요 취소</button>

      {% else %}

        <button id="like-{{review.pk}}">좋아요</button>

      {% endif %}

    </form>
```
```js
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

<script>

  const forms = document.querySelectorAll('.like-forms')

  console.log(forms)

  forms.forEach((form) => {

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    form.addEventListener('submit', function (event) {

      event.preventDefault()

      const reviewId = event.target.dataset.reviewId

      axios({

        method : 'post',

        url: `http://127.0.0.1:8000/community/${reviewId}/like/`,

        headers: {'X-CSRFToken': csrftoken},

      })

        .then((response) => {

          const isLiked = response.data.is_liked

          const likeBtn = document.querySelector(`#like-${reviewId}`)

          if (isLiked === true) {

            likeBtn.innerText = '젛아요 취소'

          } else {

            likeBtn.innerText = '젛아요'

          }

        })

        .catch((error) => {

          console.log(error)

        })

    })

  })

</script>
```
- 좋아요 버튼의 변화도 팔로우 버튼처럼 비동기화를 통해 구현했다
- 팔로우 기능 처럼 form의 제출을 막았다.
- 또한, 좋아요 여부를 view에서 response로 보내서 확인할 수 있도록 했다
# C. Movies 앱 기능 
## 1.  전체 영화 목록 조회
```python
#movies/views.py
@require_safe

def index(request):

    # 전체 영화 목록 가져오기

    movies = Movie.objects.all()

    context = {"movies": movies}

    print(context)

    return render(request, "movies/index.html", context)
```
- 단순히 movie데이터를 모두 가져와서 index.html 로 보내줬다
```html
<!--movies/index.html-->
{% block content %}

  <h1>Movies</h1>

  <hr>

  <a href="{% url 'movies:recommended' %}">영화 추천 받기</a>

  <hr>

  <!-- Movies List -->

  <main role="main" style="padding-top: 72.12px" >

    <div class="album  text-center">

      <div class="container">

        <div class="row">
		<!--여기서 부터 영화 데이터 반복문을 통해 나열-->
          {% for movie in movies %}

          <div class="col-md-4">

            <div class="card mb-4 box-shadow">
           
              <img class="card-img-top" style="display: block;" src="{{movie.poster_path}}" >

              <div class="card-body text-start">

                <h5 class="">

                  <a href="{% url 'movies:detail' movie.pk %}">

                    {{movie.title}}

                  </a>

                </h5>

                <p class="">
                <!--소속 장르를 반복문을 통해 나열-->
                <!--장르를 클릭하면 해당 장르의 영화만 볼 수 있음-->
                  {% for genre in movie.genres.all %}
                  
                  <a href="{% url 'movies:GenreDetail' genre.pk %}">

                    {{genre.name}}

                  </a>

                  {% endfor %}

                </p>

                <div class="d-flex justify-content-between align-items-center">

                  <div class="btn-group">

                    <button type="button" class="btn btn-sm btn-outline-secondary">View</button>

                    <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>

                  </div>

                  <small class="text-muted">9 mins</small>

                </div>

              </div>

            </div>

          </div>        

          {% endfor %}

        </div>

      </div>

    </div>  

  </main>

{% endblock %}
```
- 반복문을 통해 영화 정보를 나열 
- 추천 영화 보기 a태그를 통해 recommended로 이동할 수 있도록 함
- 반복문을 통해 각 영화의 장르르 나열 
- 각 영화의 장르는 a 태그를 이용해 해당 태그를 이용하면 GenreDetail url -> view로 가도록함
```python
@require_safe

def GenreDetail(request, genre_id):

    genre = Genre.objects.get(pk=genre_id)

    movies = genre.movie_set.all()

    context = {

        "movies": movies,

    }

    return render(request, "movies/index.html", context)
```
- 같은 index.html 을 쓰지만 보내주는 데이터를 해당 장르의 영화 데이터만 넣어서 보내줬다

## 2. 단일 영화 상세 조회
```python
@require_safe

def detail(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)

    context = {

        "movie": movie,

    }

    return render(request, "movies/detail.html", context)
```
- 단순히 영화 제목을 클릭하면 detail url로 이동하도록했고 pk를 같이 보내줘서 
해당 pk의 영화정보만 담을 수 있도록 했다

## 3. 영화 추천 기능(recommended)
```python
# community/forms.py
class ReviewForm(forms.ModelForm):

    try:

        choices = list(map(lambda x: (x.title, x.title), Movie.objects.all()))

    except:

        choices = []

    movie_title = forms.ChoiceField(choices=choices)

  

    class Meta:

        model = Review

        fields = ["title", "movie_title", "rank", "content"]
```
- 먼저 리뷰 form을 보자 
- try/except 로 나눈 이유는 choices에 movie의 객체들을 담아줘야 하는데 
처음 migration 을 할때는 movie데이터가 없기 때문에 try / except로 나누지 않으면 오류가 발생한다
- choice에 영화 데이터를 담고 이를 movie_title 필드에 ChoiceField로 설정해줘서 
리뷰를 생성할 때 영화제목을 입력하는 것이 아닌 선택을 해서 객체를 같이 넘겨줬다.
- 이 리뷰 생성할 때 같이 넣어주는 영화 객체를 추천 알고리즘에 사용할 것이다 
```python
@require_safe

def recommended(request):

    user = request.user

    if user.is_authenticated:

        # 10개 영화 추천

        recommneded_movies_priority_queue = []

        all_genres = set(Genre.objects.all())

        all_movie_ranking = Movie.objects.all().order_by("vote_average")

        all_movie_visited = [False] * len(all_movie_ranking)

        # 1. 좋아요한 영화의 장르 받기

        liked_reviews = user.like_reviews.all()

        print(liked_reviews)

        liked_movie_genres = set()

        for lr in liked_reviews:

            try:

                mv = Movie.objects.get(title=lr.movie_title)

                print(mv)

                gnrs = mv.genres.all()

                for gnr in gnrs:

                    liked_movie_genres.add(gnr)

            except:

                print("no matching mv title")

        print(f"liked: {liked_movie_genres}")

        # 2. 각 장르별 영화 추천

        # 3. 각 장르별 별점 기준 추천

        # 4. 각 장르 겹치는 수가 많을수록 먼저 추천

        if len(liked_movie_genres) == 0:

            liked_movie_genres = all_genres

        for idx, mv in enumerate(all_movie_ranking):

            # 해당 mv의 generes.all과 liked_genres와의 우선순위 구하기

            priority = len(liked_movie_genres.intersection(mv.genres.all()))

            if all_movie_visited[idx] == False:

                all_movie_visited[idx] = True

                heapq.heappush(recommneded_movies_priority_queue, (-priority, idx))

        print(recommneded_movies_priority_queue)

        cnt = 0

        recommneded_movies = []

        while cnt < 10:  # 우선순위 큐에서 10개만 뽑기

            popped = heapq.heappop(recommneded_movies_priority_queue)

            recommneded_movies.append(all_movie_ranking[popped[1]])

            cnt += 1

        print(recommneded_movies)

        context = {"recommneded_movies": recommneded_movies}

        return render(request, "movies/recommended.html", context)

    return redirect("moives:index")
```
- 사용자가 리뷰에 좋아요를 하게 되면 좋아요한 리뷰에 담긴 영화 객체들를 통해서 해당 영화들의 장르를 넣은 set를 만들어준다  
- 이 set를 이용해서 장르별로 영화를 거르고 
- heapq를 이용해 평점이 높은 순으로 10개를 pop을 해서 새로운 리스트에 담고
이 데이터를 넘겨줘서 recommended.html에 보내준다.
```html
{% extends 'base.html' %}

{% block content %}

  <h1>Recommended Movies for {{ user.username }}</h1>

  <hr>

  <main role="main" style="padding-top: 72.12px" >

    <div class="album  text-center">

      <div class="container">

        <div class="row">

  

          {% for movie in recommneded_movies %}

          <div class="col-md-4">

            <div class="card mb-4 box-shadow">

              <img class="card-img-top" style="display: block;" src="{{movie.poster_path}}" >

              <div class="card-body text-start">

                <h5 class="">

                  <a href="{% url 'movies:detail' movie.pk %}">

                    {{movie.title}}

                  </a>

                </h5>

                <p class="">

                  {% for genre in movie.genres.all %}

                    {{genre.name}}

                  {% endfor %}

                </p>

                <div class="d-flex justify-content-between align-items-center">

                  <div class="btn-group">

                    <button type="button" class="btn btn-sm btn-outline-secondary">View</button>

                    <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>

                  </div>

                  <small class="text-muted">9 mins</small>

                </div>

              </div>

            </div>

          </div>        

          {% endfor %}

  

        </div>

      </div>

    </div>  

  </main>

{% endblock %}
```
- recommended.html에서 영화 정보를 보여주는 방식은 index.html과 같다