<template>
  <div @click="completed" :class="{'is-completed':movie.isCompleted === true}">
    {{ movie.wishMovieTitle }}
    <br>
  </div>
</template>

<script>
export default {
  name:'WatchListItem',
  props : {
    movie: Object
  },
  methods : {
    completed(){
      this.$store.dispatch('completed', this.movie)
    }
  }


}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>