
const getTodaySales = async () => {
  const today = new Date()
  const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
  try {
    const {data} = await http.get(`sales/?date=${date}`)
    renderTodaySales(data)
  } catch (error) {
    console.log(error)
  }

}

const renderTodaySales = sales => {
  if (sales.length == 0) {
    document.getElementById('sales-report').innerHTML = '<h1>No hay ventas realizadas el día de hoy</h1>'
    return
  }
  let salesHtml = ''
  for (const sale of sales) {
    salesHtml += `
      <tr>
        <td> <span class="">${sale.sale_number}</span> </td>
        <td> <span class="name">${sale.client.name} -- ${sale.client.nit}</span> </td>
        <td> <span class="">${Number(sale.total).toFixed(2)}</span> </td>
        <td>
          <a type="button" class="btn btn-success" href="/sale/${sale.id}/">Ver Venta</a>
        </td>
      </tr>
    `
  }
  document.getElementById('sales-report').innerHTML = salesHtml
}

document.addEventListener('DOMContentLoaded', event => {
  getTodaySales()
})
