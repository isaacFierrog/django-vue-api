<template>
    <div>
        <h1>Listado de usuarios</h1>
        <button class="boton-crear blanco-a" @click="mostrarFormulario">
            <i class="fa-solid fa-plus"></i>
            Crear usuario
        </button>
        <!-- <Usuario
            v-for="usuario in usuarios"
            :usuario="usuario" 
            @editarUsuario="editarUsuario">
        </Usuario> -->
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
        <Usuario></Usuario>
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
    created() {
        this.mostrarUsuarios();
    },
    data() {
        return {
            usuarios: [],
            mostrarForm: true,
            usuarioEditar: null
        }
    },
    methods: {
        async mostrarUsuarios() {
            try{
                const url = 'http://127.0.0.1:8000/api/usuarios/';
                const res = await fetch(url);
                const data = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                this.usuarios = data;
                console.log(this.usuarios);
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(mensaje);
            }
        },
        mostrarFormulario() {
            this.mostrarForm = !this.mostrarForm;
        },
        editarUsuario(usuario){
            // this.usuarioEditar = usuario;
            this.usuarioEditar = usuario;
            this.mostrarFormulario();
        }
    }
}
</script>