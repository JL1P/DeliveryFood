<template>
    <div id="restaurante-page">

        <b-container id="registroRestaurante">
            <b-row style="height:100%">
                <b-col id="textRegRest" md="4" class="mb-5 pt-5 px-5">
                    <h1 class="">Únete a Delivery Food y ve crecer tu negocio</h1>
                    <h4 class="ml-0" style="width:60%">Plataforma rápida y confiable de entrega de comida.</h4>
                </b-col>
                <b-col id="formRegRest" md="4" offset-md="4" class="p-3">
                    <h4 class="ml-0">Hazte socio</h4>
                </b-col>
            </b-row>
        </b-container>
        
        <b-container id="caracteristicasRestaurante" class="my-5 pt-5">
            <div>
                <b-card-group deck>
                    <b-card
                    title="Obtén más pedidos"
                    img-src="@/assets/Home/restaurante.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        La gran base de usuarios de Delivery Food te permite promocionar tu 
                            restaurante y enviarte nuevos clientes. Además, nuestra 
                            aplicación facilita a clientes realizar pedidos. Llevamos 
                            tus platillos a más personas y hacemos que a ellos les resulte 
                            más fácil volver a pedir.
                    </b-card-text>

                    </b-card>

                    <b-card
                    title="Entrega profesional"
                    img-src="@/assets/Home/pedido.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        Nuestro equipo experiemntado está ansioso por ayudarte a 
                            obtener más pedidos, incluso durante las horas pico, donde
                            hay mayor actividad. Nuestro proceso avanzando de preparación
                            y entrega garantiza que los clientes reciban sus pedidos tal
                            como lo desean, sin excepción. Lo único que debes hacer es 
                            preparar la comida: ¡Nosotros nos encargamos del resto!
                    </b-card-text>

                    </b-card>

                    <b-card
                    title="Servicio integral"
                    img-src="@/assets/Home/entrega.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        Nuestra línea de servicio integral lleva tu marca al siguiente
                            nivel. Desde nuestros representantes experimentados y nuestro 
                            práctico servicio de atención al cliente hasta el marketing 
                            personalizado y orientado a resultados, puedes contar con Delivery 
                            Food para respaldarte en cada paso del proceso.
                    </b-card-text>

                    </b-card>
                    
                </b-card-group>
            
            </div>
        </b-container>

        <b-container id="descargaAppRestaurante" class="mt-5 pt-5" style="text-align: center">

            <h1 class="mb-4">Descargar tienda de Delivery Food</h1>
            <h3 class="mb-5">¡Optimiza tu negocio y empieza a recibir más pedidos!</h3>
            <b-row>
                <b-col>
                    <p>App Pc</p>
                </b-col>
                <b-col>
                    <p>App IOs</p>
                </b-col>
                <b-col>
                    <p>App Android</p>
                </b-col>
            </b-row>
                
      </b-container>
        
    </div>
</template>

<script>
export default {
    name: 'Restaurante',
}
</script>

<style lang="scss">

@import '@/assets/scss/app.scss';

#registroRestaurante {
  background: url('http://localhost:8000/media/ImagenesSitio/registro-restaurante_M3YoWsZ.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  filter: saturate(150%) contrast(120%);
  width: 100%;
  height: 600px;
}
    
#textRegRest {
    color: white;
    height: 100%;
    background: linear-gradient(to right, rgba(0,0,0,0.8), rgba(255,255,255,0));
}
    
#formRegRest {
    color: white;
    background-color: rgba(0,0,0,0.5);
    height: 100%;
}

</style>