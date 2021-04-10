<template>
  <nav
    class="tinted flex justify-between items-center h-14 border-gray-500 border-b p-3 shadow-md z-50"
  >
    <div class="flex items-center">
      <router-link class="flex items-center" :to="{ name: links[0].name }">
        <img src="/static/images/poll.svg" class="w-8" />
        <h1 class="font-thin text-lg ml-3">Pollapp</h1>
      </router-link>
      <div v-for="(item, index) in links" :key="index" class="ml-4">
        <router-link
          :to="{ name: item.link }"
          class="text-font-dark font-normal border-b border-transparent hover:text-gray-500"
          :class="[
            index === current ? 'border-primary-200' : 'border-transparent',
          ]"
        >
          {{ item.name }}
        </router-link>
      </div>
    </div>
    <div>
      <a class="font-bold cursor-pointer hover:text-gray-500" href="/" @click="logout()">Logout</a>
    </div>
  </nav>
</template>

<script>
import { ref, toRefs } from "vue";
import axios from "axios"
export default {
  name: "Nav",

  props: {
    links: {
      type: Array,
      default: [{ name: "Home", link: "Home" }],
    },
    current: {
      type: Number,
      default: 0,
    },
  },

  setup(props, context) {
    const { links, current } = toRefs(props);

    function logout() {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/logout/',
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
      });
    }

    return {
      links,
      current,
      logout,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>