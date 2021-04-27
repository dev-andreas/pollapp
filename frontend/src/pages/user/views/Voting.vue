<template>
  <transition v-if="notFound">
    <NotExist />
  </transition>
  <transition v-else name="appear" appear>
    <div class="flex flex-col justify-center items-center mt-20">
      <LoadingShape v-if="fetching" />
      <div v-else class="card w-phone items-center">
        <h2 class="text-3xl mt-5">{{ poll.title }}</h2>

        <p class="mx-3 my-5 text-center text-sm">
          You have {{ poll.votes_amt }} vote(s).
          <span v-if="poll.less_allowed"
            >Less votes are also allowed in this poll.</span
          >
          Please tick the boxes below to give a vote.
        </p>

        <div v-for="choice in choices" :key="choice.id">
          <p class="text-lg font-bold">
            {{ choice.name }}
            <input
              class="ml-3"
              :id="choice.id"
              :value="choice.id"
              name="choice"
              type="checkbox"
              v-model="checkedChoices"
            />
          </p>
        </div>

        <div class="flex flex-col items-center justify-end mt-5">
          <LoadingShape v-if="loading" class="mb-2" />
          <p
            v-else
            class="cursor-pointer group mb-2 p-1 rounded-full hover:bg-primary-500 hover:shadow-md transition ease-out duration-200"
            @click="submitChoices"
          >
            <CheckSvg
              class="h-10 w-10 transition stroke-primary-500 group-hover:stroke-white ease-out duration-200"
            />
          </p>
          <p class="text-xs text-primary-500 mb-1">{{ response.data }}</p>
          <p class="text-xs text-red-500 mb-1" v-if="error.response">{{ Object.values(error.response.data)[0][0] }}</p>
          <p class="text-xs">Choices can't be changed afterwards!</p>
        </div>
        <router-link :to="{ name:'Poll', params: route.id_hashed }" class="btn-primary mb-2 mr-2 mt-5 self-end"><ArrowLeftSvg class="w-4 h-4 inline mr-1"/>Go back</router-link>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter, useRoute, onBeforeRouteUpdate } from "vue-router";
import { useStore } from "vuex";
import { useFetching, useSubmit, makeRequest } from "../../../assets/utils.js";
import NotExist from "../../../components/poll/NotExist.vue"
import LoadingShape from "../../../components/LoadingShape.vue";
import CheckSvg from "../../../components/svgpaths/CheckSvg.vue";
import ArrowLeftSvg from "../../../components/svgpaths/ArrowLeftSvg.vue";
export default {
  components: {
    NotExist,
    LoadingShape,
    CheckSvg,
    ArrowLeftSvg,
  },
  setup() {
    // router and vuex

    const store = useStore();
    store.commit("setCurrentPage", -1);

    const router = useRouter();
    const route = useRoute();

    // form stuff

    const poll = ref({});
    const choices = ref([]);

    const checkedChoices = ref([]);

    // fetching

    const { notFound, fetching, fetchData } = useFetching(
      store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}/`
    );

    onMounted(() => {
      fetchPoll();
    });

    onBeforeRouteUpdate(() => {
      fetchPoll();
    });

    const fetchPoll = () => {
      fetchData().then((res) => {
        poll.value = res.data.poll;
        choices.value = res.data.choices;
        poll.value.owner = res.data.poll_owner;
      });
    };

    // submitting

    const { response, error, loading, submit } = useSubmit(
      store.getters.getBaseUrl + `api/vote/${route.params.id_hashed}/`
    );

    const submitChoices = () => {
      const form = new FormData();
      for (let i = 0; i < checkedChoices.value.length; i++) {
        form.append('votes', checkedChoices.value[i]);
      }

      submit(form);
    };

    return {
      route,

      poll,
      choices,
      checkedChoices,

      // fetch
      fetching,
      notFound,

      // submit
      submitChoices,
      response,
      error,
      loading,
    };
  },
};
</script>

<style>
</style>