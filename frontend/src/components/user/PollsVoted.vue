<template>
  <div class="card py-4 col-span-1 justify-between">
    <div>
      <h2 class="text-2xl">Polls Voted</h2>
      <Pagination class="mt-4" :items="$store.getters.getPollsVoted" @pageChanged="retrieveCurrentPage">
        <template v-slot:default>
          <table>
            <tr>
              <th class="text-left text-xs">
                <p>Name</p>
              </th>
              <th class="text-left text-xs">
                <p class="ml-4">Hash</p>
              </th>
            </tr>
            <tr v-for="poll in polls" :key="poll.hash">
              <td>
                <p class="font-bold">{{ poll.name }}</p>
              </td>
              <td>
                <p class="ml-4 text-xs">{{ poll.hash }}</p>
              </td>
              <td>
                <p
                  class="group ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200">
                  <svg class="h-5 w-5 stroke-primary-500" fill="none" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </p>
              </td>
            </tr>
          </table>
        </template>
        <template v-slot:noItems>No polls voted.</template>
      </Pagination>
    </div>
    <div class="flex w-full pr-2 mt-8 justify-end justify-self-end">
      <input
        class="border px-1 w-40 hover:shadow focus:shadow focus:border-primary-400 transition ease-out duration-200"
        type="text" placeholder="hash" />
      <router-link class="btn-primary" to="">Visit poll</router-link>
    </div>
  </div>
</template>

<script>
  import { ref } from "vue";
  import Pagination from "../ItemPagination.vue";
  export default {
    components: {
      Pagination,
    },

    setup() {
      const polls = ref([]);

      const retrieveCurrentPage = (list) => {
        polls.value = list;
      };

      return {
        polls,
        retrieveCurrentPage,
      };
    },
  };
</script>

<style>
</style>