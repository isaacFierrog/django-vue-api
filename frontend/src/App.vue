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
          { to: '/modulos', name: 'Modulos' },
          { to: '/usuarios', name: 'Usuarios' }
      ]
    }
  }  
}
</script>

<template>
  <div>
    <Navbar :links="links"/>
    <RouterView />
  </div>
</template>

<style scoped>
  
</style>