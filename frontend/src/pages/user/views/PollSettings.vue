<template>
  <transition v-if="notFound" name="appear" appear>
    <NotExist />
  </transition>
  <transition v-else-if="isOwner" name="appear" appear>
    <div class="flex flex-col items-center">
      <h1 class="justify-center text-5xl font-extralight mb-3 mt-10">
        Poll Settings
      </h1>
      <h2 class="justify-center text-3xl font-bold mb-10 max-w-xl break-words">
        <span v-if="fetching" class="flex">
          <LoadingShape class="mr-4" />
          Loading...
        </span>
        <span v-else>
          {{ poll.title }}
        </span>
      </h2>
      <div v-if="!fetching" class="card p-2 w-phone flex flex-col items-center">
        <div class="mt-4">
          <input
            class="inpt"
            type="text"
            v-model="poll.title"
            maxlength="128"
          />
          <h3 class="font-light text-xs">Poll Title</h3>
        </div>

        <h3 class="mt-6 mb-1 font-light text-sm">Description</h3>
        <textarea
          class="tbox mb-5 focus:outline-none"
          cols="40"
          rows="5"
          maxlength="1024"
          v-model="poll.description"
        ></textarea>

        <LoadingShape v-if="loading" />
        <p class="text-xs text-red-500 mb-5" v-if="error.response">
          {{ Object.values(error.response.data)[0][0] }}
        </p>
        <p v-if="response.data !== ''" class="text-primary-500 text-sm mb-5">
          {{ response.data }}
        </p>
        <button class="btn-primary self-end" @click="submitPoll">
          Save changes
        </button>
      </div>
      <button
        @click="deletePoll"
        class="btn mt-10 border border-red-500 rounded-lg flex items-center hover:shadow-md hover:bg-red-500 transition ease-out duration-200"
      >
        <TrashSvg class="stroke-font-dark w-5 mr-1" />
        Delete poll
      </button>
    </div>
  </transition>
  <transition v-else>
    <div
      class="flex flex-col self-center mt-20 w-desktop col-span-2 border-b pb-2"
    >
      <div class="flex">
        <img class="w-10 mr-2" src="/static/images/cross.svg" alt="Cross" />
        <h1 class="text-5xl font-light">You're not the owner of this poll!</h1>
      </div>
      <h2 class="text-2xl font-light">
        Maybe you shall leave this page alone now.
      </h2>
      <router-link
        class="self-end btn-primary flex items-center mt-2"
        :to="{ name: 'Home' }"
      >
        <ArrowLeftSvg class="h-5 w-5 mr-2" />
        <p>go home</p>
      </router-link>
    </div>
  </transition>
</template>

<script>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import { useRouter, useRoute, onBeforeRouteUpdate } from "vue-router";
import { useFetching, useSubmit, makeRequest } from "../../../assets/utils.js";
import NotExist from "../../../components/poll/NotExist.vue";
import LoadingShape from "../../../components/LoadingShape.vue";
import TrashSvg from "../../../components/svgpaths/TrashSvg.vue";
import ArrowLeftSvg from "../../../components/svgpaths/ArrowLeftSvg.vue";
export default {
  components: {
    NotExist,
    LoadingShape,
    ArrowLeftSvg,
    TrashSvg,
  },
  setup() {
    // router and vuex

    const store = useStore();
    store.commit("setCurrentPage", -1);

    const router = useRouter();
    const route = useRoute();

    // poll stuff

    const poll = ref(null);
    const isOwner = ref(true);

    // submitting stuff

    const { response, error, loading, submit } = useSubmit();

    const submitPoll = () => {
      const form = new FormData();
      form.append("title", poll.value.title);
      form.append("description", poll.value.description);
      submit(
        store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}/`,
        form
      );
    };

    // fetching stuff

    const { notFound, fetching, fetchData } = useFetching();

    onMounted(() => {
      fetchPoll();
    });

    onBeforeRouteUpdate((to, from) => {
      route.params.id_hashed = to.params.id_hashed;
      fetchPoll();
    });

    const fetchPoll = () => {
      fetchData(
        store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}/`
      ).then((res) => {
        isOwner.value = res.data.user_is_owner;
        poll.value = isOwner.value ? res.data.poll : null;
      });
    };

    // delete poll

    const deletePoll = () => {
      if (confirm("Are you sure you want to delete this poll?")) {
        makeRequest(
          "DELETE",
          "",
          store.getters.getBaseUrl + `api/poll/${route.params.id_hashed}`
        ).then((res) => {
          router.push("Home");
        });
      }
    };

    return {
      poll,
      isOwner,

      notFound,
      fetching,
      fetchPoll,

      response,
      error,
      loading,
      submitPoll,

      deletePoll,
    };
  },
};
</script>

<style>
</style>