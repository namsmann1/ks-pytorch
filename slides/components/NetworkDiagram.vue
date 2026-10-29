<script setup>
import { computed, ref } from 'vue'
const selected = ref(1)
const inputs = [0.2, 0.8, 0.5]
const weights = [[1, -0.5, 0.4], [-0.5, 1, 0.6], [0.4, 0.2, -1], [0.8, -0.2, 0.4]]
const bias = [0.1, -0.1, 0.2, 0]
const hidden = weights.map((row, j) => Math.max(0, row.reduce((sum, w, i) => sum + w * inputs[i], bias[j])))
const sums = weights.map((row, j) => row.reduce((sum, w, i) => sum + w * inputs[i], bias[j]))
const equation = computed(() => weights[selected.value].map((w, i) => `(${w.toFixed(1)}) × ${inputs[i].toFixed(1)}`).join(' + ') + ` + (${bias[selected.value].toFixed(1)})`)
</script>
<template>
  <div>
    <svg viewBox="0 0 900 285" class="w-full h-64" role="img" aria-label="Fullkoblet nettverk med tre innganger, fire skjulte nevroner og to utganger. Linjer viser vekter, sirkler viser verdier.">
      <text x="140" y="23" text-anchor="middle">Innganger</text>
      <text x="450" y="23" text-anchor="middle">Skjult lag · ReLU</text>
      <text x="760" y="23" text-anchor="middle">Rå skårer</text>
      <g v-for="(row,j) in weights" :key="j">
        <line v-for="(w,i) in row" :key="i" x1="140" :y1="80+i*75" x2="450" :y2="65+j*60" :stroke="w > 0 ? '#176b68' : '#b46c2e'" :stroke-width="Math.abs(w)*4" :opacity="selected===j ? 1 : .15" />
        <line v-for="k in 2" :key="`out${k}`" x1="450" :y1="65+j*60" x2="760" :y2="110+(k-1)*90" stroke="#82918f" stroke-width="1.5" />
      </g>
      <g v-for="(w,i) in weights[selected]" :key="`weight${i}`">
        <rect x="218" :y="(80+i*75)*0.65+(65+selected*60)*0.35-13" width="78" height="26" rx="4" fill="#faf9f5" />
        <text x="257" :y="(80+i*75)*0.65+(65+selected*60)*0.35+6" text-anchor="middle" :fill="w > 0 ? '#176b68' : '#b46c2e'" style="font-size: 17px !important">w{{i+1}}={{w.toFixed(1)}}</text>
      </g>
      <g v-for="(v,i) in inputs" :key="`in${i}`"><circle cx="140" :cy="80+i*75" r="24" :fill="`rgb(${255-v*150},${255-v*150},${255-v*150})`" stroke="#53616a"/><text x="140" :y="86+i*75" text-anchor="middle">{{v.toFixed(1)}}</text></g>
      <g v-for="(v,j) in hidden" :key="`hidden${j}`"><circle cx="450" :cy="65+j*60" r="24" :fill="selected===j ? '#c9e3dd' : '#eef3f0'" :stroke="selected===j ? '#176b68' : '#82918f'" :stroke-width="selected===j ? 3 : 1"/><text x="450" :y="71+j*60" text-anchor="middle">{{v.toFixed(2)}}</text></g>
      <g v-for="k in [0,1]" :key="`score${k}`"><circle cx="760" :cy="110+k*90" r="27" fill="#eef3f0" stroke="#176b68"/><text x="760" :y="116+k*90" text-anchor="middle">z{{k+1}}</text></g>
    </svg>
    <div class="flex items-center gap-3 text-sm"><span>Nevron:</span><button v-for="j in 4" :key="j" class="border rounded px-3 py-1" :style="{background:selected===j-1 ? '#c9e3dd' : 'transparent'}" @click="selected=j-1">{{j}}</button><span>Bias b = {{bias[selected].toFixed(1)}}</span></div>
    <div class="text-lg font-mono mt-4">z = {{ equation }} = {{ sums[selected].toFixed(2) }}</div>
    <div class="text-lg font-mono mt-2">h = ReLU(z) = max(0, {{ sums[selected].toFixed(2) }}) = {{ hidden[selected].toFixed(2) }}</div>
  </div>
</template>
