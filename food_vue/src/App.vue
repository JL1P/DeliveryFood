<template>
  <div id="app">

    <b-navbar id="myNavbar" toggleable="lg" type="dark" class="py-0">
    
      <b-navbar-brand href="/">
        <img src="./assets/Home/logo.png" alt="logo" style="width: 40px">
      </b-navbar-brand>
    
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

@import "./assets/scss/main";

#myNavbar {
  background-color: $blue0;
}

.toggle_menu {
  color: rgb(0, 204, 163);
  border: 1px solid
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
    height: 116px;
  }
}
</style>