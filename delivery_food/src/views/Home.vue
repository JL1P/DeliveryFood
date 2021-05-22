<template>
  <div class="home">
    <div>
      <b-container id="inicio" class="p-0">
        <div style="height: 480px">
        </div>
      <div id="texto">
        <h2 class="ml-5 mb-2" style="color: white">Tu comida cuando quieras, donde quieras</h2 >
        <p class="ml-5" style="color: white">Una plataforma de servicio a domicilio que lleva la comida de tu restaurante favorito a tu puerta.</p>
      </div>
      </b-container>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
  }
}
</script>

<style lang="scss">

@import '@/assets/scss/app.scss';

#inicio {
  background: url('../assets/Home/pcpal.png');
  filter: saturate(150%) contrast(120%);
  components: {
  }
}

#texto {
  background: linear-gradient(to top, rgba(0,0,0,0.7), rgba(255,255,255,0));
  height: 100px;
  width: 100%;
}
  
</style>