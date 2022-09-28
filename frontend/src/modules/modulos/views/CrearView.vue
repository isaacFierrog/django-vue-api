<template>
    <div>
        <h1 class="titulo-vista blanco-a">Crear modulo</h1>
        <form @submit.prevent="guardarModulo">
            <input 
                type="text" 
                placeholder="Mac del modulo"
                v-model="mac">
            <select v-model="mina">
                <option 
                    placeholder="Mina asignada al modulo"
                    v-for="mina_elegida in minas"
                    :key="mina_elegida"
                    :value="mina_elegida">
                    {{ mina_elegida }}
                </option>
            </select>
            <select v-model="area">
                <option
                    v-for="a in areas"
                    :key="a" 
                    :value="a">
                    {{ a }}
                </option>
            </select>
            <input type="submit" value="Guardar">
        </form>
        <button @click="agregarSensor">Agregar sensor</button>
        <template v-if="sensorMayorCero">
            <SensorDetail
                v-for="sensor in sensores"
                :key="sensor.clave"
                :sensor="sensor">
            </SensorDetail>
        </template>
        <pre>{{ $data }}</pre>
        <pre>{{ macMayorCero }}</pre>
        <pre>{{  }}</pre>
    </div>
</template>

<script>
    import { defineAsyncComponent } from 'vue';
export default {
    data() {
        return {
            mac: '',
            mina: '',
            area: '',
            sensores: [],
            minas: ['HERMOSILLO', 'CANANEA', 'ROCAPIEDRA'],
            areas: ['A', 'B', 'C', 'D'],
            numSensor: 0
        }
    }, 
    methods: {
        reiniciarValores() {
            this.mac = '';
            this.mina = '';
            this.area = '';
            this.numSensor = 0;
        },  
        agregarSensor() {
            if(!this.macMayorCero) return;
            if(this.numSensor < 8) {
                this.sensores.push({
                    clave: `${this.mac}-${++this.numSensor}`
                })
            }

            console.log(this.numSensor);
            
        },
        async guardarModulo() {
            try{
                if(!(this.macMayorCero && this.minaMayorCero && this.areaMayorCero)) return;
                console.log('Si llenaste todos los campos')
                const url = 'http://127.0.0.1:8000/api/modulos/';
                const modulo = {
                    mac: this.mac,
                    mina: this.mina,
                    area: this.area,
                    sensores: this.sensores
                }

                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json; charset=utf-8',
                    },
                    body: JSON.stringify(modulo)
                });
                const json = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                console.log(json);
                this.reiniciarValores();
                this.$router.push({ name: 'modulos-listar' })
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(`Error ${status}: ${mensaje}`);
            }
        }
    },
    components: {
        SensorDetail: defineAsyncComponent(
            () => import('../components/SensorFormComponent.vue')
        )
    },
    computed: {
        sensorMayorCero() {
            return this.sensores.length > 0;
        },
        minaMayorCero() {
            return !!this.mina;
        },
        macMayorCero() {
            return !!this.mac;
        },
        areaMayorCero() {
            return !!this.area;
        }
    }
}
</script>