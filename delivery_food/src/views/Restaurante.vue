<template>
    <div id="restaurante-page">

        <b-container id="registroRestaurante">
            <b-row>
                <b-col md="4" class="mb-5">
                    <h1>Únete a Delivery Food y ve crecer tu negocio</h1>
                    <h4>Plataforma rápida y confiable de entrega de comida.</h4>
                </b-col>
                <b-col id="formulario" md="4" offset-md="4" class="p-3">
                    <h3>Hazte socio</h3>
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