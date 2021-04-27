<template>
  <div>
    <p v-if="items.length > itemsPerPage" class="flex justify-center items-center font-light">
      Page
      <button @click="decPage">
        <svg
          :class="[
            currentPage === 0 ? 'stroke-font-dark' : 'stroke-primary-500',
          ]"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 19l-7-7 7-7"
          />
        </svg></button
      >{{ currentPage + 1 }}
      <button @click="incPage">
        <svg
          :class="[
            currentPage === pagesAmt - 1
              ? 'stroke-font-dark'
              : 'stroke-primary-500',
          ]"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5l7 7-7 7"
          />
        </svg></button
      >from {{ pagesAmt }}.
    </p>
    <div class="mt-2">
      <slot v-if="items.length !== 0"> </slot>
      <slot v-else name="noItems">No items.</slot>
    </div>
  </div>
</template>

<script>
import { ref, watch, computed, toRefs, onBeforeMount } from "vue";
export default {
  props: {
    items: {
      type: Array,
      default: [""],
    },
    itemsPerPage: {
      type: Number,
      default: 5,
    },
  },

  emits: ["pageChanged"],

  setup(props, context) {
    const { items, itemsPerPage } = toRefs(props);
    const currentPage = ref(null);
    onBeforeMount(() => {
      currentPage.value = 0;
    });

    // set current page to 0 before mounted so that watch property gets triggered
    const pagesAmt = computed(() => {
      return parseInt(items.value.length / itemsPerPage.value) + 1;
    });

    // emit current page (in reversed order)
    const getCurrentPage = computed(() => {
      const firstItem = Math.max(
        0,
        items.value.length - (currentPage.value + 1) * itemsPerPage.value
      );
      const lastItem = Math.min(
        items.value.length,
        items.value.length - currentPage.value * itemsPerPage.value
      );

      const page = items.value.slice(firstItem, lastItem);

      // return reversed current page items zipped with the corresponding index...
      return page
        .map((item, index) => {
          return { item: item, index: firstItem + index };
        })
        .reverse();
    });

    // emit when list or page changed
    watch(getCurrentPage, () => {
      context.emit("pageChanged", getCurrentPage.value);
    });

    // functions
    const incPage = () => {
      if (currentPage.value < pagesAmt.value - 1) {
        currentPage.value++;
      }
    };

    const decPage = () => {
      if (currentPage.value > 0) {
        currentPage.value--;
      }
    };

    return {
      items,
      itemsPerPage,
      currentPage,
      pagesAmt,
      incPage,
      decPage,
    };
  },
};
</script>

<style scoped>
button:focus {
  outline: none;
}
</style>