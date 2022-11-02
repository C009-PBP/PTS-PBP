$("div.lazy").lazyload({
  effect : "fadeIn"
});


async function getBMI() {
    return fetch("/bmi_calculator/json").then((res) => res.json())
  }


 function addBMI() {
  console.log("TESaddd")
  fetch(`/bmi_calculator/add/`, {
        method: "POST",
        body: new FormData(document.querySelector('#form_bmi'))
    }).then(showNewBMIResult)
  return false
}

async function showNewBMIResult(){
  console.log("tes showNewBMIResult");

  const bmi_object = await getBMI(); 
  let lastIndex = bmi_object.length - 1;
  let htmlString = '';
  if(lastIndex >= 0){
    htmlString += `\n
    <h3>Hasil BMI terakhir Anda: ${bmi_object[lastIndex].fields.bmi_result}</h3>
    <h3>Status: ${bmi_object[lastIndex].fields.deskripsi_hasil}</h3>
    <h3> Disubmit tanggal: ${bmi_object[lastIndex].fields.date_created}</h3> 
    `;
  }else{
    htmlString += `\n
    <h3>Hasil BMI terakhir Anda: - </h3>
    <h3>Status: Belum diketahui </h3>
    `;
  }
  document.getElementById("bmi_result").innerHTML = htmlString;
  console.log("GG")
}


// history

async function viewBMIHistory(){
    
    const bmi_objects = await getBMI();
    console.log("TESSSSSSSS" + " " + bmi_objects);
    let htmlString = ''
    bmi_objects.forEach((item) => {
      htmlString += `\n
      <div class="flex-container justify-content-center align-self-center d-flex h-100""">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Tanggal: ${item.fields.date_created}</h5>
            <h5 class="card-title">BMI: ${item.fields.bmi_result}</h5>
            <h5 class="card-title">Deskripsi: ${item.fields.deskripsi_hasil}</h5>
          </div>
          <div class="card-body">
            <button type="button" id="button-delete" class="btn btn-primary" onclick="deleteBMI(${item.pk})">Delete</button>
          </div>
        </div>
      </div>
      ` 
    })
    document.getElementById("bmi_history").innerHTML = htmlString
    
}

function deleteBMI(bmiPK) {
  // console.log("TESzzz")
  fetch(`/bmi_calculator/delete/${bmiPK}`, {
    method: "GET",
    }
    ).then(viewBMIHistory)
  return false
}

// refreshBMIPage()  
showNewBMIResult();