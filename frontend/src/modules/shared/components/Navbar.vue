<template>
    <div>
        
        <CustomLink 
            v-for="link in links"
            :key="link.to"
            :link="link"/>

    </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
export default {
    components: {
        CustomLink: defineAsyncComponent(
            () => import('./CustomLink.vue')
        )
    },
    data(){
        return {
            links: [
                { to: '/modulos', name: 'Modulos' },
                { to: '/usuarios', name: 'Usuarios' }
            ]
        }
    }
}
</script>

<style scoped>
    .router-link-exact-active{
        color: #2e7454;
    }
</style>