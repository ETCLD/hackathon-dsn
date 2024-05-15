<template>
    <div class="container">
        <div class="text-3xl my-3">Suivi impact d'une cohorte</div>
        <div class="text-700 text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis congue risus sed odio commodo, vel posuere tellus consectetur. Curabitur scelerisque metus purus, ut efficitur ipsum fringilla quis. Pellentesque eu ultricies ex. Aenean quis pharetra sem.</div>

        <Divider />

        <div class="border-1 border-dashed border-primary text-500 w-100 flex align-items-center justify-content-center h-screen">
            <iframe
                id="metabase_iframe"
                src="http://10.0.0.55:8080/"
                frameborder="0"
                allowtransparency>
            </iframe>
        </div>
    </div>
</template>

<script setup>
</script>

<style scoped>
#metabase_iframe {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
