<template>
  <div class="card py-4 col-span-1 justify-between px-2">
    <div class="flex flex-col items-center">
      <h2 class="text-2xl">Polls Voted</h2>
      <Pagination
        class="mt-4"
        :items="$store.getters.getPollsVoted"
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
            <tr v-for="poll in polls" :key="poll.item.id_hashed">
              <td>
                <p class="font-bold break-all">{{ poll.item.title }}</p>
              </td>
              <td>
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
            </tr>
          </table>
        </template>
        <template v-slot:noItems>No polls voted.</template>
      </Pagination>
    </div>
    <form
      class="flex w-full pr-2 mt-8 justify-end justify-self-end"
      @submit.prevent=""
    >
      <input class="inpt" type="text" placeholder="hash" v-model="pollHash" />
      <input
        class="btn-primary"
        type="submit"
        value="Visit poll"
        @click="visitPoll"
      />
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import Pagination from "../ItemPagination.vue";
import EyeSvg from "../svgpaths/EyeSvg.vue";
export default {
  components: {
    Pagination,
    EyeSvg,
  },

  setup() {
    const polls = ref([]);
    const pollHash = ref("");

    const router = useRouter();

    const retrieveCurrentPage = (list) => {
      polls.value = list;
    };

    const visitPoll = () => {
      router.push({
        name: "Poll",
        params: { id_hashed: pollHash.value.toLowerCase() },
      });
    };

    return {
      polls,
      retrieveCurrentPage,
      pollHash,
      visitPoll,
    };
  },
};
</script>

<style>
</style>