<template>
  <div>
    <button @click="buscarCampos">Buscar Campos</button>
    <div v-if="erro" class="erro">{{ erro }}</div>
    <div v-if="campos">
      <h3>Campos Mais Repetidos:</h3>
      <pre>{{ campos }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      campos: null,
      erro: null,
    };
  },
  methods: {
    async buscarCampos() {
      try {
        const resposta = await fetch('http://localhost:5000/buscar-campos-mais-repetidos');
        if (!resposta.ok) {
          throw new Error('Erro ao buscar dados');
        }
        const dados = await resposta.json();
        this.campos = dados;
      } catch (error) {
        this.erro = error.message;
      }
    }
  }
};
</script>

<style scoped>
.erro {
  color: red;
}
</style>
