<template>
  <div>
    <h1>Random</h1>
    <div>
      <img :src="getPoster(randomMovie.poster_path)">
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomView',
  computed : {
    randomMovie(){
      const index = Math.floor(Math.random() * 20)
      console.log(this.$store.state.topRatedMovies[index])
      return this.$store.state.topRatedMovies[index]
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