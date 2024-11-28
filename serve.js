function updatemenu() {
    if (document.getElementById('responsive-menu').checked == true) {
      document.getElementById('menu').style.borderBottomRightRadius = '0';
      document.getElementById('menu').style.borderBottomLeftRadius = '0';
    }else{
      document.getElementById('menu').style.borderRadius = '10px';
    }
  }


function updatePoints() {
    const maxPoints = 600;
    const fields = ["intelligence", "strength", "speed", "durability", "power", "combat"];
    let totalUsed = 0;


    fields.forEach(field => {
        const value = parseInt(document.getElementById(field).value) || 0;
        totalUsed += value;
    });

    document.getElementById("used-points").textContent = totalUsed;
    document.getElementById("remaining-points").textContent = maxPoints - totalUsed;


    const remainingField = document.getElementById("remaining-points");
    if (totalUsed > maxPoints) {
        remainingField.style.color = "red";
    } else {
        remainingField.style.color = "green";
    }
}