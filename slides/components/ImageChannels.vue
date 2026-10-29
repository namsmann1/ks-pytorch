<script setup>
const colors = ['#e06030', '#4080c0', '#80c040', '#c04080']
const channels = [{name:'R', values:[224,64,128,192], color:'#b54838'}, {name:'G',values:[96,128,192,64],color:'#3c7e49'}, {name:'B',values:[48,192,64,128],color:'#426caa'}]
</script>
<template>
<svg viewBox="0 0 900 270" class="w-full h-65" role="img" aria-label="Et RGB-bilde med fire piksler deles i tre matriser med verdier for rødt, grønt og blått.">
 <text x="100" y="30" text-anchor="middle">RGB-bilde</text>
 <rect v-for="(c,i) in colors" :key="i" :x="40+(i%2)*60" :y="65+Math.floor(i/2)*60" width="60" height="60" :fill="c"/>
 <path d="M210 125 H250 M240 115 L250 125 L240 135" fill="none" stroke="#53616a" stroke-width="3" />
 <g v-for="(c,j) in channels" :key="c.name">
  <text :x="350+j*200" y="30" text-anchor="middle" :fill="c.color">{{c.name}}</text>
  <g v-for="(v,i) in c.values" :key="i"><rect :x="290+j*200+(i%2)*60" :y="65+Math.floor(i/2)*60" width="60" height="60" fill="#eef3f0" :stroke="c.color"/><text :x="320+j*200+(i%2)*60" :y="101+Math.floor(i/2)*60" text-anchor="middle">{{v}}</text></g>
 </g>
 <text x="450" y="240" text-anchor="middle">Tre kanaler, samme pikselposisjoner: [3, 2, 2]</text>
</svg>
</template>
