<template>
  <div>
    <h1>날씨</h1>
    <form @submit.prevent>
      <input type="text" placeholder="ex) Seoul" v-model="city">
      <button @click="findWeather">{{ city? city:defaultCity }}의 현재 날씨 찾기</button>
    </form>
    <div v-if="weather" style="color:white; background-color: skyblue;">
      <hr>
      <h2>{{ weather.name }}은 지금 {{ weather.weather[0].main }}</h2>
      <img :src="weatherIconUrl" width="70">
      <p><b>기온 : {{ Math.floor(weather.main.temp - 273.15) }}℃</b></p>
      <p>최저기온 : {{ Math.floor(weather.main.temp_min - 273.15) }}℃</p>
      <p>최고기온 : {{ Math.floor(weather.main.temp_max - 273.15) }}℃</p>
      <br>
    
    </div>
    <!--영화추천-->
    <div v-if="recommendMovies">
      <hr>
      <h2>오늘같은 날씨는 이런 영화를 추천해요!</h2>
      <div v-for="movie in recommendMovies" :key="movie.id" :movie="movie">
        <img :src="getPoster(movie.poster_path)">
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'WeatherView',
  data () {
    return {
      defaultCity : '원하는 도시',
      city : null,
      weather : null,
      weatherIconUrl : null
    }
  },
  methods : {
    findWeather(){
      const API_key = "" 
      const weatherUrl = `http://api.openweathermap.org/data/2.5/weather?q=${this.city}&appid=${API_key}`
      console.log(weatherUrl)
      this.$store.dispatch('deleteRecommend')
      axios({
        method : 'get',
        url : weatherUrl 
      })
      .then((res)=>{
        // console.log(res,1)
        this.weather = res.data
        this.weatherIconUrl = `https://openweathermap.org/img/wn/${res.data.weather[0].icon}.png`
        // 날씨 id를 통한 영화 장르 분류 
        this.$store.dispatch('recommendMovie', this.weather.weather[0].id)
      })
      .catch((err)=>{
        console.log(err,4)
      })

      this.city =""
    },
    findGenre(){
      const api_key = ""
      const genreUrl =`https://api.themoviedb.org/3/genre/movie/list?api_key=${api_key}&language=en-US`
      axios({
        method : 'get',
        url: genreUrl
      })
      .then((res)=>{
        this.$store.dispatch('getGenre',res.data)
      })
    },
    getPoster(posterPath){
      // console.log(`https://image.tmdb.org/t/p/w500${posterPath}`)
      return `https://image.tmdb.org/t/p/w500${posterPath}`
    }
  },
  computed : {
    recommendMovies(){
      return this.$store.state.recommendMovie
    }
  },
  created() {
    this.$store.dispatch('deleteRecommend')
    this.findGenre()
  }
}
</script>

<style>

</style>