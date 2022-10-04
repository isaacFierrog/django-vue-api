<template>
    <article class="layout-form layout-form--oculto">
        <form class="modulo-form">
            <button 
                @click="agregarSensor"
                class="">
                Agregar sensor
            </button>
            <p class="modulo-form__label blanco-a">MAC</p>
            <input 
                type="text" 
                v-model="mac"
                class="modulo-form__input blanco-b">
            <p class="modulo-form__label blanco-a">MINA</p>
            <select v-model="mina" class="modulo-form__input blanco-b">
                <option 
                    v-for="m in minas"
                    :key="m"
                    :value="m">
                    {{ m }}
                </option>
            </select>
            <p class="modulo-form__label blanco-a">AREA</p>
            <select v-model="area" class="modulo-form__input blanco-b">
                <option
                    v-for="a in areas"
                    :key="a"
                    :value="a">
                    {{ a }}
                </option>
            </select>
            <input 
                type="submit" 
                value="Crear modulo"
                class="modulo-form__submit">
        </form>
        <template v-if="sensorMayorCero">
            <SensorDetail
                v-for="sensor in sensores"
                :key="sensor.clave"
                :sensor="sensor">
            </SensorDetail>
        </template>
    </article>
</template>

<script>
export default {
    data() {
        return {
            mac: '',
            mina: '',
            area: '',
            minas: [
                'HERMOSILLO',
                'CANANEA',
                'ROCAPIEDRA'
            ],
            areas: ['A', 'B', 'C', 'D'],
            
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

                this.reiniciarValores();
                this.$router.push({ name: 'modulos-listar' })
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(`Error ${status}: ${mensaje}`);
            }
        }
    }
}
</script>

<style scoped>
    .layout-form--oculto{
        transform: translateY(-100%);
    }
    .layout-form{
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
        width: 100%;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(29, 29, 29, 0.5);
        transition: all .3s ease-in-out;
    }
    .modulo-form{
        display: flex;
        flex-direction: column;
        width: 40%;
        padding: 3rem;
        background-color: rgb(34, 41, 65);
        border: none;
        border-radius: 1rem;
    }
    .modulo-form__input{
        margin-bottom: 1rem;
        padding: 1rem;
        background-color: rgba(29, 29, 29, 0.5);
        border: .1rem solid white;
        border-radius: .6rem;
        font-weight: bold;
    }
    .modulo-form__submit{
        padding: 1rem;
        background-color: blueviolet;
        border: none;
        border-radius: 1rem;
    }
    .modulo-form__label{
        margin-bottom: .2rem;
        font-weight: bold;
    }
</style>