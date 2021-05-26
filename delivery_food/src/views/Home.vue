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
        <div>
          <b-card-group deck>
            <b-card
              title="Pide de tus restaurantes favoritos"
              img-alt="Restaurante"
              img-src="https://picsum.photos/400/400/?image=20"
              id="img1"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                En Delivery Food podrás encontrar una gran variedad de restaurantes y tipos de comidas. Tu restaurante favorito está a un clic de distancia.
              </b-card-text>

            </b-card>

            <b-card
              title="Ordena sin complicaciones"
              img-src="@/assets/Home/pedido.png"
              img-alt="Restaurante"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                ¿Quieres sushi, hamburguesa o una pizza? Con Delivery Food ordenar es fácil
                y rápido. ¿No tienes efectivo? No te preocupes, también puedes pagar
                con tarjeta de crédito. Nuestra prioridad es que recibas tu comida
                directamente en tu puerta.
              </b-card-text>

            </b-card>

            <b-card
              title="Entrega express"
              img-src="@/assets/Home/entrega.png"
              img-alt="Restaurante"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                Los repartidores expertos de Delivery Food garantizan que las órdenes sean
                 entregadas rápidamente y en perfectas condiciones.
              </b-card-text>

            </b-card>
            
          </b-card-group>
          
        </div>
      </b-container>

      <b-container id="descargaApp" class="mt-5 pt-5">
        <b-row>

          <b-col>
            <h1 class="mb-4">Descarga la app de Delivery Food</h1>
            <p class="mb-5">La comida que deseas esta a unos clicks de distancia</p>
            <b-row>
              <b-col>
                <p>App Android</p>
              </b-col>
              <b-col>
                <p>App IOs</p>
              </b-col>
            </b-row>
          </b-col>

          <b-col>
            <h1>Imagen screenshot en las apps</h1>
          </b-col>
          
        </b-row>
      </b-container>

      <b-container id="trgtasRegistro" class="pt-5">

          <b-card no-body class="overflow-hidden mt-5" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <b-card-img src="../assets/Home/registro-restaurante.png" alt="Registrate como restaurante" class="rounded-0"></b-card-img>
              </b-col>
              <b-col md="6">
                <b-card-body title="Conviértete en una Tienda Delivery">
                  <b-card-text>
                    Asóciate con Delivery Food para atraer más clientes con facilidad y llevar tu negocio al
                     siguiente nivel.
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
          
          <b-card no-body class="overflow-hidden mt-5" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <b-card-body title="Únete al equipo de entregas de Delivery Food">
                  <b-card-text>
                    Únete al equipo de entregas de Delivery Food y entrega órdenes con tu scooter, 
                      bici o moto. Puedes elegir libremente las horas y ganar dinero y recompensas.
                  </b-card-text>
                </b-card-body>
              </b-col>
              <b-col md="6">
                <b-card-img src="../assets/Home/registro-mensajero.png" alt="Registrate como repartidor" class="rounded-0"></b-card-img>
              </b-col>
            </b-row>
          </b-card>

      </b-container>
    
      <b-container id="ciudadesLanzadas" class="mt-5 mb-5 pt-3">
        
        <h1 class="ml-4" style="font-size: 50px">Municipios lanzados</h1>
        
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
  components: {
  }
}

#texto {
  font-family: 'Times New Roman', Times, serif; 
  background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(255,255,255,0));
  width: 100%;
}

//trgtas caracteristicas

#img1 {
  // background: url('../assets/Home/restaurante.png');
}

//
#ciudadesLanzadas {
  // background-color: gray;
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
  
  h1, h4 {
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
  
  h1, h4 {
    padding: 30px 15px;
  }
}

@media only screen and (min-width: 769px) and (max-width: 991px) {
  h1, h4 {
    margin-left: 20px;
  }
}

@media only screen and (min-width: 992px) {
  h1, h4 {
    margin-left: 48px;
  }
}

@media only screen and (min-width: 769px) {
  h1, h4 {
    padding-top: 15px;
  }
} 
</style>