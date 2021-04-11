<template>
  <div class="flex flex-col justify-center items-center border-b pb-2 col-span-2">
    <h1 class="mt-10 text-6xl font-extralight">
      Hello,
      <span v-if="$store.getters.getUser.first_name !== ''">
        {{ $store.getters.getUser.first_name }}
      </span>
      <span v-else> {{ $store.getters.getUser.username }} </span>!
    </h1>
    <table class="text-sm mt-4">
      <tr>
        <td class="font-bold">Username:</td>
        <td>
          <p class="ml-3">{{ $store.getters.getUser.username }}</p>
        </td>
      </tr>
      <tr>
        <td class="font-bold">E-Mail:</td>
        <td>
          <p class="ml-3">{{ $store.getters.getUser.email }}</p>
        </td>
      </tr>
      <td class="font-bold">Joined:</td>
      <td>
        <p class="ml-3">{{ $store.getters.getUser.date_joined }}</p>
      </td>
    </table>
    <router-link
      :to="{ name: 'UserSettings' }"
      class="group self-end mr-2 p-2 rounded-full hover:bg-primary-500 hover:shadow-md transition ease-out duration-200"
    >
      <svg
        class="h-6 w-6 transition stroke-primary-500 group-hover:stroke-white ease-out duration-200"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
        />
      </svg>
    </router-link>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>