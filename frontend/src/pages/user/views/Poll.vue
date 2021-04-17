<template></template>

<script>
import { useStore } from "vuex";
export default {
  setup() {
    const store = useStore();
    store.commit("setCurrentPage", -1);
  },
};
</script>

<style>
</style>