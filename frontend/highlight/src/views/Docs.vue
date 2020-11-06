<template>
<!-- eslint-disable max-len -->
    <div class="fixed top-0 left-0 w-full flex">
        <div class="h-screen pt-16 overflow-y-auto hidden md:block md:w-1/3">
            <docs-nav />
        </div>
        <div class="h-screen w-screen flex pt-16 overflow-y-auto">
            <div class="flex-1 py-12">
                <docs-detail />
            </div>
            <div class="sticky top-0 hidden xl:flex justify-center items-center xl:w-1/3 border">
                <p>aLDSKFJ SDJ</p>
            </div>
        </div>
    </div>
</template>

<script>
import DocsNav from './DocsNav.vue';
import DocsDetail from './DocsDetail.vue';

export default {
  name: 'Docs',
  components: { DocsNav, DocsDetail },
};
</script>
