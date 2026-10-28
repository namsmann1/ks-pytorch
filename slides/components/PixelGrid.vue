<script setup>
const values = [0, 0, 0, 0, 0, .4, .8, 0, 0, .8, 1, 0, 0, 0, 0, 0]
</script>
<template>
  <div class="grid grid-cols-4 w-72 h-72 border border-slate-400" role="img" aria-label="Fire ganger fire piksler med lysstyrke mellom null og én">
    <div v-for="(value, index) in values" :key="index" class="flex items-center justify-center border border-gray-500 text-xl font-mono" :style="{ background: `rgb(${value*255},${value*255},${value*255})`, color: value > .5 ? '#111' : '#fff' }">{{ value.toFixed(1) }}</div>
  </div>
</template>
