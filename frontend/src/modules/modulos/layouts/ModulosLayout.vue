<template>
    <div class="container">
        <Navbar :links="links"/>
        <router-view></router-view>
    </div>
</template>

<script>
    import { defineAsyncComponent } from 'vue';
export default {
    components: {
        Navbar: defineAsyncComponent(
            () => import('../../shared/components/Navbar.vue')
        )
    },
    data() {
        return {
            links: [
                { to: '/modulos/', name: 'Modulos' }
            ]
        }
    }
}
</script>