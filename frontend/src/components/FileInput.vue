<template>
  <div>
    <div class="relative inline-block">
      <img
        :src="src"
        alt="Avatar"
        class="object-cover w-48 h-48 rounded-full bg-white"
      />
      <div
        class="group absolute top-0 w-48 h-48 rounded-full bg-black bg-opacity-0 hover:bg-opacity-25 flex 
            items-center justify-center transition ease-out duration-100"
        @click="browse"
      >
        <svg
          class="w-10 h-10 cursor-pointer opacity-0 group-hover:opacity-100 transition ease-out duration-200"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
          />
        </svg>
      </div>
    </div>
    <input
      type="file"
      accept="image/*"
      class="hidden"
      ref="file"
      @change="change"
    />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  props: {
    value: {
      type: File,
      default: null,
    },

    defaultSrc: {
      typeSrc: String,
      default: null,
    },
  },

  emits: ["image"],

  setup(props, context) {
    const file = ref(null);
    const src = ref(props.defaultSrc);

    const browse = () => {
      file.value.click();
    };

    const change = (event) => {
      file.value = event.target.files[0];
      
      context.emit("image", file.value);

      let reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]);
      reader.onload = (event) => {
        src.value = event.target.result;
      };
    };

    return {
      file,
      src,
      browse,
      change,
    };
  },
};
</script>

<style>
</style>