<template>
    <div class="container">
        <div class="text-3xl my-3">Dashbord</div>
        <div class="text-700 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis congue risus sed odio commodo, vel posuere tellus consectetur. Curabitur scelerisque metus purus, ut efficitur ipsum fringilla quis. Pellentesque eu ultricies ex. Aenean quis pharetra sem.</div>

        <Divider />

        <div class="flex flex-wrap gap-3 mb-3">
            <AutoComplete v-model="siretFilter" multiple :suggestions="siretList" @complete="search" placeholder="Siret" class="w-full md:w-14rem"  />
            <Button label="Plus de filtres" icon="pi pi-sliders-h" plain text />
        </div>

        <div class="border-1 border-dashed border-primary text-500 w-100 flex align-items-center justify-content-center h-screen">
            <iframe
                v-if="iframeUrl"
                id="metabase_iframe"
                :src="iframeUrl"
                frameborder="0"
                allowtransparency>
            </iframe>
        </div>
    </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const iframeUrl = ref("");

onMounted(() => {
    try {
        axios.post(`http://${window.location.hostname}:8000/dashboard/`, {"dashboard_id": 3, "filters": {}}).then((response) => {
            console.log(response.data);
            iframeUrl.value = response.data.iframe_url;
        });
    } catch (error) {
        console.log(error);
    }
})

const siretFilter = ref();
const siretList = ref([]);
const search = (event) => {
    siretList.value = [...Array(10).keys()].map((item) => event.query + '-' + item);
}

</script>

<style scoped>
#metabase_iframe {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
