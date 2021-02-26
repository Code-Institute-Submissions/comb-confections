// Get Stripe public key
fetch("/memberships/config/")
// convert to JS object
.then((result) => { return result.json(); })
// Get data
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  let submitBtn = document.querySelector("#submitBtn");
 if (submitBtn !== null) {
   submitBtn.addEventListener("click", () => {
   // Get Checkout Session ID
   fetch("/memberships/create-checkout-session/")
     .then((result) => { return result.json(); })
     .then((data) => {
       console.log(data);
       // Redirect to seccure Checkout form hosted by Stripe
       return stripe.redirectToCheckout({sessionId: data.sessionId})
     })
     .then((res) => {
       console.log(res);
     });
   });
 }
}); 