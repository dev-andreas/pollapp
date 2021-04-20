<template>
  <transition name="appear" appear>
    <div class="grid grid-cols-2 gap-5 w-desktop self-center mt-20">

      <div class="card col-span-2 py-24">
        <h1 class="text-9xl font-extralight">404!</h1>
        <h2 class="text-2xl font-light">Poll doesn't exist. Maybe you should try in another universe.</h2>
      </div>
      <div class="card col-span-1">
        <h2 class="text-2xl pt-5 mb-5">Poll info</h2>
      </div>
      <div class="card col-span-1">
        <h2 class="text-2xl pt-5 mb-5">Description</h2>
      </div>
    </div>
  </transition>
</template>

<script>
  import { ref, watch, onMounted } from "vue";
  import { useRouter, useRoute, onBeforeRouteUpdate } from "vue-router";
  import { useStore } from "vuex";
  import { makeRequest } from "../../../assets/utils.js";
  export default {
    setup() {
      const store = useStore();
      store.commit("setCurrentPage", -1);

      const router = useRouter();
      const route = useRoute();

      const notFound = ref(false);
      const fetching = ref(true);

      onMounted(() => {
        fetchData();
      });

      onBeforeRouteUpdate(() => {
        fetchData();
      });

      const fetchData = () => {
        notFound.value = false;
        fetching.value = true;

        makeRequest(
          "GET",
          store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}/`
        )
          .then((res) => { })
          .catch((err) => {
            notFound.value = true;
          })
          .finally(() => {
            fetching.value = false;
          });
      };

      return {
        notFound,
        route
      };
    },
  };
</script>

<style>
</style>