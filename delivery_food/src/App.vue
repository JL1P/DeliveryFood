<template>
  <div id="app">

    <!-- Navbar -->
    <div>
      <b-navbar id="navbar" toggleable="sm" type="dark" class="px-0 py-0">
        <b-navbar-brand id="brand" :to="{name: 'Home'}">
          <img src="@/assets/Home/logo.png" alt="logo" style="width: 47px; height: 45px; padding-bottom: 1px">
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse">
          <template>
            <button class="menu" onclick="this.classList.toggle('opened');this.setAttribute('aria-expanded', this.classList.contains('opened'))" aria-label="Main Menu">
              <svg width="30" height="30" viewBox="0 0 100 100">
                <path class="line line1" d="M 20,29.000046 H 80.000231 C 80.000231,29.000046 94.498839,28.817352 94.532987,66.711331 94.543142,77.980673 90.966081,81.670246 85.259173,81.668997 79.552261,81.667751 75.000211,74.999942 75.000211,74.999942 L 25.000021,25.000058" />
                <path class="line line2" d="M 20,50 H 80" />
                <path class="line line3" d="M 20,70.999954 H 80.000231 C 80.000231,70.999954 94.498839,71.182648 94.532987,33.288669 94.543142,22.019327 90.966081,18.329754 85.259173,18.331003 79.552261,18.332249 75.000211,25.000058 75.000211,25.000058 L 25.000021,74.999942" />
              </svg>
            </button>
          </template>
        </b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-button 
              id="restaurante" class="items-nav my-auto" 
              style="box-shadow: none"
              :to="{name: 'Restaurante'}">
              <strong style="font-family: 'Times New Roman', Times, serif">Restaurante</strong>
            </b-button>
            <b-button 
              id="repartidor" class="items-nav my-auto" 
              style="box-shadow: none"
              :to="{name: 'Repartidor'}">
              <strong style="font-family: 'Times New Roman', Times, serif">Repartidor</strong>
            </b-button>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button id="pedirOrden" class="items-nav"
              style="box-shadow: none; font-size: 20px">
              <strong style="font-family: 'Times New Roman', Times, serif">Realizar una orden</strong>
            </b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    
    <br/>

    <router-view/>
    
    <!-- Footer -->
    <div id="footer" class="mt-5 pt-5 px-0 mx-0">

      <div id="contacto" class="py-5 px-5" style="text-align: center">
        <b-row>
          <div style="text-align: left; margin-right: 20%" class="ml-5">
            <img src="@/assets/Home/logo.png" alt="logo" style="width: 150px">
          </div>
          <b-list-group horizontal="md" style="text-align: left">
            <b-list-group-item class="listContacto">
              <div>
                <p class="mb-5 titlesFooter">Asóciate con nosotros</p>
                <p>Hazte repartidor de Delivery Food</p>
                <p>Abre una tienda en Delivery Food</p>
              </div>
            </b-list-group-item>
            <b-list-group-item class="listContacto">
              <div>
                <p class="mb-5 titlesFooter">Informacion de la empresa</p>
                <p>Acerca de Delivery Food</p>
                <p>Contáctanos</p>
              </div>
            </b-list-group-item>
            <b-list-group-item class="listContacto">
              <div>
                <p class="mb-5 titlesFooter">Sigue a Delivery Food</p>
                <div style="width: 185px">
                  <b-link href="#" class="redes">
                    <b-icon-facebook></b-icon-facebook>
                  </b-link>
                  <b-link href="#" class="ml-4 redes">
                    <b-icon-instagram></b-icon-instagram>
                  </b-link>
                  <b-link href="#" class="ml-4 redes">
                    <b-icon-twitter></b-icon-twitter>
                  </b-link>
                  <b-link href="#" class="ml-4 redes">
                    <b-icon-youtube></b-icon-youtube>
                  </b-link>
                </div>
              </div>
            </b-list-group-item>
          </b-list-group>
        </b-row>
      </div>

      <div id="idioma_copyright" class="py-5 pl-5" style="font-size: 14px; text-align: left">
        <b-list-group horizontal="md" class="pl-4">
          <b-list-group-item class="listIdioma pr-0 pt-1" style="width: 260px">

            <b-dropdown id="idioma" text="Español" class="m-2" style="border-radius: 50%;">
              <b-dropdown-item>Español</b-dropdown-item>
              <b-dropdown-item>English</b-dropdown-item>
            </b-dropdown>
            
          </b-list-group-item>
          <b-list-group-item class="listIdioma pr-0" style="width: 260px; margin-left: 13%">
            <p>@2021 Delivery Food</p>
          </b-list-group-item>
          <b-list-group-item class="listIdioma pr-0" style="width: 260px; margin-left: 5%">
           <p>Privacidad</p>
          </b-list-group-item>
        </b-list-group>
      </div>
      
    </div>
  </div>
</template>

<style lang="scss">

@import '@/assets/scss/app.scss';

#navbar {
  background-color: $yellow0;
}

#restaurante, #repartidor {
  background-color: rgba(255, 255, 255, 0);
  border: none;
  margin: 0px;
  padding: 0px;
  font-size: 30px;
}

.items-nav { 
  font-style: italic;
}

* {
  font-family: Andale Mono, monospace;
}

#pedirOrden {
  background-color: $green0;
  border: none;
}

#footer {
  text-align: center;
  color: white;
}

#contacto {
  background-color: #333740;
}

.listContacto {
  background-color: #333740 !important;
  border: none !important;
}

.listIdioma {
  background-color: #2C2F36 !important;
  border: none !important;
}

#idioma_copyright {
  background-color: #2C2F36;
}

.redes {
  color: white; 
  font-size: 25px;
}

.titlesFooter {
  color: #9B9B9B;
}

#idioma .dropdown-menu {
  background: transparent;
}

button.dropdown-toggle {
  border-radius: 20px;
  outline: 0px;
  background: transparent;
}

a.dropdown-item {
  color: white !important;
}

a.dropdown-item:hover {
  color: black !important;
}

a.dropdown-item:active {
  background-color: aliceblue !important;
}


//Burger Menu
.menu {
  background-color: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  padding: 0;
}
.line {
  fill: none;
  stroke: $green0;
  stroke-width: 6;
  transition: stroke-dasharray 600ms cubic-bezier(0.4, 0, 0.2, 1),
    stroke-dashoffset 600ms cubic-bezier(0.4, 0, 0.2, 1);
}
.line1 {
  stroke-dasharray: 60 207;
  stroke-width: 6;
}
.line2 {
  stroke-dasharray: 60 60;
  stroke-width: 6;
}
.line3 {
  stroke-dasharray: 60 207;
  stroke-width: 6;
}
.opened .line1 {
  stroke-dasharray: 90 207;
  stroke-dashoffset: -134;
  stroke-width: 6;
}
.opened .line2 {
  stroke-dasharray: 1 60;
  stroke-dashoffset: -30;
  stroke-width: 6;
}
.opened .line3 {
  stroke-dasharray: 90 207;
  stroke-dashoffset: -134;
  stroke-width: 6;
}


@media only screen and (max-width: 575px) {
  #restaurante, #repartidor {
    color: $green0;
  }

  #brand {
    margin-left: 5px;
  }

  #nav-collapse {
    background-color: white;
  }
}

@media only screen and (min-width: 576px) {
  #brand {
    margin-left: 5px;
  }
  
  #repartidor {
    margin-left: 15px;
  }

  #pedirOrden {
    margin-right: 6px;
  }
}

@media only screen and (min-width: 730px) {
  #brand {
    margin-left: 10px;
  }
  
  #repartidor {
    margin-left: 20px;
  }

  #pedirOrden {
    margin-right: 10px;
  }
}

@media only screen and (min-width: 1000px) {
  #brand {
    margin-left: 40px;
  }
  
  #restaurante {
    margin-left: 25px;
  }

  #repartidor {
    margin-left: 50px;
  }

  #pedirOrden {
    margin-right: 40px;
  }
}
</style>