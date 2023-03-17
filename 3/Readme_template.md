>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 03

### 이번 pjt 를 통해 배운 내용

* 내가 원하는 결과가 눈에 보이니 재밌다

## A. 01_nav_footer.html

* 요구 사항 : navbar 및 login에 modal기능 추가하기 

* 결과 : 
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-19-20-image.png)
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-19-37-image.png)
  
  * 문제 접근 방법 및 코드 설명
  
  ```python
  여기에 관련 작성 코드 복붙!   
  <!--navbar-->   
  <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
  
          <a class="navbar-brand" href="/02_home.html"><img src="logo.png" width="120px"></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/02_home.html">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/03_community.html">Community</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
              </li>
            </ul>
  
          </div>
        </div>
      </nav>
    </header>
  
  <!--modal-->
  
  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <!-- Email input -->
            <div class="form-outline mb-4">
              <p class="fs-5">Email address</p>
              <input type="email" id="form3Example3" class="form-control form-control-lg" placeholder="Enter a valid email address">
              <label class="form-label text-secondary"  for="form3Example3" style="margin-left: 0px;">We'll never share your email with anyone else.</label>
              <div class="form-notch"><div class="form-notch-leading" style="width: 9px;"></div><div class="form-notch-middle" style="width: 88.8px;"></div><div class="form-notch-trailing"></div></div></div>
              
              <!-- Password input -->
              <div class="form-outline mb-3">
              <p class="fs-5">Password</p>
              <input type="password" id="form3Example4" class="form-control form-control-lg" placeholder="Enter password">
            <div class="form-notch"><div class="form-notch-leading" style="width: 9px;"></div><div class="form-notch-middle" style="width: 64.8px;"></div><div class="form-notch-trailing"></div></div></div>
  
            <div class="d-flex justify-content-between align-items-center">
              <!-- Checkbox -->
              <div class="form-check mb-0">
                <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3">
                <label class="form-check-label" for="form2Example3">
                  Check me out
                </label>
              </div>
              <a href="#!" class="text-body">Forgot password?</a>
            </div>
  
            <div class="text-center text-lg-start mt-4 pt-2">
              <p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <a href="#!" class="link-danger">Register</a></p>
            </div>
  
          </form>
          
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
  ```
  
  * modal을 처음 만들어봤고 modal의 위치에 따라 실행여부가 결정되어서 어려웠다
  * 내가 생각하는 이 문제의 포인트
    - 이미 주어진 코드를 이해하고 내가 원하는 방향으로 변형시키는 과정 

-----

## B. 02_home.html

- 요구사항 : section 파트 만들기 

- 결과
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-23-15-image.png)
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-23-39-image.png)

- 문제 해결 방법 및 코드
  
  ```html
    <main role="main" style="padding-top: 72.12px" >
      <div class="album  text-center">
        <div class="container">
          <div class="row">
            <img src="header1.jpg" class="w-auto h-auto">
            <h1 class="py-4 fw-bold">Boxoffice</h1>
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" style="display: block;" src="movie1.jpg" >
                <div class="card-body text-start">
                  <h5 class="">card title</h5>
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="movie2.jpg"  style=" display: block;">
                <div class="card-body text-start">
                  <h5 class="">card title</h5>       
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="movie3.jpg" style=" display: block;">
                <div class="card-body text-start">
                  <h5 class="">card title</h5>                  
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="movie4.jpg" style=" display: block;">
                <div class="card-body text-start">
                  <h5 class="">card title</h5>
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="movie5.jpg" style=" display: block;">
                <div class="card-body text-start">
                  <h5 class="">card title</h5>                  
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="movie6.jpg" style=" display: block;">
                <div class="card-body text-start">
                  <h5 class="">card title</h5>
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
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
            
          </div>
        </div>
      </div>   
    </main>
  ```

- 내가 생각하는 이 문제의 포인트
  
  - 이미 주어진 코드를 이해하고 내가 원하는 방향으로 변형시키는 과정
    
    

# ## 03_community.html

- 요구사항 : 브라우저 크기에 따라 반응하는 게시글 목록 만들기 

- 결과 
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-33-16-image.png)
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-17-15-33-41-image.png)



- 내가 생각하는 이 문제의 포인트
  
  - 이미 주어진 코드를 이해하고 내가 원하는 방향으로 변형시키는 과정

# 후기

* 오픈소스를 가져다가 사용하는 것도 쉽지 않다 
* 최대한 영어로된 공식문서를 보려했으나 어렵다 
* 영어공부도 열심히 해야할 것 같다 
  
  
