<template>
    <div class="w-10 h-10">
        <div class="loading-shape w-full h-full rounded-full">

        </div>
    </div>
</template>

<script>
    export default {};
</script>

<style>
    .loading-shape {
        border: 0.15rem #d8fff5 solid;
        border-bottom: 0.15rem #00e1a0 solid;
        animation: spin 1s linear infinite;
    }
</style>