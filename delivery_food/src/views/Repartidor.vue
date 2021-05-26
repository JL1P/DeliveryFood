<template>
    <div id="repartidor-page">
        
        <b-container id="registroRepartidor" class="mt-5">
            <b-row>
                <b-col cols="5">
                    <h1 class="px-0">¡Únete a Delivery Food! Obtén excelentes ganancias y otras recompensas.</h1>
                    <h4 class="px-0">Comenzar es sencillo y tú mismo estableces tu horario</h4>
                    <b-button>
                        Únete ahora
                    </b-button>
                </b-col>
                <b-col cols="7">
                    <h1>Imagen de repartidor</h1>
                </b-col>
            </b-row>
        </b-container>

        <b-container id="caracteristicasRepartidor" class="my-5 pt-5">
            <div>
                <b-card-group deck>
                    <b-card
                    title="Obtén excelentes ganancias"
                    img-src="@/assets/Home/restaurante.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        Esto es posible gracias a la gran cantidad de pedidos y a las 
                            generosas recompensas. Con Delivery Food, cuanto más te 
                            esfuerces, mayor será tu ganancia.
                    </b-card-text>

                    </b-card>

                    <b-card
                    title="Disfruta de más libertad"
                    img-src="@/assets/Home/pedido.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        Delivery Food te ofrece más libertad al permitirte establecer tus 
                            propios horarios y conectarte cuando quieras. Además, 
                            recoger pedidos y entregarlos es muy sencillo gracias a 
                            nuestro sistema de navegación fácil de usar. Si tienes una 
                            moto o una bicicleta, empieza a ganar dinero sobre la
                            marcha. Con Delivery Food, tienes la libertad de establecer 
                            tu propio horario y aprovechar tu tiempo al máximo.
                    </b-card-text>

                    </b-card>

                    <b-card
                    title="Delivery te cuida"
                    img-src="@/assets/Home/entrega.png"
                    img-alt="Restaurante"
                    img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
                    >
                    <b-card-text>
                        En Delivery Food, cuidamos a nuestros repartidores y priorizamos 
                            sus intereses. En nuestro equipo, los repartidores son mucho 
                            más que socios… forman parte de una gran familia. Con Delivery Food, 
                            podrás sentirte orgulloso de saber que agregas gran valor al 
                            servicio y obtienes recompensas por tu esfuerzo.
                    </b-card-text>

                    </b-card>
                    
                </b-card-group>
            
            </div>
        </b-container>
        
        <b-container id="diagramaRegistro">
            <h1>COMO SER UN SOCIO DE ENTREGA</h1>
            <h4>Diagrama de registro</h4>
        </b-container>

        <b-container id="descargaAppRepartidor" class="mt-5 pt-5" style="text-align: center">

            <h1 class="mb-4">Obtén la aplicación repartidor</h1>
            <h3 class="mb-5">Despreocúpate y acepta pedidos con mayor facilidad</h3>
            <b-row>
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
    name: 'Repartidor'
}
</script>

<style lang="scss">

#diagramaRegistro {
    text-align: center;
}

</style>