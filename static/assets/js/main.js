
import {  displayCompare, displayCart, displayWishlist, formatPrice} from './library.js';

window.onload = () =>{
    let mainContent
    
    console.log("compare");
    mainContent = document.querySelector('.compare_container')
    let compare = JSON.parse(mainContent?.dataset?.compare || false)
    
    displayCompare(compare)

    /******************************* */
    
    console.log("wishlist");
    mainContent = document.querySelector('.wishlist_content')
    let wishlist = JSON.parse(mainContent?.dataset?.wishlist || false)
    
    displayWishlist(wishlist)

     /******************************* */
    
    console.log("cart");
    mainContent = document.querySelector('.cart_content')
    let cart = JSON.parse(mainContent?.dataset?.cart || false)

    const form = document.querySelector(".carrier_form form")
    const select = document.querySelector(".carrier_form form select")
   
    let carriers =  JSON.parse(mainContent?.dataset?.carriers || false)
   
    if (cart) {
        select.innerHTML = ""
        carriers.forEach(carrier => {
            if(carrier.id == cart.carrier.id){
                select.innerHTML += `
                <option 
                 value="${carrier.id}" selected  > 
                 ${carrier.name} ( ${formatPrice(carrier.price / 100)} )
                 </option>
                `

            }else{
                select.innerHTML += `
                <option 
                 value="${carrier.id}"  > 
                 ${carrier.name} ( ${formatPrice(carrier.price / 100)} )
                 </option>
                `

            }

        });
    }

    const handleSubmit = (event) => {
        event.preventDefault();

    }
    const handleChange = async (event) => {
        event.preventDefault();
        const id = event.target.value
        if( id) {
            const response = await fetch('/api/cart/update/carrier/'+id)
            const result = await response.json()

            if(result.isSuccess){
                const {data} = result
                displayCart(data)
            }
        }
        console.log({id});

    }
    form?.addEventListener('submit', handleSubmit)
    select?.addEventListener('change', handleChange)
    
    displayCart(cart)
}
