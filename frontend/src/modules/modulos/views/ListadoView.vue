<template>
    <div>
        <h1>Listado de modulos</h1>
        <button class="boton-crear blanco-a" @click="mostrarFormulario">
            <i class="fa-solid fa-plus"></i>
            Crear modulo
        </button>
        <ModuloForm
            :mostrarForm="mostrarForm"
            @ocultarFormulario="mostrarFormulario">
        </ModuloForm>
        <section class="modulos">
            <Modulo></Modulo>
        </section>
    </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
export default {
    components: {
        ModuloForm: defineAsyncComponent(
            () => import('../components/ModuloForm.vue')
        ),
        Modulo: defineAsyncComponent(
            () => import('../components/ModuloComponent.vue')
        )
    },
    created() {
        this.mosModulos();
    },
    data() {
        return {
            modulos: [],
            mostrarForm: true
        }
    },
    methods: {
        async mosModulos() {
            try{
                const url = 'http://127.0.0.1:8000/api/modulos/';
                const res = await fetch(url);
                const data = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                this.modulos = data;
                console.log(this.usuarios);
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(mensaje);
            }
        },
        mostrarFormulario() {
            this.mostrarForm = !this.mostrarForm;
        }
    }
}
</script>
    
<style scoped>
    .modulos{
        display: flex;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
</style>