console.log("its working")
// setting local storage for cart to get items
if(localStorage.getItem('cart') == null){
 
var cart = {}


}else{
  cart = JSON.parse(localStorage.getItem('cart'))
  document.getElementById('cart').innerHTML = "Items in cart " + "(" + Object.keys(cart).length + ")"
}


// getting product id and setting to the cart

$('.cart').click(function(){

var pro_id  = this.id.toString()

if(cart[pro_id] == undefined){
  cart[pro_id] = 1
}else{
   cart[pro_id] = cart[pro_id] + 1
}
console.log(cart)
localStorage.setItem('cart', JSON.stringify(cart))
document.getElementById('cart').innerHTML = "Items in cart " + "(" + Object.keys(cart).length + ")"
})

// cart popover bootstrap cdn
$('#cart').popover()
document.getElementById("cart").setAttribute('data-content', '<h5>Cart for your items in my shopping cart</h5>');