<template>
  <nav class="tinted flex justify-between items-center h-14 border-gray-500 border-b p-3 shadow-md">
    <div class="flex items-center">
      <a class="flex items-center" href="">
        <img src="/static/images/poll.svg" class="w-10">
        <h1 class="font-thin text-lg ml-2">Pollapp</h1>
      </a>
      <div v-for="(item, index) in items" :key="item.name" class="ml-4">
        <a :href="item.link" class="border-b border-transparent hover:text-gray-500"
          :class="[index === current ? 'border-secondary-200' : 'border-transparent']">
          {{item.name}}
        </a>
      </div>
    </div>
    <div>
      <a class="font-bold hover:text-gray-500" href="">Logout</a>
    </div>
  </nav>
</template>

<script>
  import { ref, toRefs } from 'vue';
  export default {
    name: "Nav",

    props: {
      current: {
        type: Number,
        default: 0,
      },
    },

    setup(props, context) {
      const { current } = toRefs(props);
      const items = ref([
        { name: 'Home', link: '/' },
        { name: 'New Poll', link: '/new_poll' },
        { name: 'Settings', link: '/settings' },
      ]);

      return {
        items,
        current,
      }
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>