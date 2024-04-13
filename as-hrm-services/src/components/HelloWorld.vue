<script setup>
import { ref } from 'vue';
let states;
const ar = ref(null);

fetch('http://127.0.0.1:5000/getStates')
    .then(response => response.json())
    .then(data => ar.value = data)
</script>

<style>
    
</style>

<template>
    <div class="card m-3">
        <h5 class="card-header">Simple POST Request</h5>
        <div class="card-body">
            <li v-for="state in ar.states">
                <input type="checkbox" id="checkbox" v-model="checked" />
                <label for="checkbox">{{ state }}</label>
            </li>
        </div>
    </div>
</template>