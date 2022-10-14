<template>
    <div class="layout-modulo-form" :class="ocultarForm">
        <button class="txt-upper blanco-a titulo-modulo boton-cerrar" @click="ocultarFormulario">x</button>
        <h2 class="txt-upper blanco-a titulo-modulo">Crear modulo</h2>
        <form class="form" @submit.prevent="crearModulo">
            <p class="blanco-a form__label">Mac</p>
            <input type="text" class="form__input" v-model="mac">
            <p class="blanco-a form__label">Mina</p>
            <select class="form__input" v-model="mina">
                <option
                    v-for="(m, index) in minas"
                    :key="m"
                    :value="m">
                    {{ etiquetasMinas[index] }}
                </option>
            </select>
            <p class="blanco-a form__label">Zona</p>
            <select class="form__input" v-model="zona">
                <option 
                    v-for="(z, index) in zonas"
                    :key="z"
                    :value="z">
                    {{ etiquetasZonas[index] }}
                </option>
            </select>
            <!-- <button class="boton-crear boton-usuario blanco-a txt-upper">
                Guardar 
                <i class="fa-solid fa-user"></i>
            </button> -->
            <section class="sensores">
                <button class="sensores__boton blanco-a" @click="eliminarSensores">-</button>
                <p>Sensores: {{ numSensores }}</p>
                <button class="sensores__boton blanco-a" @click="agregarSensores">+</button>
            </section>
            <input type="submit" class="boton-crear boton-modulo blanco-a txt-upper" value="Guardar">
        </form>
    </div>
</template>

<script>
    export default {
        props: {
            mostrarForm: {
                type: Boolean
            }
        },
        data() {
            return {
                mac: '',
                mina: '',
                zona: '',
                ocultar: true,
                numSensores: 0,
                maxSensores: 8,
                minas: [1, 2],
                zonas: [1,2,3,4],
                etiquetasMinas: ['HERMOSILLO', 'CANANEA'],
                etiquetasZonas: ['A', 'B', 'C', 'D']
            }
        },
        methods: {
            agregarSensores(){
                if(this.numSensores >= this.maxSensores) return;
                this.numSensores++;
            },
            eliminarSensores(){
                this.numSensores--;
            },
            async crearModulo() {
                try{
                    const url = 'http://127.0.0.1:8000/api/modulos/';
                    const res = await fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json; charset=utf-8'
                        },
                        body: JSON.stringify({
                            mac: this.mac,
                            mina: this.mina,
                            zona: this.zona
                        })
                    });
                    const data = await res.json();
                    const { status, statusText } = res;
    
                    if(!res.ok) throw { status, statusText };
    
                    console.log(data);
                }catch({ status, statusText }){
                    const mensaje = statusText || 'Ocurrio un error';
                    console.log(`Error ${status}: ${mensaje}`);
                }
            },  
            ocultarFormulario() {
                this.$emit('ocultarFormulario');
            },
            reiniciarCampos() {
                this.correo = '';
                this.nombre = '';
                this.apellido = '';
                this.password = '';
                this.mina = '';
                this.zona = '';
            }
        },
        computed: {
            ocultarForm() {
                return { 'ocultar-layout': this.mostrarForm }
            }
        }
    }
    </script>

<style scoped> 
    .layout-modulo-form{
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100vh;
        background-color: rgba(17, 16, 16, 0.8);
        transition: all .8s ease-in-out;
    }
    .titulo-modulo{
        margin-bottom: 1rem;
    }
    .boton-modulo{
        margin-top: 1.8rem;
    }
    .ocultar-layout{
        transform: translateY(-100vh);
        visibility: hidden;        
    }
    .sensores{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .sensores__boton{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 4rem;
        height: 4rem;
        font-size: 2rem;
        font-weight: bold;
        border: none;
        border-radius: 50%;
        background-color: rgb(57, 55, 70);
        transition: all .3s ease-in-out;
    }
    .sensores__boton:hover{
        cursor: pointer;
        background-color: rgb(69, 66, 92);
    }
</style>