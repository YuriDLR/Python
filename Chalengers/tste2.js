let Year = new Date
Year = Year.getFullYear()

if (Year % 4 == 0){
    console.log("é bissexto")
} else{
    console.log("NE NAO HOMI \uF603")
}

let hour = new Date
hour = hour.getHours()


let day = new Date
day = day.getDate()

let month = new Date
let minute = new Date 
console.log(`hoje é dia ${day} de ${month.getMonth()} e agora são ${hour}:${minute.getMinutes()} do ano ${Year}`)



 