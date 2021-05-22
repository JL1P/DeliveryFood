<template>
  <div id="app">
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
              <strong>Restaurante</strong>
            </b-button>
            <b-button 
              id="repartidor" class="items-nav my-auto" 
              style="box-shadow: none"
              :to="{name: 'Repartidor'}">
              <strong>Repartidor</strong>
            </b-button>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button id="pedirOrden" class="items-nav"
              style="box-shadow: none; font-size: 20px">
              <strong>Realizar una orden</strong>
            </b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    
    <br/>

    <router-view/>
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
  font-family: 'Times New Roman', Times, serif; 
  font-style: italic;
}

#pedirOrden {
  background-color: $green0;
  border: none;
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