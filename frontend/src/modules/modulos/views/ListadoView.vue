<template>
    <div>
        <h1 class="titulo-vista blanco-a">Listado de modulos</h1>
        <section class="modulo-listado">
            <Modulo v-for="modulo in modulos"
                :key="modulo.mac"
                :modulo="modulo"
                @click="verDetalles(modulo.id)">
            </Modulo>
        </section>
    </div>
</template>

<script>
    import { defineAsyncComponent } from 'vue';
export default {
    created() {
        this.obtenerModulos();
    },
    data() {
        return {
            modulos: []
        }
    },
    components: {
        Modulo: defineAsyncComponent(
            () => import('../components/ModuloComponent.vue')
        )
    },
    methods: {
        verDetalles(moduloId){
            this.$router.push({
                name: 'modulos-detalles',
                params: {
                    moduloId
                }
            })
        },  
        async obtenerModulos() {
            const url = 'http://127.0.0.1:8000/api/modulos/';

            try{
                const res = await fetch(url);
                const json = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                console.log(json);
                this.modulos = json;
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(`Error ${status}: ${mensaje}`);
            }
        }
    }
}
</script>