<template>
  <div id="wrapper">
    <nav class="navbar is_dark" style="background-color: #d3d3d3;">
      <div class="navbar-item">
            <div class="buttons">
              <router-link to="/park" class="button is-light"><strong>Estacionamento</strong></router-link>
            </div>
          </div>
      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/customer" class="button is-light">Clientes</router-link>
            </div>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/contract" class="button is-light">Contratos</router-link>
            </div>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/vehicle" class="button is-light">Veiculos</router-link>
            </div>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/plan" class="button is-light">Planos</router-link>
            </div>
          </div>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/operation" class="button is-light">Operação</router-link>
            </div>
          </div>
        </div>  
      </div>
    </nav>
    <section class="section" style="flex: 1; display: flex; align-items: center; justify-content: center;">
      <router-view/>
    </section>

    <footer class="is_fixed-bottom">
      <div class="content has-text-centered" style="">
        <p>Copyright (c) 2024</p>
      </div>
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';

.is_fixed-bottom {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #5dbda8;
  padding: 10px;
}
</style>
