<template>
    <div>
      <h1 class="display-4">Cadastro de Cliente</h1>
  
      <!-- Botão para abrir o Modal -->
      <button class="btn btn-success mb-4" @click="openNewCustomerModal">Novo Cliente</button>
  
      <!-- Modal para Cadastrar Cliente -->
      <div class="modal" :class="{ 'is-active': modalActive }">
        <div class="modal-background" @click="closeModal"></div>
        <div class="modal-content">
          <div class="box">
            <h1 class="title">Novo Cliente</h1>
            <!-- Formulário no Modal -->
            <form @submit.prevent="submitForm">
              <div class="field">
                <label for="name" class="label">Nome:</label>
                <div class="control">
                  <input v-model="customer.name" class="input" type="text" id="name" placeholder="Digite o nome do cliente" required />
                </div>
              </div>
              <div class="field">
                <label for="cardId" class="label">Número do Cartão:</label>
                <div class="control">
                  <input v-model="customer.card_id" class="input" type="text" id="cardId" placeholder="Digite o número do cartão" required />
                </div>
              </div>
              <button type="submit" class="button is-primary">Cadastrar</button>
            </form>
          </div>
        </div>
        <button class="modal-close is-large" aria-label="close" @click="closeModal"></button>
      </div>
  
      <!-- Lista de clientes cadastrados -->
      <div v-if="customers.length > 0" class="mt-4">
        <h2 class="display-5">Clientes Cadastrados:</h2>
        <div id="DATATABLEDIVCUSTOMER"></div>
      </div>
    </div>
  </template>
  
  <script>
import { ref } from 'vue';
import axios from 'axios';
import $ from 'jquery';
import 'bootstrap';
import Swal from 'sweetalert2';
$(function(){
  montaDataTable();
})

function montaDataTable(){
  $('#DATATABLEDIVCUSTOMER').empty()
  let table = `<table id="customerTable" class="table is-striped is-fullwidth">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Número do Cartão</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="customer in customers" :key="customer.id">
              <td>{{ customer.id }}</td>
              <td>{{ customer.name }}</td>
              <td>{{ customer.card_id }}</td>
              <td>
                <button class="button is-info is-small" @click="editCustomer(customer)">Editar</button>
                <button class="button is-danger is-small" @click="deleteCustomer(customer.id)">Excluir</button>
              </td>
            </tr>
          </tbody>
        </table>`;
  $('#DATATABLEDIVCUSTOMER').html(table);
  $('#customerTable').DataTable({
        responsive: true,
        paging: false,
        searching: false,
        info: false,
      });
}

export default {
  setup() {
    const customer = ref({
      id: null,
      name: '',
      card_id: '',
    });

    const customers = ref([]);
    const modalActive = ref(false);

    const openNewCustomerModal = () => {
      customer.value = { id: null, name: '', card_id: '' };
      modalActive.value = true;
    };

    const submitForm = async () => {
  try {
    let response;
    let update = false;

    if (customer.value.id) {
      response = await axios.put(`http://localhost:8000/api/v1/customer/${customer.value.id}/`, customer.value);
      update = true;
    } else {
      response = await axios.post('http://localhost:8000/api/v1/customer/', customer.value);
    }

    if (response.data) {
      if (update) {
        Swal.fire({
          text: 'Cliente Atualizado com sucesso',
          icon: 'success',
        });

        const existingCustomerIndex = customers.value.findIndex(c => c.id === response.data.id);

        if (existingCustomerIndex !== -1) {
          // Atualize os dados existentes ao invés de adicionar novamente
          customers.value[existingCustomerIndex] = response.data;
        }
      } else {
        Swal.fire({
          text: 'Cliente Cadastrado com sucesso',
          icon: 'success',
        });

        // Adicione o novo cliente apenas se não for uma atualização
        customers.value.push(response.data);
      }
      montaDataTable();
    }

    customer.value = { id: null, name: '', card_id: '' };
    closeModal();
  } catch (error) {
    console.error('Erro ao cadastrar o cliente:', error);
  }
    };

    const fetchCustomers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/customer/list/');
        console.log('Dados dos clientes:', response.data);
        customers.value = response.data;
        montaDataTable();
      } catch (error) {
        console.error('Erro ao buscar clientes:', error);
      }
    };

    const openModal = () => {
      modalActive.value = true;
    };

    const closeModal = () => {
      modalActive.value = false;
    };

    const editCustomer = (customerToEdit) => {
      customer.value = { ...customerToEdit };

      openModal();
    };

    const deleteCustomer = async (customerId) => {
      try {
        const confirmed = await Swal.fire({
          icon: 'warning',
          title: 'Tem certeza?',
          text: 'Deseja realmente excluir o cliente?',
          showCancelButton: true,
          confirmButtonColor: '#d33',
          cancelButtonColor: '#3085d6',
          confirmButtonText: 'Sim, excluir',
          cancelButtonText: 'Cancelar',
        });

        if (confirmed.isConfirmed) {
          await axios.delete(`http://localhost:8000/api/v1/customer/delete/${customerId}/`);

          customers.value = customers.value.filter((c) => c.id !== customerId);

          closeModal();

          Swal.fire({
            icon: 'success',
            title: 'Exclusão bem-sucedida!',
            text: 'Cliente excluído com sucesso.',
          });
          montaDataTable();
        }
      } catch (error) {
        console.error('Erro ao excluir o cliente:', error);
      }
    };

    return {
      customer,
      customers,
      modalActive,
      openNewCustomerModal,
      submitForm,
      fetchCustomers,
      openModal,
      closeModal,
      editCustomer,
      deleteCustomer,
    };
  },
  mounted() {
    this.fetchCustomers();
  },
};
</script>

<style scoped>
/* Seus estilos aqui, se necessário */
</style>
  
  