<template>
  <div class="home">

    <div id="inicio" class="container mt-5">
      <div style="height: 480px">
        <div>
        </div>
      </div>
      <div id="texto">
        <h2 class="title is-2 ml-5 mb-2" style="color: white">Tu comida cuando quieras, donde quieras</h2 >
        <p class="title is-5 ml-5" style="color: white">Una plataforma de servicio a domicilio que lleva la comida de tu restaurante favorito a tu puerta.</p>
      </div>
    </div>
    
    <!-- Caracteristicas de la empresa -->
    
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
    
  },
  methods: {
    
  },
}

</script>

<style lang="scss">
  #inicio {
    background: url('../assets/Home/pcpal.png');
    filter: saturate(150%) contrast(120%);
  }
  #texto {
    background: linear-gradient(to top, rgba(0,0,0,0.7), rgba(255,255,255,0));
    height: 100px;
  }
</style>