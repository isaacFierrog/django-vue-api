<template>
    <div>
        <h1>Este es el layout de modulos</h1>
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
                { to: '/modulos/crear', name: 'Crear modulo' },
            ]
        }
    }
}
</script>