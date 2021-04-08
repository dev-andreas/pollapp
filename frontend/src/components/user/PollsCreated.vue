<template>
  <div class="card py-4 col-span-1 justify-between">
    <div>
      <h2 class="text-2xl">Polls Created</h2>
      <Pagination class="mt-4" :items="$store.getters.getPollsCreated" @pageChanged="retrieveCurrentPage">
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
              <td class="text-left">
                <p class="font-bold">{{ poll.name }}</p>
              </td>
              <td class="text-left">
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
              <td>
                <p
                  class="group ml-2 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200">
                  <svg class="h-5 w-5 stroke-primary-500" fill="none" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </p>
              </td>
            </tr>
          </table>
        </template>
        <template v-slot:noItems>No polls created.</template>
      </Pagination>
    </div>
    <div class="flex w-full pr-2 mt-8 justify-end">
      <router-link class="btn-primary" to="">Create new poll</router-link>
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