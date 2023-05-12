<template>
  <div>
    <div v-for="topRatedMovie in topRatedMovieList" 
    :key="topRatedMovie.id">
      <hr>

      <p><b>{{ topRatedMovie.title }}</b></p>
      <img :src="getPoster(topRatedMovie.poster_path)">
      
    </div>

  </div>
</template>

<script>

export default {
  name:'MovieCard',
  computed : {
    topRatedMovieList(){
      return this.$store.state.topRatedMovies
    }
  },
  methods : {
    getPoster(posterPath){
      // console.log(`https://image.tmdb.org/t/p/w500${posterPath}`)
      return `https://image.tmdb.org/t/p/w500${posterPath}`
    }
  },

}
</script>

<style>

</style>