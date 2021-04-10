<template>
  <transition name="appear" appear>
    <div class="flex flex-col items-center self-center">
      <h1 class="text-5xl mt-10 font-extralight">User Settings</h1>
      <div class="grid grid-cols-2 mt-20">
        <div class="flex flex-col justify-center items-center">
          <FileInput v-model="file" :default-src="'/static/images/defaultpic.svg'"></FileInput>
          <h2 class="text-3xl mt-2 px-1 border-b border-primary-500">{{ username }}</h2>
        </div>
        <div class="card justify-between w-phone pt-5">
          <div class="flex flex-col items-center w-full" enctype="multipart/form-data" method="post" @submit.prevent="">
            <table>
              <tr>
                <td class="font-bold">Username:</td>
                <td><input class="inpt my-3 ml-2" type="text" placeholder="Username" v-model="username"></td>
              </tr>
              <tr>
                <td class="font-bold">First Name:</td>
                <td><input class="inpt my-3 ml-2" type="text" placeholder="First Name" v-model="firstName"></td>
              </tr>
              <tr>
                <td class="font-bold">Last Name:</td>
                <td><input class="inpt my-3 ml-2" type="text" placeholder="Last Name" v-model="lastName"></td>
              </tr>
              <tr>
                <td class="font-bold">E-Mail:</td>
                <td><input class="inpt my-3 ml-2" type="email" placeholder="E-Mail" v-model="email"></td>
              </tr>
            </table>
            <div class="my-5 px-3 w-full flex justify-between items-center">
              <a class="btn hover:text-primary-500 transition ease-out duration-100"
                :href="$store.getters.getBaseUrl + 'accounts/password/change'">Change Password</a>
              <input class="btn-primary" type="submit" value="Save changes" @click="saveChanges">
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import { ref } from "vue"
  import { useStore } from "vuex"
  import FileInput from "../../../components/FileInput.vue"

  export default {
    components: {
      FileInput,
    },

    setup() {
      const store = useStore();
      store.commit('setCurrentPage', 1);

      const username = ref(store.getters.getUsername);
      const firstName = ref(store.getters.getFirstName);
      const lastName = ref(store.getters.getLastName);
      const email = ref(store.getters.getEmail);
      const file = ref(null);

      const form = new FormData();
      form.append('username', username.value);
      form.append('first_name', firstName.value);
      form.append('last_name', lastName.value);
      form.append('email', email.value);
      form.append('profile_pic', file.value);

      const saveChanges = () => {

      };

      return {
        username,
        firstName,
        lastName,
        email,
        file,
        saveChanges,
      }
    }
  };
</script>

<style>
</style>