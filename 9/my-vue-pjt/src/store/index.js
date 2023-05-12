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
  
      this.state.topRatedMovies.map((movie)=>{
 
        if (movie.genre_ids.includes(genre.id)) {
   
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
