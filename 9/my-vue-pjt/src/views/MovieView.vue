<template>
  <div>
    <h1>Movies</h1>
    <MovieCard />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue'


export default {
  name : 'MovieView',
  components : {
    MovieCard,
  },
  methods : {
    getMovies() {
      const api_key = ''
      const movies_api = `https://api.themoviedb.org/3/movie/top_rated?api_key=${api_key}&page=1`
      
      axios({
        method : 'get',
        url : movies_api
      })
      .then((res)=>{
        console.log(res.data)
        this.$store.dispatch('getMovies',res.data)
      })
      .catch((err)=> {
        console.log(err)
      })
    }
  },
  created () {
    this.getMovies()
  }

}
</script>

<style>

</style>