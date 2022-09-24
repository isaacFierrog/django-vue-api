<template>
    <div>
        <h2>Crear modulo</h2>
        <form>
            <input 
                type="text" 
                placeholder="Mac del modulo"
                v-model="mac">
            <select v-model="mina">
                <option 
                    placeholder="Mina asignada al modulo"
                    v-for="m in minas"
                    :key="m"
                    :value="m">
                    {{ m }}
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
        <button @click="">Agregar sensor</button>
        <pre>{{ $data }}</pre>
    </div>
</template>

<script>
export default {
    data() {
        return {
            mac: '',
            mina: '',
            area: '',
            minas: ['HERMOSILLO', 'CANANEA', 'ROCAPIEDRA'],
            areas: ['A', 'B', 'C', 'D']
        }
    }
}
</script>