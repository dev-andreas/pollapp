<template>
  <div class="flex flex-col min-h-screen">
    <Nav :links="$store.getters.getNavLinks" :current="$store.state.currentPage"/>
    <router-view />
  </div>
</template>

<script>
import { ref } from "vue";
import NavBar from "../../components/NavBar.vue"
export default {
  components: {
    Nav: NavBar,
  },
  setup() {},
};
</script>

<style>
</style>