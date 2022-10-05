<template>
    <div>
        <h1>Listado de usuarios</h1>
        <button class="boton-crear blanco-a" @click="mostrarFormulario">
            <i class="fa-solid fa-plus"></i>
            Crear usuario
        </button>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <UsuarioForm 
            :mostrarForm="mostrarForm"
            @ocultarFormulario="mostrarFormulario">
        </UsuarioForm>
    </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
export default {
    components: {
        UsuarioForm: defineAsyncComponent(
            () => import('../components/UsuarioForm.vue')
        ),
        Usuario: defineAsyncComponent(
            () => import('../components/UsuarioComponent.vue')
        )
    },
    data() {
        return {
            mostrarForm: true
        }
    },
    methods: {
        mostrarFormulario() {
            this.mostrarForm = !this.mostrarForm;
            console.log(this.mostrarForm);
        }
    }
}
</script>