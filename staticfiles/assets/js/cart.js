
import { formatPrice,
    displayCompare,
    addCompareEventListener,
     addFlashMessage,
     fetchData, 
     manageCartLink, 
     addCartEventListenerToLink,
     initCart,
     updateHeaderCart,
     manageCompareLink} from './library.js';

window.onload = () =>{
    
    console.log("cart");

    let mainContent = document.querySelector('.main_content')

    let cart = JSON.parse(mainContent?.dataset?.cart || false)
    
    initCart(cart)

    updateHeaderCart(cart)
    
    console.log("compare");

    mainContent = document.querySelector('.compare_container')

    let compare = JSON.parse(mainContent?.dataset?.compare || false)

    addCompareEventListener()
    
    displayCompare(compare)

}
