<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <div class="flex items-center justify-center transition ease-out duration-500 transform hover:scale-110">
      <img src="/static/images/poll.svg" class="w-32">
      <h1 class="text-9xl font-extralight ml-2">Pollapp</h1>
    </div>
    <div class="flex mt-10">
      <a class="btn btn-primary" href="/accounts/login/">Login</a>
      <a class="btn btn-primary" href="/accounts/signup/">Sign Up</a>
    </div>
    <a class="flex flex-col items-center mt-10 transition ease-out duration-500 transform hover:scale-110"
      href="https://github.com/dev-andreas/pollapp">
      <img src="/static/images/github_dark.svg" class="w-14">
      <p class="text-sm">View source code &raquo;</p>
    </a>
  </div>
</template>

<script>
  export default {

  };
</script>

<style>
</style>