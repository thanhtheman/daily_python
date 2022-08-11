// for(let i = 0; i <= 100; i++) {
//     let out = ""
//     if(i % 3 === 0)
//         out += "Fizz";
//     if(i % 5 === 0)
//         out += "Buzz";
//     if(i % 7 === 0)
//         out += "Bazz";
//     console.log(out || i);
// }


// order = [{name: 'espresso', price: 1.99}, {"name": 'coffee', "price": 2.50}, {"name": 'cake', "price": 2.79}]
// subtotal = 0
// for(let i = 0; i < order.length; i++) {
//     subtotal += order[i].price
// }
// console.log(subtotal)

let obj = {1: {name: 'espresso', price: 1.99}, 2: {"name": 'coffee', "price": 2.50}, 3: {"name": 'cake', "price": 2.79}}

let jason = JSON.stringify(obj)
console.log(jason)


let abc = JSON.parse(jason)
console.log(abc)

let order = abc[1].name; console.log(order)