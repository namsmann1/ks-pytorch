<script setup>
import { computed, ref } from 'vue'
const level = ref(204)
const value = computed(() => Number(level.value))
</script>
<template>
 <div class="flex items-center gap-12 my-8">
  <div class="w-40 h-40 border border-slate-400" :style="{background:`rgb(${value},${value},${value})`}" role="img" :aria-label="`Gråtone med pikselverdi ${value}`"></div>
  <div><div class="text-2xl font-mono">{{value}} / 255 = {{(value/255).toFixed(3)}}</div><label class="block mt-6 text-lg">Pikselverdi: <input v-model="level" type="range" min="0" max="255" aria-label="Pikselverdi fra null til 255" class="w-64 align-middle" /></label><div class="text-base mt-4">0: svart · 255: hvitt</div></div>
 </div>
</template>
