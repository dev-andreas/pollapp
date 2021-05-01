<template>
  <transition v-if="notFound" name="appear" appear>
    <NotExist />
  </transition>

  <!-- Actual content -->

  <transition v-else name="appear" appear>
    <div class="flex flex-col justify-center items-center">
      <h1 class="grid justify-center text-5xl font-extralight mb-5 mt-10">
        <span v-if="fetching" class="flex">
          <LoadingShape class="mr-4" />
          Loading...
        </span>
        <span v-else>
          {{ poll.title }}
        </span>
      </h1>
      <h2
        v-if="!fetching"
        class="max-h-32 break-words text-xl font-bold p-3 border-b overflow-y-auto"
      >
        {{ poll.description }}
      </h2>
      <div v-if="!fetching" class="grid grid-cols-3 gap-5 h-80 mt-5">
        <!-- Graph -->

        <div class="card justify-end col-span-2">
          <ItemPagination
            :items="showResults ? choices : []"
            :itemsPerPage="6"
            @pageChanged="getCurrentPage"
            class="flex flex-col justify-end h-full p-5"
          >
            <template v-slot:default>
              <div
                v-if="showResults"
                class="flex items-end justify-center h-60 justify-self-center mt-auto"
              >
                <div
                  v-for="choice in currentPage"
                  :key="choice.item.id"
                  class="px-5 flex flex-col items-end h-full transform hover:scale-110 transition ease-out duration-200"
                >
                  <div
                    class="flex items-end h-full border-font-dark"
                  >
                    <p
                      style="writing-mode: vertical-rl"
                      class="text-xs font-bold transform rotate-180"
                    >
                      {{ choice.item.name }}
                    </p>
                    <div class="text-center">
                      <p class="text-sm">{{ choice.item.votes }}</p>

                      <transition name="rise" appear>
                        <div
                          class="w-6 bg-primary-500 border-b border-font-dark"
                          :style="{
                            height:
                              (choice.item.votes / mostVoted) * 12 + 'rem',
                          }"
                        ></div>
                      </transition>
                    </div>
                  </div>
                  <p class="text-xs">
                    {{
                      votesAmt > 0
                        ? Math.round((choice.item.votes / votesAmt) * 1000) / 10
                        : 0
                    }}%
                  </p>
                </div>
              </div>
            </template>
            <template v-slot:noItems>
              <div class="flex flex-col items-center mb-10 transform hover:scale-110 transition ease-out duration-500">
                <ChartSvg class="w-20 h-20 fill-primary-500" />
                <p class="text-3xl font-light">
                  Results visible here when poll is finished.
                </p>
              </div>
            </template>
          </ItemPagination>
        </div>

        <!-- Information -->

        <div class="card p-2 items-start justify-between w-80">
          <div v-if="!fetching" class="flex flex-col items-start p-3">
            <p class="text-3xl font-bold break-all">
              Created by {{ owner.username }}
            </p>
            <p class="font-light text-lg mb-5">Hash: {{ poll.id_hashed }}</p>

            <p>{{ beautifyDate(poll.date_to_start) }}</p>
            <p class="font-light text-xs mb-3">Starting at</p>

            <p>{{ beautifyDate(poll.date_to_end) }}</p>
            <p class="font-light text-xs mb-3">Deadline</p>

            <p v-if="poll.voters">{{ poll.voters.length }}</p>
            <p v-if="poll.voters" class="font-light text-xs mb-3">Voters</p>
          </div>
          <router-link
            class="btn-primary self-end"
            :to="{ name: 'Vote', params: route.id_hashed }"
            >Go Vote</router-link
          >
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, computed, onMounted } from "vue";
import { useRouter, useRoute, onBeforeRouteUpdate } from "vue-router";
import { useStore } from "vuex";
import { DateTime } from "luxon";
import { useFetching } from "../../../assets/utils.js";
import NotExist from "../../../components/poll/NotExist.vue"
import LoadingShape from "../../../components/LoadingShape.vue";
import ItemPagination from "../../../components/ItemPagination.vue";
import ArrowLeftSvg from "../../../components/svgpaths/ArrowLeftSvg.vue";
import ChartSvg from '../../../components/svgpaths/ChartSvg.vue';
export default {
  components: {
    NotExist,
    LoadingShape,
    ItemPagination,
    ArrowLeftSvg,
    ChartSvg,
    ChartSvg,
  },
  setup() {
    // router and vuex

    const store = useStore();
    store.commit("setCurrentPage", -1);

    const router = useRouter();
    const route = useRoute();
  

    // poll stuff

    const poll = ref("");
    const choices = ref([
      {name: 'PHP', votes: 3, },
      {name: 'C#', votes: 5, },
      {name: 'Python', votes: 10, },
      {name: 'JavaScript', votes: 7, },
      {name: 'Java', votes: 8, },
    ]);
    const showResults = ref(false);

    const owner = ref({});

    const currentPage = ref([]);

    const votesAmt = computed(() => {
      return choices.value.reduce((curr, next) => curr + next.votes, 0);
    });

    const mostVoted = computed(() => {
      let maxVal = 0;
      choices.value.forEach((choice) => {
        if (choice.votes > maxVal) {
          maxVal = choice.votes;
        }
      });
      return maxVal;
    });

    const beautifyDate = (date) => {
      return DateTime.fromISO(date).toLocaleString(DateTime.DATETIME_FULL);
    };

    // loading stuff

    const { fetching, notFound, fetchData } = useFetching();

    onMounted(() => {
      fetchPoll();
    });

    onBeforeRouteUpdate((to, from) => {
      route.params.id_hashed = to.params.id_hashed;
      fetchPoll();
    });

    const fetchPoll = () => {

      fetchData(store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}/`).then((res) => {
        poll.value = res.data.poll;
        //choices.value = res.data.choices.reverse();
        showResults.value = typeof choices.value[0].votes !== 'undefined';
        owner.value = res.data.poll_owner;
      });

    };

    const getCurrentPage = (items) => {
      currentPage.value = items;
    };

    return {
      notFound,
      fetching,
      route,
      poll,
      choices,
      owner,
      beautifyDate,
      votesAmt,
      currentPage,
      getCurrentPage,
      mostVoted,
      showResults,
    };
  },
};
</script>
<style>
</style>