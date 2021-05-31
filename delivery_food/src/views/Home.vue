<template>
  <div class="home">

      <b-container id="inicio" class="p-0">
        <div id="inicio2">
        </div>
        <div id="texto">
          <h1 class="mb-2" style="color: white">Tu comida cuando quieras, donde quieras</h1 >
          <h4 style="color: white">Una plataforma de servicio a domicilio que lleva la comida de tu restaurante favorito a tu puerta.</h4>
        </div>
      </b-container>

      <b-container id="caracteristicas" class="my-5 pt-5">
        <b-row align-h="between">
          <div id="card1" class="trgtasCaracteristicas" style="width: 30%">
            <div class="img-card">
              <img 
                src="http://localhost:8000/media/ImagenesSitio/restaurante_S1NkxHx.png" 
                alt="restaurante"
                style="width: 100%"
                >
            </div>
            <div class="body-card">
              <div class="tituloCaracteristicas">
                <h2>Pide de tus restaurantes favoritos</h2>
              </div>
              <div class="textoCaracteristicas">
                <p>
                  En Delivery Food podrás encontrar una gran variedad de restaurantes y tipos de comidas.
                    Tu restaurante favorito está a un clic de distancia.    
                </p>
              </div>
            </div>
          </div>

          <div id="card2" class="trgtasCaracteristicas" style="width: 30%">
            <div class="img-card">
              <img 
                src="http://localhost:8000/media/ImagenesSitio/pedido_qbVseVy.png" 
                alt="ordena de manera rápida"
                style="width: 100%"
                >
            </div>
            <div class="body-card">
              <div class="tituloCaracteristicas pt-2">
                <h2>Ordena sin complicaciones</h2>
              </div>
              <div class="textoCaracteristicas">
                <p>
                  ¿Quieres sushi, hamburguesa o una pizza? Con Delivery Food ordenar es fácil
                  y rápido. ¿No tienes efectivo? No te preocupes, también puedes pagar
                  con tarjeta de crédito. Nuestra prioridad es que recibas tu comida
                  directamente en tu puerta.
                </p>
              </div>
            </div>
          </div>
          
          <div id="card3" class="trgtasCaracteristicas" style="width: 30%">
            <div class="img-card">
              <img 
                src="http://localhost:8000/media/ImagenesSitio/entrega_WWAjIiK.png" 
                alt="Entrega express"
                style="width: 100%"
                >
            </div>
            <div class="body-card">
              <div class="tituloCaracteristicas pt-4">
                <h2>Entrega express</h2>
              </div>
              <div class="textoCaracteristicas">
                <p>
                Los repartidores expertos de Delivery Food garantizan que las órdenes sean
                 entregadas rápidamente y en perfectas condiciones.
                </p>
              </div>
            </div>
          </div>

        </b-row>        
      </b-container>

      <b-container id="descargaApp" class="mt-5 pt-5">
        <b-row>

          <b-col cols="4" style="text-align: left" class="pt-5">
            <h2 class="mb-4 mt-5">Descarga la app de Delivery Food</h2>
            <p class="mb-5">La comida que deseas esta a unos clicks de distancia.</p>
            <b-row>
              <b-col class="px-2">
                <b-link href="#">
                  <img src="http://localhost:8000/media/ImagenesSitio/descargaAppStore.gif" 
                    alt="Link de descarga de la App Store"
                    style="width: 100%"
                    >
                </b-link>
              </b-col>
              <b-col class="px-2">
                <b-link href="#">
                  <img src="http://localhost:8000/media/ImagenesSitio/disponible-en-google-play-badge.png" 
                    alt="Link de descarga de Google Play"
                    style="width: 100%"
                    >
                </b-link>
              </b-col>
            </b-row>
          </b-col>

          <b-col cols="8" style="text-align: right">
            <img src="http://localhost:8000/media/ImagenesSitio/Imagen_de_app_.png"
            alt="Imagen App Android"
            style="width: 80%"
            >
          </b-col>
          
        </b-row>
      </b-container>

      <b-container id="trgtasRegistro" class="pt-5 px-0">

          <b-card no-body class="overflow-hidden mt-5" style="border: none">
            <b-row no-gutters align-v="center" class="trgtasReg">
              <b-col md="8">
                <b-card-img src="http://localhost:8000/media/ImagenesSitio/registro_restaurante.jpg"
                  alt="Registrate como restaurante"
                  class="rounded-0">
                 </b-card-img>
              </b-col>
              <b-col md="4" class="cardbody">
                <b-card-body>
                  <b-card-text>
                    <h2 class="mx-4 mb-2">Conviértete en una Tienda Delivery</h2>
                    <p class="mx-4 mt-5">
                      Asóciate con Delivery Food para atraer más clientes con facilidad y llevar tu negocio al
                      siguiente nivel.
                    </p>
                    <div>
                      <b-button size="lg" variant="success" class="mx-4 mt-5" style="border-radius: 2px">
                        <p style="margin: 0px; font-size: 23px">Más información <b-icon icon="arrow-right" font-scale="1"></b-icon></p>
                      </b-button>
                    </div>
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
          
          <b-card no-body class="overflow-hidden mt-5" style="border: none">
            <b-row no-gutters align-v="center" class="trgtasReg"> 
              <b-col md="4" class="cardbody">
                <b-card-body>
                  <b-card-text>
                    <h2 class="mx-5 mb-2">Únete al equipo de entregas de Delivery Food</h2>
                    <p class="mx-5 mt-5">
                      Únete al equipo de entregas de Delivery Food y entrega órdenes con tu scooter, 
                        bici o moto. Puedes elegir libremente las horas y ganar dinero y recompensas.
                    </p>
                    <div>
                      <b-button size="lg" variant="success" class="mx-4 mt-5" style="border-radius: 2px">
                        <p style="margin: 0px; font-size: 23px">Más información <b-icon icon="arrow-right" font-scale="1"></b-icon></p>
                      </b-button>
                    </div>
                  </b-card-text>
                </b-card-body>
              </b-col>
              <b-col md="8">
                <b-card-img src="http://localhost:8000/media/ImagenesSitio/registro-mensajero.png"
                  alt="Registrate como repartidor"
                  class="rounded-0"
                  style="width: 102%">
                 </b-card-img>
              </b-col>
            </b-row>
          </b-card>

      </b-container>
    
      <b-container id="ciudadesLanzadas" class="mt-5 mb-5 pt-3">
        
        <h1 class="ml-4" style="font-size: 40px">Municipios lanzados</h1>
        
        <b-row class="ml-4 mt-5" id="mcpios">
          <b-col>Habana del Este</b-col>
          <b-col>Guanabo</b-col>
          <b-col>Guanabacoa</b-col>
          <b-col>Plaza</b-col>
          <b-col>Centro Habana</b-col>
        </b-row>
        <b-row class="ml-4 mt-4 pb-5" id="mcpios">
          <b-col>Arroyo Naranjo</b-col>
          <b-col>10 de Octubre</b-col>
          <b-col>Regla</b-col>
          <b-col>Marianao</b-col>
          <b-col>Habana Vieja</b-col>
        </b-row>
      </b-container>

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

//Inicio
#inicio {
  background: url('../assets/Home/pcpal.png');
  filter: saturate(150%) contrast(120%);
  width: 100%;
}

#texto {
  font-family: 'Times New Roman', Times, serif; 
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(255,255,255,0));
  width: 100%;
}

//trgtas caracteristicas

.trgtasCaracteristicas {
}

.tituloCaracteristicas {
  height: 35%;
  text-align: center;
  font-size: 35px;
  margin-bottom: 20px;
  color: $light;
}

.textoCaracteristicas {
  text-align: center;
  color: $light;
}

.body-card {
  padding: 20px;
  height: 50%;
}

#card1 {
  background-color: $dark;
}

#card2 {
  background-color: $green1;
}

#card3 {
  background-color: $yellow1;
}


//trgtas de registro

.trgtasReg {
  background-color: $gray0;
}

//
#ciudadesLanzadas {
  background-color: $gray0;
}

#mcpios {
  font-size: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

@media only screen and (min-width: 200px) and (max-width: 390px) {
  #inicio2 {
    height: 200px;
  }

  #texto {
    height: 400px;
  }
  
  #texto h1, h4 {
    padding: 30px 15px;
  }

}

@media only screen and (min-width: 391px) {
  h1, h4 {
    padding: 0px 15px;
  }

  #inicio2 {
    height: 400px;
  }

  #texto {
    height: 200px;
  }  
} 

@media only screen and (min-width: 200px) and (max-width: 769px) {
  #inicio2 {
    height: 200px;
  }

  #texto {
    height: 400px;
  }
  
  #texto h1, h4 {
    padding: 30px 15px;
  }
}

@media only screen and (min-width: 769px) and (max-width: 991px) {
  #texto h1, h4 {
    margin-left: 20px;
  }
}

@media only screen and (min-width: 992px) {
  #texto h1, h4 {
    margin-left: 48px;
  }
}

@media only screen and (min-width: 769px) {
  #texto h1, h4 {
    padding-top: 15px;
  }
} 
</style>