<template>
    <div class="container">
        <Toolbar class="border-0">
            <template #start>
                <img src="/logo_moche.svg" alt="Logo APRES">
                <div class="ml-4">
                    <div class="font-bold">Aide au Pilotage pour le Reseau Emploi sur le Suivi de parcours</div>
                    <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis congue risus sed odio commodo</div>
                </div>
            </template>


            <template #end>
                <Button plain text>
                    <div class="flex flex-columns text-left align-items-center">
                        <i class="pi pi-user font-medium mr-2"></i>
                        <div>
                            <div class="font-medium">Sylvie Durand</div>
                            <div class="text-sm">Poste au département Ain</div>
                        </div>
                    </div>
                </Button>
            </template>
        </Toolbar>
    </div>
    <div class="menu">
        <div class="container">
            <TabMenu :model="items" />
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";

const items = ref([
    { label: 'Fonctionnalité 1', icon: 'pi pi-chart-bar' },
    { label: 'Fonctionnalité 2 future', icon: 'pi pi-building' },
    { label: 'Fonctionnalité 3 future', icon: 'pi pi-map' },
]);
</script>

<style scoped>
.menu {
    background-color: var(--highlight-bg);
}
.menu :deep(.p-tabmenu-nav), .menu :deep(.p-menuitem-link) {
    background: transparent;
}
</style>
