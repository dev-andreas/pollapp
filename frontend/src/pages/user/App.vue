<template>
  <div class="flex flex-col min-h-screen">
    <Nav :links="$store.getters.getNavLinks" :current="currentPage"/>
    <router-view/>
  </div>
</template>

<script>
import { ref, computed, onMounted } from "vue"
import { useStore } from "vuex"
import NavBar from "../../components/NavBar.vue"
export default {
  components: {
    Nav: NavBar,
  },
  setup() {
    const store = useStore();

    onMounted(() => {
      store.dispatch('loadUserData');
      store.dispatch('loadPollData');
    });

    const currentPage = computed(() => {
      return store.state.currentPage;
    });

    return { currentPage }
  }
};
</script>

<style>
</style>