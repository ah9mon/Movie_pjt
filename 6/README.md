# pjt 06 
- 관계형 데이터베이스 설계 

## 목표
- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Django Model과 ORM에 대한 이해
- Django Authentication System에 대한 이해
- Database many to one relationship(1:N) 및 many to many relationship(M:N) 에 대한 이해

# Model

## A
```python
# movies/model.py 의 Movie 모델
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
```
- ForeignKey 를 이용해 게시글 작성자의 PK(게시글입장에선 FK) 활용
- ManyToManyField를 이용해 좋아요 누른 user의 PK와 Movie 게시글의 PK의 중계 테이블 생성 및 활용 

## B
```python
# movies/model.py 의 Comment 모델
movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```
- ForeignKey를 이용해 게시글의 PK 활용
- ForeignKey로 댓글단 user의 PK활용 

## C
```python
# accounts/models.py 의 User 모델
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
- ManyToManyField 로 user 간의 중계 테이블 생성 및 활용 

----
# Templates
## A Base.html
- `.is_authenticted` 를 활용한 로그인/비로그인 상태 구분
- 각 a tag와 submit form 에서 url로 보낼 때 어떤 것들을 같이 넘겨줘야 하는 지 (예를들어 pk) 신경 많이 씀
  - template -> url -> view -> template 이 사이클을 제대로 이해해야 가능했다

## B index.html
- `{% if request.user in movie.like_users.all %}` 를 사용해 좋아요/좋아요 취소 구분

## C detail.html
- 댓글이 보여지는 형태를 `작성자 : 댓글` 의 형태로 했는데 작성자를 a tag를 사용해 해당 작성자의 profile로 이동하도록 구현했다

## D create.html
- 로그인이 되어있지 않으면 새로운 영화 게시물을 작성하지 못하고 login 페이지로 리다이렉트 하도록 구현

## E update.html 
- D 처럼 로그인을 해야할 뿐만 아니라 해당 게시글의 작성자가 아니면 수정하지 못하도록 구현했다 

## F login.html
- `AbstractUser`
- 장고가 지원하는 로그인 프레임워크 폼을 사용 

## G Signup.html
- `CustomUserCreationForm(UserCreationForm)`
- 장고가 지원하는 회원가입 프레임워크 폼을 사용

## H update.html
- `CustomUserChangeForm(UserChangeForm)`
- 장고가 지원하는 개인정보 수정 프레임워크 폼을 사용 

## I change_password.html
- `PasswordChangeForm`
- 장고가 지원하는 비밀번호 수정 프레임워크 폼을 사용

## J 추가 필수 
- 영화 정보 생성 if 문 + `is_authenticated` 로 로그인 한 사람만 할수 있도록 구현

- 영화 정보 수정, 삭제는 해당 게시물의 작성자만 할 수 있도록 구현 (Model에 ForeignKey를 통해서 작성자의 user.pk를 FK로 사용했기때문에 구현할 수 있었음)

- 로그인 한 회원만 댓글 달수 있게함 (`is_authenticated`)

- 삭제는 로그인한 상태 + 작성자여야 삭제 가능 (`if request.user == comment.user`)

- 비밀번호 변경해도 로그인 상태 유지 
  - `update_session_auth_hash(request, form.user)` 를 통해서 구현 

- 본인은 팔로우 할 수 없음 
```python
person = User.objects.get(pk=user_pk)
if person != request.user:
```

## K 추가 과제 
- 팔로우, 팔로잉, 좋아요 수 profile.html 에서 볼 수 있음 

