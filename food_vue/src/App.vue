<template>
  <div id="app">
      <b-navbar 
        shadow
        type=is-warning
        >
        <template #brand>
            <b-navbar-item class='ml-5 py-0' tag="router-link" :to="{ path: '/' }">
                <img
                    src="./assets/lff.png"
                    alt="Logo"
                >
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item href="#" class='ml-5 py-0'>
              <strong class="items-nav">Restaurante</strong>
            </b-navbar-item>
            <b-navbar-item href="#" class='ml-5 py-0'>
              <strong class="items-nav">Repartidor</strong>
            </b-navbar-item>
        </template>

        <template #end>
            <b-navbar-item tag="div" class="py-0">
                <div class="buttons">
                    <a class="button" style="background: rgb(0, 204, 163); border: none">
                        <strong style="color: white; font-style: italic">Realizar una orden</strong>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
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