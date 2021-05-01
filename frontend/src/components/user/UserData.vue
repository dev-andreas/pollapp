<template>
  <div class="col-span-2 flex flex-col border-b pt-8">
    <div class="flex justify-center items-center">
      <img :src="$store.getters.getProfilePic"
        class="object-cover w-40 h-40 rounded-full bg-white border-2 border-primary-500">
      <div class="flex flex-col justify-center ml-6">
        <h1 class="text-6xl font-extralight">
          Hello,
          <span v-if="$store.getters.getUser.first_name !== ''">
            {{ $store.getters.getUser.first_name }}
          </span>
          <span v-else> {{ $store.getters.getUser.username }} </span>!
        </h1>
        <table class="text-sm mt-4">
          <tr>
            <td class="font-bold">Username:</td>
            <td>
              <p class="ml-3">{{ $store.getters.getUser.username }}</p>
            </td>
          </tr>
          <tr>
            <td class="font-bold">E-Mail:</td>
            <td>
              <p class="ml-3">{{ $store.getters.getUser.email }}</p>
            </td>
          </tr>
          <td class="font-bold">Joined:</td>
          <td>
            <p class="ml-3">{{ $store.getters.getDateJoined }}</p>
          </td>
        </table>
      </div>
    </div>
    <router-link :to="{ name: 'UserSettings' }"
      class="group self-end mr-2 mb-2 p-2 rounded-full hover:bg-primary-500 hover:shadow-md transition ease-out duration-200">
      <PencilSvg class="h-6 w-6 transition stroke-primary-500 group-hover:stroke-white ease-out duration-200" />
    </router-link>
  </div>
</template>

<script>
  import PencilSvg from "../svgpaths/PencilSvg.vue";
  export default {
    components: {
      PencilSvg,
    },
  };
</script>

<style>
</style>