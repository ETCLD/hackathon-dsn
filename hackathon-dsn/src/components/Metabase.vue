<template>
    <div>
        Metabase
    </div>
</template>
<script>
import axios from "axios";
export default {
    data() {
        return {
        };
    },

    methods: {},
    computed: {},
    mounted() {
        try {
            axios.post("http://localhost:8000/dashboard/", {"year": null, "departement": null, "siren": null})
                .then((response) => {
                    console.log(response.data);
                });
        } catch (error) {
            console.log(error);
        }
    }
};
</script>

<style scoped></style>