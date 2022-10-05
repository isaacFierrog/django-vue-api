<script>
import { RouterView } from 'vue-router'
import { defineAsyncComponent } from 'vue'

export default {
  components: {
    Navbar: defineAsyncComponent(
      () => import('./modules/shared/components/Navbar.vue')
    )
  },
  data() {
    return {
      links: [
          { to: '/usuarios', name: 'Usuarios' }
      ]
    }
  },
  mounted() {
    console.log('Aplicacion iniciada');
  }
}
</script>

<template>
  <div class="container">
    <Navbar :links="links"/>
    <RouterView />
  </div>
</template>

<style scoped>
  
</style>