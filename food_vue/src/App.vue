<template>
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

  .burger-menu {
    display: none;
  }

  .navs-item {
    color: #00D1B2;
    font-family: 'Times New Roman', Times, serif; 
    font-style: italic
  }
  
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
  }

</style>
