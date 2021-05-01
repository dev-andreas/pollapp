<template>
  <div class="card py-4 col-span-1 justify-between">
    <div class="flex flex-col items-center">
      <h2 class="text-2xl">Polls Created</h2>
      <Pagination
        class="mt-4"
        :items="$store.getters.getPollsCreated"
        @pageChanged="retrieveCurrentPage"
      >
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
            <tr v-for="poll in polls" :key="poll.item.hash">
              <td class="text-left">
                <p class="font-bold break-all">{{ poll.item.title }}</p>
              </td>
              <td class="text-left">
                <p class="ml-4 text-xs">{{ poll.item.id_hashed }}</p>
              </td>
              <td>
                <router-link
                  :to="{
                    name: 'Poll',
                    params: { id_hashed: poll.item.id_hashed.toLowerCase() },
                  }"
                >
                  <p
                    class="group ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                  >
                    <EyeSvg class="'h-5 w-5 stroke-primary-500"></EyeSvg>
                  </p>
                </router-link>
              </td>
              <td>
                <router-link
                  :to="{
                    name: 'PollSettings',
                    params: { id_hashed: poll.item.id_hashed.toLowerCase() },
                  }"
                >
                  <p
                    class="group ml-2 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                  >
                    <CogSvg class="h-5 w-5 stroke-primary-500"></CogSvg>
                  </p>
                </router-link>
              </td>
            </tr>
          </table>
        </template>
        <template v-slot:noItems>No polls created.</template>
      </Pagination>
    </div>
    <div class="flex w-full pr-2 mt-8 justify-end">
      <router-link class="btn-primary mx-2" :to="{ name: 'NewPoll' }"
        >Create new poll</router-link
      >
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import Pagination from "../ItemPagination.vue";
import CogSvg from "../svgpaths/CogSvg.vue";
import EyeSvg from "../svgpaths/EyeSvg.vue";
export default {
  components: {
    Pagination,
    CogSvg,
    EyeSvg,
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