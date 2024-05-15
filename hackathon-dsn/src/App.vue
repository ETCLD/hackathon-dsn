<template>
    <Menu @menu-changed="onMenuChanged"/>

    <component :is="currentView" />
</template>

<script setup>
import { ref } from "vue";

import Menu from './components/Menu.vue'
import Metabase from './components/Metabase.vue'
import Cohorte from './components/Cohorte.vue'

const urlMap = {
    "dashbord_0": Metabase,
    "cohorte": Cohorte
}

const currentView = ref(Metabase);
function onMenuChanged(menu) {
    currentView.value = urlMap[menu]
};

</script>
