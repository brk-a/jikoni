const AfricasTalking = require('africastalking');

// TODO: Initialize Africa's Talking
const africastalking = AfricasTalking({
  apiKey: process.env.apiKey, 
  username: 'sandbox',
});


module.exports = async function sendSMS() {
    
    // TODO: Send message
    try {
        const result=await africastalking.SMS.send({
            to: process.env.to, 
            message: 'Hey AT Ninja! Wassup...',
            // from: 'FNjakai'
         });
        console.log(result);
    } catch(ex) {
        console.error(ex);
    } 
};