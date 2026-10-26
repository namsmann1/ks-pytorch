<template>
  <div v-if="!['cover', 'section'].includes($frontmatter.class)" class="footer">
    <span>PyTorch 101 · Fra tall til prediksjoner</span>
    <span>{{ String($page).padStart(2, '0') }}</span>
  </div>
</template>
