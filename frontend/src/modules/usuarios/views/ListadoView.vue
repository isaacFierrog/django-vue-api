<template>
    <div>
        <h1>Listado de usuarios</h1>
        <button class="boton-crear blanco-a" @click="mostrarFormulario">
            <i class="fa-solid fa-plus"></i>
            Crear usuario
        </button>
        <Usuario @editarUsuario="editarUsuario"></Usuario>
        <UsuarioForm 
            :mostrarForm="mostrarForm"
            :usuario="usuarioEditar"
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
            mostrarForm: true,
            usuarioEditar: null
        }
    },
    methods: {
        mostrarFormulario() {
            this.mostrarForm = !this.mostrarForm;
        },
        editarUsuario(usuario){
            // this.usuarioEditar = usuario;
            console.log('Vamos a editar al usuario');
            this.mostrarFormulario();
        }
    }
}
</script>