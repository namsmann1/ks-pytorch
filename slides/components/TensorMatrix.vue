<script setup>
defineProps({ rows: Array, selected: { type: Array, default: () => [] }, label: String })
</script>
<template>
  <div>
    <div class="matrix" :style="{ gridTemplateColumns: `repeat(${rows[0].length}, 1fr)` }">
      <template v-for="(row, r) in rows" :key="r">
        <span v-for="(value, c) in row" :key="c" :class="{ selected: selected.includes(`${r},${c}`) }">{{ value }}</span>
      </template>
    </div>
    <div v-if="label" class="matrix-label">{{ label }}</div>
  </div>
</template>
