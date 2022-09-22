<template>
    <div>
        <h1>Listado de modulos</h1>
        <ModuloComponent 
            v-for="(modulo, idx) in modulos"
            :key="idx"
            :modulo="modulo"/>
    </div>
</template>

<script>
    import servicio from '../services/moduloServicio.js';
    import { defineAsyncComponent } from 'vue';
import ModuloComponent1 from '../components/ModuloComponent.vue';
export default {
    created(){
        this.obtenerModulos();    
    },
    data(){
        return {
            modulos: []
        }
    },
    components: {
    ModuloComponent: defineAsyncComponent(() => import("../components/ModuloComponent.vue")),
    ModuloComponent1
},
    methods: {
        async obtenerModulos(){
            try{
                const res = await fetch('http://127.0.0.1:8000/api/modulos/');
                const json = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText }

                console.log(json);
                this.modulos = json;
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.error(`Error ${status}: ${mensaje}`);
            }   
        }
    }
}
</script>