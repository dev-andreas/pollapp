<template>
  <div
    class="flex flex-col self-center mt-20 w-desktop col-span-2 border-b pb-2"
  >
    <div class="flex">
      <img class="w-24" src="/static/images/cross.svg" alt="Cross" />
      <h1 class="text-9xl font-extralight">404!</h1>
    </div>
    <h2 class="text-2xl font-light">
      Poll doesn't exist. Maybe you should try in another universe.
    </h2>
    <router-link
      class="self-end btn-primary flex items-center mt-2"
      :to="{ name: 'Home' }"
    >
      <ArrowLeftSvg class="h-5 w-5 mr-2" />
      <p>go home</p>
    </router-link>
  </div>
</template>

<script>
import ArrowLeftSvg from "../svgpaths/ArrowLeftSvg";
export default {
  components: {
    ArrowLeftSvg,
  },
};
</script>

<style>
</style>