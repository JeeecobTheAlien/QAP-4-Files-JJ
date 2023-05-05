const motelCustomer = {
    name: "Mark White",
    gender: "Male",
    birthdate: "1991-01-12",
    prefRooms: ["smoking room", "king size bed", "extra key", "pool view"],
    payMethod: "Credit Card",
    mailAddress: {
        street: "2 West road",
        city: "Corner brook",
        province: "NL",
        postal: "a1n 0c9",
    },
    phonenumber: "7096824477",
    checkInDate: {
        date: "2023-05-10",
        time: "15:00",
    },
    checkOutDate: {
        date: "2023-05-12",
        time: "11:00",
    },
    getage: function() {
        const birthdate = new Date(this.birthdate);
        const now = new Date();
        let age = now.getFullYear() - birthdate.getFullYear();
        const monthdifference = now.getMonth() - birthdate.getMonth();
        if (
            monthdifference < 0 || (monthdifference === 0 && now.getDate() < birthdate.getDate())

        ) {
            age--;
        }
        return age;
    },
    getDurationOfStay: function() {
        const checkInDateTime = new Date(
            this.checkInDate.date + " " + this.checkInDate.time
        );
        const checkOutDateTime = new Date(
            this.checkOutDate.date + " " + this.checkOutDate.time
        );
        const diffTime = Math.abs(checkOutDateTime - checkInDateTime);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return diffDays;
    },

};
html = `
  <ul>
    <li>Name: ${motelCustomer.name} </li>
    <li>Gender: ${motelCustomer.gender} </li>
    <li>Age: ${motelCustomer.getage()} </li>
    <li>Room preferences: ${motelCustomer.prefRooms.join(", ")} </li>
    <li>Payment method: ${motelCustomer.payMethod} </li>
    <li>Mailing Address: ${motelCustomer.mailAddress.street}, ${
    motelCustomer.mailAddress.city
}, ${motelCustomer.mailAddress.province}, ${
    motelCustomer.mailAddress.postal
} </li>
    <li>Phone number: ${motelCustomer.phone} </li>
    <li>Check-In date and time: ${motelCustomer.checkInDate.date} ${
    motelCustomer.checkInDate.time
} </li>
    <li>Check-Out date and time: ${motelCustomer.checkOutDate.date} ${
    motelCustomer.checkOutDate.time
} </li>
    <li>Duration of stay: ${motelCustomer.getDurationOfStay()} day(s) </li>
  </ul>
`;

document.body.innerHTML = html;