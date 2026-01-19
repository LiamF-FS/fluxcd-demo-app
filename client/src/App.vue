<template>
  <div class="container">
    <h1>
      Testing OKD FluxCD Integration, handling updated docker images, etc.
    </h1>
    <h2>This is used as POC for a very important approach to GitOps</h2>
    <p>Version: {{ version }}</p>
    <img
      :src="currentImage"
      :style="{
        marginTop: '2%',
        marginBottom: '2%',
        transform: `rotate(${rotation}deg)`,
        transition: 'transform 2s',
      }"
    />
    <button class="button" @click="spinDaRodent">SPIN IT YOUNG MAN!!!</button>
    <p v-if="spins < 15">Bruh Spun: {{ spins }} times</p>
    <p v-else>bruh spun too much!!!!!!</p>
  </div>
</template>

<script setup>
import { version } from "../package.json";
import { ref, computed } from "vue";
import { env } from "@/env";

const spins = ref(0);
const rotation = ref(0);
const isXpp = ref(true);

const currentImage = computed(() => {
  return isXpp.value ? "/xpp.png" : "/xdd.png";
});

const spinDaRodent = async () => {
  try {
    const response = await fetch(`${env.VITE_BASE_API_URL}/spin-da-rodent`);
    const data = await response.json();

    spins.value = spins.value + data.spins;
    rotation.value = spins.value * 360;

    // Check if we hit 20 spins
    if (spins.value >= 15) {
      // Swap the image
      isXpp.value = !isXpp.value;
      // Reset spins to 0
      rotation.value = 0;

      await new Promise((r) => setTimeout(r, 2000));
      spins.value = 0;
    }
  } catch (error) {
    console.error("Error fetching spins:", error);
  }
};
</script>

<style scoped>
h1 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}
p {
  font-size: 1.2rem;
}
.container {
  text-align: center;
  width: 100vw;
  min-height: 100vh;
  background-color: lightcoral;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0;
  position: fixed;
  top: 0;
  left: 0;
}

.button {
  margin-top: 1vh;
  cursor: pointer;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: bold;
}
</style>
