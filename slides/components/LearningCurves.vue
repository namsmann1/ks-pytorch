<template>
  <svg viewBox="0 0 900 290" class="w-full h-70" role="img" aria-labelledby="curve-title curve-desc">
    <title id="curve-title">Skjematisk eksempel på overtilpasning</title>
    <desc id="curve-desc">Treningstap synker gjennom hele treningen. Valideringstap synker først, men stiger deretter.</desc>
    <path d="M90 25 V235 H840" fill="none" stroke="#53616a" stroke-width="2" />
    <text x="42" y="45" fill="#202d37" style="font-size: 18px !important">Tap</text>
    <text x="725" y="275" fill="#202d37" style="font-size: 18px !important">Epoke →</text>
    <path d="M110 45 C180 130 250 170 360 190 S640 222 820 226" fill="none" stroke="#176b68" stroke-width="4" />
    <path d="M110 40 C200 130 270 158 390 164 S660 110 820 65" fill="none" stroke="#b46c2e" stroke-width="4" stroke-dasharray="9 5" />
    <text x="645" y="202" fill="#176b68" style="font-size: 20px !important">Trening</text>
    <text x="625" y="70" fill="#985521" style="font-size: 20px !important">Validering</text>
  </svg>
</template>
