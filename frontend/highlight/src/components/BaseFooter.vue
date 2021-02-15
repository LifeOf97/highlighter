<template>
<!-- eslint-disable max-len -->
    <!-- start of footer -->
    <footer v-bind="$attrs" class="flex flex-col mt-10 sm:mt-0 sm:flex-row justify-between items-center w-11/12 mx-auto">
      <div class="text-xs">
        <span class="font-semibold text-gray-500">JustHighlight</span>
        <i class="fas fa-copyright text-gray-800 dark:text-gray-600 ml-2 mr-1"></i>
        <span class="font-semibold text-gray-400">{{year}}</span>
        <span class="font-medium text-coolGray-400 ml-3">All Rights Reserved</span>
      </div>
      <div>
        <span class="text-xs text-gray-500 font-semibold">Aces & Coup inc.</span>
      </div>
    </footer>
    <!-- end of footer -->
</template>

<script>
export default {
  name: 'BaseFooter',
  inheritAttrs: false,
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
};
</script>
