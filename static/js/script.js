document.addEventListener('DOMContentLoaded', () => {
  let idCounter = 1;
  const form = document.getElementById('suplemento-form');
  const tableBody = document.querySelector('table tbody');

  form.addEventListener('submit', (event) => {
      event.preventDefault();

      const nome = document.getElementById('nome').value;
      const marca = document.getElementById('marca').value;
      const tipo = document.getElementById('tipo').value;

      const row = document.createElement('tr');
      row.innerHTML = `
          <td>${idCounter++}</td>
          <td>${nome}</td>
          <td>${marca}</td>
          <td>${tipo}</td>
          <td>
              <button class="btn btn-warning btn-sm edit">Editar</button>
              <button class="btn btn-danger btn-sm delete">Excluir</button>
          </td>
      `;
      tableBody.appendChild(row);

      form.reset();
  });

  tableBody.addEventListener('click', (event) => {
      if (event.target.classList.contains('delete')) {
          const row = event.target.closest('tr');
          tableBody.removeChild(row);
      }
      // Implementar a lógica de edição conforme necessário
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu-toggle');
  const wrapper = document.getElementById('wrapper');

  menuToggle.addEventListener('click', (e) => {
      e.preventDefault();
      wrapper.classList.toggle('toggled');
  });

  // Adicionar funcionalidade de preenchimento de dados para a tabela de suplementos consumidos
  const tableBody = document.querySelector('table tbody');

  // Exemplo de dados
  const suplementosConsumidos = [
      { id: 1, nome: 'Whey Protein', marca: 'Marca A', dataConsumo: '2023-01-01', quantidade: 30 },
      { id: 2, nome: 'Creatina', marca: 'Marca B', dataConsumo: '2023-01-05', quantidade: 5 },
      // Adicione mais dados conforme necessário
  ];

  suplementosConsumidos.forEach(suplemento => {
      const row = document.createElement('tr');
      row.innerHTML = `
          <td>${suplemento.id}</td>
          <td>${suplemento.nome}</td>
          <td>${suplemento.marca}</td>
          <td>${suplemento.dataConsumo}</td>
          <td>${suplemento.quantidade}</td>
      `;
      tableBody.appendChild(row);
  });

  // Calcular estatísticas
  const totalConsumido = suplementosConsumidos.reduce((sum, item) => sum + item.quantidade, 0);
  const mediaPorDia = (totalConsumido / suplementosConsumidos.length).toFixed(2);

  document.getElementById('total-consumido').innerText = totalConsumido;
  document.getElementById('media-por-dia').innerText = mediaPorDia;

  // Configurar o gráfico de consumo
  const ctx = document.getElementById('consumoChart').getContext('2d');
  const consumoChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: suplementosConsumidos.map(suplemento => suplemento.dataConsumo),
          datasets: [{
              label: 'Quantidade Consumida',
              data: suplementosConsumidos.map(suplemento => suplemento.quantidade),
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              fill: true,
          }]
      },
      options: {
          responsive: true,
          scales: {
              x: {
                  title: {
                      display: true,
                      text: 'Data de Consumo'
                  }
              },
              y: {
                  title: {
                      display: true,
                      text: 'Quantidade'
                  }
              }
          }
      }
  });
});




