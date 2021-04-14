<template>
  <transition name="appear" appear>
    <div class="flex flex-col items-center self-center">
      <h1 class="text-5xl mt-10 font-extralight">Create Poll</h1>
      <div class="flex items-stretch mt-10 mb-20">
        <div class="flex flex-col">
          <!-- Main information card -->

          <div class="card w-phone pt-5 mb-5">
            <h2 class="text-2xl">Main Information</h2>
            <h3 class="mt-4 mb-1 font-light">Poll name:</h3>
            <input class="inpt" type="text" />
            <h3 class="mt-4 mb-1 font-light">Description:</h3>
            <textarea class="tbox mb-5" cols="40" rows="5"></textarea>
          </div>

          <!-- Additional information card -->

          <div class="card w-phone pt-5">
            <h2 class="text-2xl">Additional Information</h2>
            <h3 class="mt-4 mb-1 font-light">Starting date:</h3>
            <input class="inpt text-primary-500 font-light" type="date" />
            <h3 class="mt-4 mb-1 font-light">Ending date:</h3>
            <input class="inpt text-primary-500 font-light" type="date" />
            <h3 class="mt-4 mb-1 font-light">Votes amt:</h3>
            <input class="inpt" type="number" />
            <table class="my-4">
              <tr>
                <td>
                  <h3 class="mt-4 mb-1 font-light self-start">
                    Less votes allowed?
                  </h3>
                </td>
                <td><input class="ml-2" type="checkbox" /></td>
              </tr>
              <tr>
                <td>
                  <h3 class="mt-1 mb-1 font-light self-start">
                    Show results when poll is running?
                  </h3>
                </td>
                <td><input class="ml-2" type="checkbox" /></td>
              </tr>
            </table>
          </div>
        </div>

         <!-- choices card -->

        <div class="card w-phone pt-5 ml-5">
          <h2 class="text-2xl">Choices</h2>
          <form class="flex my-5" @submit.prevent="addChoice">
            <input
              class="inpt"
              type="text"
              placeholder="New Choice:"
              v-model="choiceInput"
            />
            <input class="btn-primary ml-2" type="submit" value="New Choice" />
          </form>
          <ItemPagination
            :items="choices"
            @pageChanged="retrieveCurrentPage"
            :itemsPerPage="10"
          >
            <template v-slot:default>
              <table class="mt-5">
                <tr>
                  <th class="text-left text-xs">Name</th>
                </tr>
                <tr v-for="choice in currentPage" :key="choice.index">
                  <td class="font-bold">{{ choice.item }}</td>
                  <td>
                    <p
                      class="group cursor-pointer ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                      @click="editChoice(choice.index)"
                    >
                    <PencilSvg class="h-5 w-5 stroke-primary-500"></PencilSvg>
                    </p>
                  </td>
                  <td>
                    <p
                      class="group cursor-pointer ml-4 p-0.5 border border-transparent hover:border-primary-500 hover:shadow transition ease-out duration-200"
                      @click="choices.splice(choice.index, 1)"
                    >
                      <TrashSvg class="h-5 w-5 stroke-primary-500"></TrashSvg>
                    </p>
                  </td>
                </tr>
              </table>
            </template>
            <template v-slot:noItems> Currently no choices. </template>
          </ItemPagination>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref } from "vue"
import { useStore } from "vuex"
import ItemPagination from "../../../components/ItemPagination.vue"
import PencilSvg from "../../../components/svgpaths/PencilSvg.vue"
import TrashSvg from "../../../components/svgpaths/TrashSvg.vue"

export default {
  components: {
    ItemPagination,
    PencilSvg,
    TrashSvg,
  },
  setup() {
    const store = useStore();
    store.commit("setCurrentPage", 2);

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

    return {
      choices,
      retrieveCurrentPage,
      currentPage,
      choiceInput,
      currentItem,
      addChoice,
      editChoice,
    };
  },
};
</script>

<style>
</style>