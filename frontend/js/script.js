const BASE_URL = "http://127.0.0.1:5000";

// Get Menu
function getMenu() {
    fetch(`${BASE_URL}/menu`)
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("menu");
        list.innerHTML = "";

        data.forEach(item => {
            list.innerHTML += `<li>${item.name} - ₹${item.price}</li>`;
        });
    });
}

// Place Order
function placeOrder() {
    let qty = document.getElementById("qty").value;

    let data = {
        items: [
            { name: "Pizza", price: 200, quantity: Number(qty) }
        ]
    };

    fetch(`${BASE_URL}/order`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        document.getElementById("result").innerText =
            `Order ID: ${response.order_id}, Total: ₹${response.total}`;
    });
}

// Get Orders
function getOrders() {
    fetch(`${BASE_URL}/orders`)
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("orders");
        list.innerHTML = "";

        data.forEach(order => {
            list.innerHTML += `<li>Order ${order.id} - ₹${order.total}</li>`;
        });
    });
}