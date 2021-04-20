<template>
  <transition name="appear" appear>
    <div class="flex flex-col items-center self-center">
      <h1 class="text-5xl mt-10 font-extralight">Create Poll</h1>
      <div class="flex items-stretch mt-10 mb-20">
        <div class="flex flex-col">
          
          <!-- Main information card -->

          <div class="card w-phone pt-5 mb-5">
            <h2 class="text-2xl">Main Information</h2>
            <div class="mt-4">
              <input class="inpt" type="text" maxlength="128" v-model="name" />
              <h3 class="font-light text-xs">Poll name</h3>
            </div>
            <h3 class="mt-4 mb-1 font-light">Description:</h3>
            <textarea class="tbox mb-5 focus:outline-none" cols="40" rows="5" maxlength="1024"
              v-model="desc"></textarea>
          </div>

          <!-- Additional information card -->

          <div class="card w-phone pt-5">
            <h2 class="text-2xl">Additional Information</h2>
            <div class="mt-4">
              <input class="inpt font-mono text-sm" type="datetime-local" v-model="startingDate" />
              <h3 class="font-light text-xs">Starting date</h3>
            </div>
            <div class="mt-4">
              <input class="inpt font-mono text-sm" type="datetime-local" v-model="endingDate" />
              <h3 class="font-light text-xs">Ending date</h3>
            </div>
            <div class="mt-4">
              <input class="inpt" type="number" v-model="votesAmt" />
              <h3 class="font-light text-xs">Votes amount per user</h3>
            </div>
            <table class="my-6">
              <tr>
                <td>
                  <h3 class="mb-1 font-light self-start">
                    Less votes allowed?
                  </h3>
                </td>
                <td>
                  <input class="ml-2" type="checkbox" v-model="lessAllowed" />
                </td>
              </tr>
              <tr>
                <td>
                  <h3 class="mt-1 font-light self-start">
                    Show results when poll is running?
                  </h3>
                </td>
                <td>
                  <input class="ml-2" type="checkbox" v-model="showWhileRunning" />
                </td>
              </tr>
            </table>
          </div>
        </div>

        <!-- choices card -->

        <div class="card w-phone pt-5 ml-5 justify-between">
          <div class="flex flex-col justify-center items-center">
            <h2 class="text-2xl">Choices</h2>
            <form class="flex my-5" @submit.prevent="addChoice">
              <input class="inpt" type="text" placeholder="New Choice:" v-model="choiceInput" />
              <input class="btn-primary ml-2" type="submit" value="New Choice" />
            </form>
            <ItemPagination class="self-start" :items="choices" @pageChanged="retrieveCurrentPage" :itemsPerPage="10">
              <template v-slot:default>
                <table class="mt-5 mx-3">
                  <tr>
                    <th class="text-left text-xs">Name</th>
                  </tr>
                  <tr v-for="choice in currentPage" :key="choice.index">
                    <td class="font-bold break-all">{{ choice.item }}</td>
                    <td>
                      <p class="group cursor-pointer ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                        @click="editChoice(choice.index)">
                        <PencilSvg class="h-5 w-5 stroke-primary-500"></PencilSvg>
                      </p>
                    </td>
                    <td>
                      <p class="group cursor-pointer ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                        @click="choices.splice(choice.index, 1)">
                        <TrashSvg class="h-5 w-5 stroke-primary-500"></TrashSvg>
                      </p>
                    </td>
                  </tr>
                </table>
              </template>
              <template v-slot:noItems> Currently no choices. </template>
            </ItemPagination>
          </div>
          <div class="flex flex-col justify-center items-center w-full">
            <LoadingShape v-if="showIndicator"></LoadingShape>
            <p v-if="errors !== ''" class="text-red-500 text-sm my-2">{{ errors }}</p>
            <button class="btn-primary self-end m-2" @click="onSubmit">
              Create Poll
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import { ref, watch } from "vue";
  import { useRouter, useRoute } from "vue-router"
  import { useStore } from "vuex";
  import moment from "moment";
  import { makeRequest } from "../../../assets/utils.js";
  import LoadingShape from '../../../components/LoadingShape.vue'
  import ItemPagination from "../../../components/ItemPagination.vue";
  import PencilSvg from "../../../components/svgpaths/PencilSvg.vue";
  import TrashSvg from "../../../components/svgpaths/TrashSvg.vue";

  export default {
    components: {
      ItemPagination,
      PencilSvg,
      TrashSvg,
      LoadingShape,
    },
    setup() {
      const store = useStore();
      store.commit("setCurrentPage", 2);

      const route = useRoute();
      const router = useRouter();

      // fields
      const name = ref("");
      const desc = ref("");
      const startingDate = ref("");
      const endingDate = ref("");
      const votesAmt = ref(1);
      const lessAllowed = ref(false);
      const showWhileRunning = ref(false);

      watch(votesAmt, (after, before) => {
        if (after < 1) {
          votesAmt.value = 1;
        }
      });

      // choices
      const choices = ref([]);
      const currentPage = ref([]);

      const choiceInput = ref("");
      const currentItem = ref(null);

      const retrieveCurrentPage = (items) => {
        currentPage.value = items;
      };

      const addChoice = () => {
        if (currentItem.value === null) {
          if (choiceInput.value !== "") {
            choices.value.push(choiceInput.value);
          }
        } else {
          choices.value[currentItem.value] = choiceInput.value;
          currentItem.value = null;
        }
        choiceInput.value = "";
      };

      const editChoice = (index) => {
        currentItem.value = index;
        choiceInput.value = choices.value[index];
      };


      // form

      const showIndicator = ref(false);
      const errors = ref('');

      const onSubmit = () => {
        showIndicator.value = true;
        errors.value = ''

        const form = new FormData();
        form.append("title", name.value);
        form.append("description", desc.value);
        form.append("votes_amt", votesAmt.value);
        form.append("less_allowed", lessAllowed.value);
        form.append("show_while_running", showWhileRunning.value);
        form.append("date_to_start", moment(startingDate.value).toISOString());
        form.append("date_to_end", moment(endingDate.value).toISOString());
        for (var i = 0; i < choices.value.length; i++) {
          form.append("choices", choices.value[i]);
        }

        makeRequest("POST", form, store.getters.getBaseUrl + "api/create_poll/")
          .then((res) => {
            router.push({name: 'Home'})
            showIndicator.value = false;
          })
          .catch((err) => {
            errors.value = Object.values(err.response.data)[0][0];
            showIndicator.value = false;
          });
      };

      return {
        choices,
        retrieveCurrentPage,
        currentPage,
        choiceInput,
        currentItem,
        addChoice,
        editChoice,

        name,
        desc,
        startingDate,
        endingDate,
        votesAmt,
        lessAllowed,
        showWhileRunning,

        showIndicator,
        errors,
        onSubmit,
      };
    },
  };
</script>

<style>
</style>