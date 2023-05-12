<template>
  <div>
    <form @submit.prevent>
      <input type="text" v-model="wishMovie" placeholder="ex) 가디언즈 오브 갤럭시 vol.3" >
      <button @click="createWishMovie">Add</button>
    </form>
    <WatchListItem v-for="(movie, index) in wishMovies" :key="index" :movie="movie"/>
  </div>
</template>

<script>
import WatchListItem from './WatchListItem.vue'
export default {
  name:'WatchListForm',
  data () {
    return {
      wishMovie : null
    }
  },
  components : {
    WatchListItem
  },
  methods: {
    createWishMovie(){
        const wishMovieTitle = this.wishMovie.trim()
        if (wishMovieTitle) {
          this.$store.dispatch('createWishMovie', wishMovieTitle)
          this.wishMovie =""
        } else {
          alert('보고싶은 영화 제목을 입력하세요')
        }
      },
  },
  computed : {
    wishMovies(){
      console.log(this.$store.state.wishMovies)
      return this.$store.state.wishMovies
    }
  },

}
</script>

<style>

</style>