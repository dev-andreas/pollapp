<template>
  <div class="flex flex-col min-h-screen">
    <Nav/>
    <router-view />
  </div>
</template>

<script>
import { ref } from "vue";
import Nav from "../../components/Nav.vue"
export default {
  components: {
    Nav,
  },
  setup() {},
};
</script>

<style>
</style>