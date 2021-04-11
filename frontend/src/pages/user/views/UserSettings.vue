<template>
  <transition name="appear" appear>
    <div class="flex flex-col items-center self-center">
      <h1 class="text-5xl mt-10 font-extralight">User Settings</h1>
      <div class="grid grid-cols-2 mt-20">
        <div class="flex flex-col justify-center items-center">
          <FileInput class="w-48"
            v-model="file"
            :default-src="'/static/images/defaultpic.svg'"
          ></FileInput>
          <h2 class="text-3xl border-b p-1 mt-3">Profile picture</h2>
        </div>
        <div class="card justify-between w-phone pt-5">
          <div
            class="flex flex-col items-center w-full"
            enctype="multipart/form-data"
            method="post"
            @submit.prevent=""
          >
            <table>
              <tr>
                <td class="font-bold">Username:</td>
                <td>
                  <input
                    class="inpt my-3 ml-2"
                    type="text"
                    placeholder="Username"
                    v-model="username"
                  />
                </td>
              </tr>
              <tr>
                <td class="font-bold">First Name:</td>
                <td>
                  <input
                    class="inpt my-3 ml-2"
                    type="text"
                    placeholder="First Name"
                    v-model="firstName"
                  />
                </td>
              </tr>
              <tr>
                <td class="font-bold">Last Name:</td>
                <td>
                  <input
                    class="inpt my-3 ml-2"
                    type="text"
                    placeholder="Last Name"
                    v-model="lastName"
                  />
                </td>
              </tr>
              <tr>
                <td class="font-bold">E-Mail:</td>
                <td>
                  <input
                    class="inpt my-3 ml-2"
                    type="email"
                    placeholder="E-Mail"
                    v-model="email"
                  />
                </td>
              </tr>
            </table>
            <LoadingShape v-if="showIndicator" class="my-2" />
            <p v-if="messages !== ''" class="text-primary-500 text-sm my-2">{{ messages }}</p>
            <p v-if="errors !== ''" class="text-red-500 text-sm my-2">{{ errors }}</p>
            <div class="my-5 px-3 w-full flex justify-between items-center">
              <a
                class="btn hover:text-primary-500 transition ease-out duration-100"
                :href="$store.getters.getBaseUrl + 'accounts/password/change'"
                >Change Password</a
              >
              <input
                class="btn-primary"
                type="submit"
                value="Save changes"
                @click="saveChanges"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import FileInput from "../../../components/FileInput.vue";
import LoadingShape from "../../../components/LoadingShape.vue";

export default {
  components: {
    FileInput,
    LoadingShape,
  },

  setup() {
    const store = useStore();
    store.commit("setCurrentPage", 1);

    // form
    const username = ref(store.getters.getUser.username);
    const firstName = ref(store.getters.getUser.first_name);
    const lastName = ref(store.getters.getUser.last_name);
    const email = ref(store.getters.getUser.email);
    const file = ref(null);

    // indicator
    const showIndicator = ref(false);
    const messages = ref('');
    const errors = ref('');

    const saveChanges = () => {
      showIndicator.value = true;
      messages.value = '';
      errors.value = ''

      store.commit("setUsername", username.value);
      store.commit("setFirstName", firstName.value);
      store.commit("setLastName", lastName.value);
      store.commit("setEmail", email.value);
      store
        .dispatch("saveUserData")
        .then((res) => {
          console.log(res);
          messages.value = 'Data successfully changed!';
          showIndicator.value = false;
        })
        .catch((err) => {
          errors.value = Object.values(err.response.data)[0][0];
          showIndicator.value = false;
        });
    };

    return {
      username,
      firstName,
      lastName,
      email,
      file,
      saveChanges,

      showIndicator,
      messages,
      errors,
    };
  },
};
</script>

<style>
</style>