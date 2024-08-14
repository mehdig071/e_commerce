import { formatPrice,
    displayCompare,
    addCompareEventListener,
     addFlashMessage,
     fetchData, 
     manageCartLink, 
     addCartEventListenerToLink,
     initCart,
     updateHeaderCart,
     manageCompareLink } from './library.js';

window.onload = () => {
    
    console.log("compare");

    let mainContent = document.querySelector('.compare_container')

    let compare = JSON.parse(mainContent?.dataset?.compare || false)

    addCompareEventListener()

    displayCompare(compare)

}