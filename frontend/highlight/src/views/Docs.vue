<template>
<!-- eslint-disable max-len -->
    <div class="fixed top-0 left-0 w-full flex">
        <!-- start of doc left side nav -->
        <!-- this side nav is hidden on small screens, visible on medium screens and up -->
        <div class="h-screen pt-16 overflow-y-auto hidden md:block md:w-1/3">
            <docs-left-nav />
        </div>
        <!-- end of doc left side nav -->
        <!-- start of docs detail -->
        <!-- this detail div takes the full width of the screen on small devices -->
        <div class="h-screen w-full md:w-2/3 pt-24 overflow-y-auto dark:bg-blueGray-800"  style="scroll-behavior: smooth">
            <docs-detail />
        </div>
        <!-- end of docs detail -->
        <!-- start of right side nav -->
        <!-- this div is hidden on small screens, visible on large screens -->
        <div class="sticky top-0 xl:flex justify-center items-center hidden lg:w-1/3 dark:bg-coolGray-900">
        </div>
        <!-- end of right side nav -->
    </div>
</template>

<script>
import DocsLeftNav from './DocsLeftNav.vue';
import DocsDetail from './DocsDetail.vue';

export default {
  name: 'Docs',
  components: { DocsLeftNav, DocsDetail },
};
</script>
