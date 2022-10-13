<template>
    <div class="modulo">
        <p class="modulo__mina blanco-b txt-upper">hermosillo</p>
        <h3 class="modulo__mac blanco-a txt-upper">123456789AZS</h3>
        <p class="modulo__zona blanco-b txt-upper">zona: a</p>
    </div>
</template>

<style scoped>
    .modulo{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex-basis: calc((100% / 4) - 1rem);
        height: 20rem;
        margin: 0 .3rem;
        margin-bottom: .8rem;
        padding: 2rem 2rem;
        background-color: rgb(19, 18, 24);
        border: none;
        border-top: 3rem solid rgb(56, 199, 115);
        border-radius: 1.5rem;
        transition: all .3s ease-in-out;
    }
    .modulo:hover{
        cursor: pointer;
        background-color: rgb(49, 45, 65);
    }
    .modulo__mac{
        font-size: 2.5rem;
    }
</style>