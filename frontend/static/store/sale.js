// document.addEventListener('DOMContentLoaded', event => {
// })

const getProduct = async () => {
  const barcode = document.getElementById('sale-product-code').value
  const description = document.getElementById('sale-product-description').value

  try {
    const { data } = await http.get(`products/?barcode=${barcode}&description__icontains=${description}`)
    renderProducts(data)
  } catch (error) {
    console.log(error)
  }
}

const renderProducts = products => {
  if (products.length == 0) {
    document.getElementById('products-results-tbody').innerHTML = '<h1>No se encontraron coincidencias</h1>'
    return
  }
  let productsHtml = ''
  for (const product of products) {
    productsHtml += `
      <tr>
        <td> <span class="name">${product.description}</span> </td>
        <td> <span class="">${product.barcode}</span> </td>
        <td><span class="time">Q${Number(product.cost_price).toFixed(2)}</span></td>
        <td><span class="time">${product.observations}</span></td>
        <td>
          <button type="button" class="btn btn-primary" onclick="addProductSale(${product.sale_price_1}, ${product.id}, '${product.description}')">Agregar Q${Number(product.sale_price_1).toFixed(2)}</button>
        </td>
        <td>
        <button type="button" class="btn btn-info" onclick="addProductSale(${product.sale_price_2}, ${product.id}, '${product.description}')">Agregar Q${Number(product.sale_price_2).toFixed(2)}</button>
        </td>
      </tr>
    `
  }
  document.getElementById('products-results-tbody').innerHTML = productsHtml
}

const thisSale = []

const addProductSale = (salePrice, productId, productDescription) => {
  const cantidad = prompt('Ingrese la cantidad a vender')
  if (!cantidad) {
    alert('Ingrese la cantidad a vender')
    return
  }
  thisSale.push({
    sale_price: salePrice,
    id: productId,
    description: productDescription,
    units: cantidad,
  })
  renderSaleProducts()
}

const removeProductSale = index => {
  thisSale.splice(index, 1)
  renderSaleProducts()
}

let total = 0

const renderSaleProducts = () => {
  let productsHtml = ''
  let index = 0
  total = 0
  for (const product of thisSale) {
    subtotal = product.sale_price * product.units
    total += subtotal
    productsHtml += `
      <tr>
        <td> <span class="">${index + 1}</span> </td>
        <td> <span class="name">${product.description}</span> </td>
        <td> <span class="">${product.units}</span> </td>
        <td><span class="time">Q${Number(product.sale_price).toFixed(2)}</span></td>
        <td><span class="time">${Number(subtotal).toFixed(2)}</span></td>
        <td>
          <button type="button" class="btn btn-danger" onclick="removeProductSale(${index++})">Eliminar</button>
        </td>
      </tr>
    `
  }
  document.getElementById('sale-products-added').innerHTML = productsHtml
  document.getElementById('sale-save-btn-amount').innerHTML = `Total : Q${total.toFixed(2)}`
}

const saveSale = async () => {
  const client = document.getElementById('sale-client').value
  if (client === ''){
    alert('Seleccione al cliente')
    return
  }

  if (thisSale.length == 0) {
    alert('Agregue al menos un producto a vender')
    return
  }

  if (!confirm('Guardar venta?')) {
    return
  }

  try {
    const {data} = await http.post('sale/create/', {client, total})
    saveSaleDetail(data.sale_pk)
    alert('Venta guardada')
    location.href = '/'
  } catch (error) {
    alert('No se pudo guardar la venta, intente nuevamente')
  }

}

const saveSaleDetail = async saleId => {
  try {
    for (const product of thisSale) {
      const data = {
        sale_price: product.sale_price,
        product: product.id,
        sale: saleId,
        unit: product.units,
        subtotal: product.units * product.sale_price
      }
      const response = await http.post('sale_detail/', data)
    }
  } catch (error) {
    console.log(error)
  }
}