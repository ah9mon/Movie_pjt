# Vue를 활용한 SPA 구성 

## 목표 
- 영화 정보를 제공하는 SPA제작 
- AJAX 통신과 JSON 구조에 대한 이해 
- VUE CLI, VUE Router 플러그인 활용

## 사용 API
- TMDB API
  - https://developers.themoviedb.org/3/movies/get top rated movies

- OpenWeather API
  - https://openweathermap.org/current

## 컴포넌트 구조 
![1](READ_ME_img/1.png)

## router view
![2](READ_ME_img/2.png)
```js
<template>
  <div id="app">
    <nav>

      <router-link to="/">Movie</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/weather">Weather</router-link> | 
      <router-link to="/watchlist">WatchList</router-link> 

    </nav>
    <router-view/>
  </div>
</template>
```
```js
const routes = [

  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/watchlist',
    name: 'watchlist',
    component: WatchListView
  },
  {
    path: '/weather',
    name: 'weather',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "weather" */ '../views/WeatherView.vue')
  },
  {
    path: '/random',
    name: 'random',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "random" */ '../views/RandomView.vue')
  }
]
```
## vuex
```js
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    topRatedMovies : null,
    wishMovies : [],
    genres: null,
    recommendMovie : null
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state,movies) {
      state.topRatedMovies = movies
      console.log('dasd',state.topRatedMovies)
    },
    CREATE_WISH_MOVIE(state,wishMovieTitle){
      const isCompleted = false
      state.wishMovies.push({wishMovieTitle, isCompleted})
    },
    UPDATE_COMPLETED(state,wishmovie){
      state.wishMovies.map((movie)=>{
        if (movie === wishmovie) {
          movie.isCompleted = !movie.isCompleted
        }
      })
    },
    GET_GENRES(state, genres){
      state.genres = genres
    },
    RECOMMEND_MOVIES(state, movies){
      state.recommendMovie = movies
    },
    DELETE_RECOMMEND(state){
      state.recommendMovie = null
    }
  },
  actions: {
    getMovies(context, movies){
      context.commit('GET_MOVIES', movies.results)
    },
    createWishMovie(context, wishMovieTitle){
      // console.log(context)
      // console.log(wishMovieTitle)
      context.commit('CREATE_WISH_MOVIE', wishMovieTitle)
    },
    completed(context, wishmovie){
      context.commit('UPDATE_COMPLETED', wishmovie)
    },
    recommendMovie(context, weatherId){
      const genre = this.state.genres.genres[Number(String(weatherId)[0])]
      const movies = []
      // console.log('추천장르번호',genre.id)
      this.state.topRatedMovies.map((movie)=>{
        // console.log('영화',movie)
        // console.log('영화장르',movie.genre_ids)
        if (movie.genre_ids.includes(genre.id)) {
          // console.log(movie)
          movies.push(movie)
        }
      })
      context.commit('RECOMMEND_MOVIES',movies)
    },
    getGenre(context, genres){
      // console.log(context)
      // console.log(genres)
      context.commit('GET_GENRES',genres)
    },
    deleteRecommend(context){
      context.commit('DELETE_RECOMMEND')
    }
  },
  modules: {
  }
})
```
- 각종 components와 view에서 사용할 데이터 vuex로 다룸
- 또한 불러온 데이터를 plugins으로 브라우저에서 저장해서 활용 
## A 최고 평점 영화 출력 
- Movie링크를 클릭하면 AJAX 통신을 이용해 TMDB API로 부터 JSON데이터를 받아와 영화목록 출력 
![2](READ_ME_img/3.png)

1. MovieView.vue에서 비동기로 영화 데이터 가져오기 
2. 그 response를 store에 보내서 action -> mutation -> state에 있는 데이터 수정순으로 저장
3. 해당 영화 데이터를 자식 컴포넌트인 MovieCard.vue가 store에서 꺼내서 모두 출력
## B 최고 평점 영화 중 랜덤 영화 한개 출력 
- Random 링크를 클릭하면 저장된 최고 평점 영화 목록 중 랜덤으로 한 개를 출력
![2](READ_ME_img/4.png)

1. RandomView.vue에서 Math.random을 활용해 인덱스를 랜덤으로 정함
2. A에서 가져온 영화 데이터중 해당 인덱스의 영화 객체를 store에서 꺼내와 출력 

## C 보고싶은 영화 등록 및 시청완료 표시하기
- 네비게이션바에서 WatchList 링크 (/watch list) 를 클릭하면
보고 싶은 영화 제목을 등록할 수 있는 Form 이 출력
- 등록된 영화 제목을 클릭하면 취소선이 그어짐
![2](READ_ME_img/5.png)

1. 구조 : WatchView - WatchListForm - WatchListItem
2. WatchListForm에서 영화제목 입력하면 해당 영화 제목을 vuex로 저장 
3. WatchListItem에서 Item들을 출력

## D 현재 날씨에 따른 영화 추천하기 
- RandomView에서 도시를 입력하면 OpenWeather API 로 부터 해당 도시의 현재 날씨 정보와
현재 날씨와 연관시킨 영화 장르를 선별하고 해당 장르 소속인 영화를 A에서 저장한 영화 리스트에서 꺼내서 출력 
![2](READ_ME_img/6.png)

1. WeatherView 키자마자 영화 장르 리스트  API에서 비동기로 가져옴
2. input에 도시를 입력하면 해당 도시의 날씨 정보를 API에서 비동기로 가져옴 
3. 날씨 정보엔 날씨ID가 있다 100번대 ~ 800번대까지 있음
4. 앞자리만 따서 (예를들어 100번대면 1, 200번대면 2) 인덱스로 활용
5. 1에서 가져온 장르리스트에서 `장르리스트[4에서 뗀 인덱스]` 로 장르 꺼냄 
6. map으로 A에서 저장한 영화리스트에서 5에서 꺼낸 장르랑 같은 장르의 영화있으면 모두 리스트에 담고 
7. state에 저장 
8. 해당 추천영화리스트를 출력