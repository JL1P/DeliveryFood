<template>
  <div id="app">
      <nav class="navbar is-warning" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <a id="logo" class="mx-1" href="#" style="width: 50px; padding: 0px">
            <img src="./assets/logo/lff.png" alt="logo">
          </a>

          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="showMenu">
            <span aria-hidden="true" class="toggle_menu"></span>
            <span aria-hidden="true" class="toggle_menu"></span>
            <span aria-hidden="true" class="toggle_menu"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu fade" :class="{'is-active': mostrar}">
          <div class="navbar-start">
            <a class="navbar-item ml-5">
              <strong class="items-nav">Restaurante</strong>
            </a>
            <a class="navbar-item ml-5">
              <strong class="items-nav">Repartidor</strong>
            </a>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <b-button id="pedirOrden" type="is-success">
                <strong style="color: white; font-style: italic">Realizar una orden</strong>
              </b-button>
            </div>
          </div>
        </div>
      </nav>
    <router-view/>
  </div>
</template>

<script>
export default {

data() {
  return {
   mostrar: false, 
  }
},
methods: {
  showMenu() {
    this.mostrar = !this.mostrar
  }
},
}
</script>

<style lang="scss">

.toggle_menu {
  color: rgb(0, 204, 163);
}

@media only screen and (max-width: 1023px) {
  .items-nav {
    color: rgb(0, 204, 163);
    font-size: 20px;
  }
  #pedirOrden {
    width: 100%;
  }
}
@media only screen and (min-width: 1024px) {
  .items-nav {
    color: white;
    font-size: 30px;
  }
  #logo {
    margin-top: 4px;
  }
}

.items-nav { 
  font-family: 'Times New Roman', Times, serif; 
  font-style: italic
}

#pedirOrden {
  background-color: rgb(0, 204, 163);
}

.navbar-menu.is-active {
    animation: navAnim .2s ease-in-out;
}

@keyframes navAnim {
  0% {
    display: none;
    opacity: 0;
    height: 0;
  }
  1% {
    display: block;
    opacity: 0;
  }
  100% {
    opacity: 1;
    height: 150px;
  }
}
</style>