<template>
  <div class="shift-illustration">
    <figure>
      <svg viewBox="0 0 28 28" role="img" aria-label="Sjutall i opprinnelig posisjon">
        <rect width="28" height="28" fill="#000" />
        <image href="/mnist-seven.svg" width="28" height="28" />
      </svg>
      <figcaption>Før</figcaption>
    </figure>
    <span class="shift-arrow">→</span>
    <figure>
      <svg viewBox="0 0 28 28" role="img" aria-label="Det samme sjutallet forskjøvet to piksler mot høyre">
        <rect width="28" height="28" fill="#000" />
        <image href="/mnist-seven.svg" x="2" width="28" height="28" />
      </svg>
      <figcaption>Forskjøvet</figcaption>
    </figure>
  </div>
</template>
<style scoped>
.shift-illustration { display: flex; align-items: center; justify-content: center; gap: 70px; }
figure { margin: 0; text-align: center; }
svg { width: 220px; height: 220px; image-rendering: pixelated; }
figcaption { font-size: 20px; margin-top: 10px; color: var(--muted); }
.shift-arrow { font-size: 36px; color: var(--accent); }
</style>
