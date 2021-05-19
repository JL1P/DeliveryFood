<template>
<<<<<<< HEAD
  <v-app>
    <v-app-bar
      absolute
      elevate-on-scroll
    >
      <v-app-bar-nav-icon class="ml-2 mr-2 pb-1">
        <img src="@/assets/lff.png" style="width:50px; height: 50px" alt="">
      </v-app-bar-nav-icon>

      <div id="menu">
        <v-item>
          <v-btn ml-2 elevation="0">
            <strong class="navs-item" style="font-size:25px;">Restaurante</strong>
          </v-btn>
        </v-item>
        <v-item>
          <v-btn ml-2 elevation="0">
            <strong class="navs-item" style="font-size:25px;">Repartidor</strong>
          </v-btn>
        </v-item>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        color=#ffdf4d
        elevation="0"
        id="ordenar"
      ><strong class="pedirOrden" style="color: white; font-style: italic">Realizar una orden</strong></v-btn>

      <div class="burger-menu">
        <v-menu rounded="b-xl" offset-y>
          <template v-slot:activator="{ attrs, on }">
              <v-btn 
                class="white--text ma-5"
                v-bind="attrs"
                v-on="on"
                  >
                <v-app-bar-nav-icon color="#00D1B2"></v-app-bar-nav-icon>
                <!-- Menu -->
              </v-btn>
          </template>
          <v-list>
          <v-list-item
            v-for="item in items"
            :key="item"
            link
              >
              <v-list-item-title v-text="item"></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>


    </v-app-bar>
    
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
=======
  <div id="app">

    <b-navbar id="myNavbar" toggleable="lg" type="dark" class="py-0">
    
      <b-navbar-brand href="/">
        <img src="./assets/Home/logo.png" alt="logo" style="width: 40px">
      </b-navbar-brand>
    
    </b-navbar>

    <router-view/>
  </div>
>>>>>>> main
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      btns: [
        ['Removed', '0'],
        ['Large', 'lg'],
        ['Custom', 'b-xl'],
      ],
      colors: ['deep-purple accent-4', 'error', 'teal darken-1'],
      items: [...Array(4)].map((_, i) => `Item ${i}`),
    }
  },
};
</script>

<style lang="scss">

<<<<<<< HEAD
  .burger-menu {
=======
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
>>>>>>> main
    display: none;
  }

  .navs-item {
    color: #00D1B2;
    font-family: 'Times New Roman', Times, serif; 
    font-style: italic
  }
<<<<<<< HEAD
  
  @media only screen and (max-width: 800px) {
    #menu {
      display: none
    }
    #ordenar {
      display: none;
    }
    .burger-menu {
      display: block;
    }
=======
  100% {
    opacity: 1;
    height: 116px;
>>>>>>> main
  }

</style>
