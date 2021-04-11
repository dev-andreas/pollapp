<template>
  <h1>Create Poll</h1>
</template>

<script>
import { useStore } from 'vuex'

export default {
  setup() {
    const store = useStore();
    store.commit("setCurrentPage", 2);
  },
};
</script>

<style>
</style>