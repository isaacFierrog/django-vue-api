<template>
    <div>
        <h1>Detalles del Modulo {{ $route.params.moduloId }}</h1>
        <Sensor 
            v-for="sensor in sensores"
            :key="sensor.id"
            :sensor="sensor">
        </Sensor>
    </div>
</template>

<script>
    import { defineAsyncComponent } from 'vue';
export default {
    created(){
        this.obtenerDatos();
        this.consultarDatos();    
    },
    beforeUnmount(){
        console.log('ADIOS');
        clearInterval(this.referenciaDatos);
        this.referenciaDatos = null;
    },
    data() {
        return {
            referenciaDatos: null,
            sensores: null,
            mac: null,
            mina: null,
            area: null
        }
    },
    methods: {
        async obtenerDatos() {
            try{
                const { moduloId } = this.$route.params;
                const url = `http://127.0.0.1:8000/api/modulos/${moduloId}`;
                const res = await fetch(url);
                const json = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                const { sensores, mac, mina, area } = json;
                this.sensores = sensores;
                this.mac = mac;
                this.mina = mina;
                this.area = area;
            }catch(err){
                console.log(err);
            }   
        },
        consultarDatos() {
            console.log('Consultando datos');
            this.referenciaDatos = setInterval(() => {
                console.log('Datos consultados');
                this.obtenerDatos();
            }, 5000);
        }
    },
    components: {
        Sensor: defineAsyncComponent(
            () => import('../components/SensorComponent.vue')
        )
    }
}
</script>