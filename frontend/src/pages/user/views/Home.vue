<template>
  <transition name="appear" appear>
    <div class="grid grid-cols-2 gap-5 w-desktop self-center">
      <user-data />
      <polls-voted />
      <polls-created />
    </div>
  </transition>
</template>

<script>
import UserData from "../../../components/user/UserData.vue";
import PollsVoted from "../../../components/user/PollsVoted.vue";
import PollsCreated from "../../../components/user/PollsCreated.vue";

import { ref } from "vue";

export default {
  components: {
    UserData,
    PollsVoted,
    PollsCreated,
  },

  setup() {
    const appear = ref(true);

    return {
      appear,
    };
  },
};
</script>

<style>
</style>