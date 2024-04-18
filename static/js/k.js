let vedio2 = document.getElementById('svedio');
window.addEventListener('scroll' , function()
{
    let val2 = 1 + window.scrollY/-600;
    vedio2.style.opacity = val2;
})  


function returnToPreviousPage() {
  location.reload();
}
// form:
function validateForm() {
    //Blood_Pressure
    let Blood_Pressure = document.forms["k"]["Blood_Pressure"].value;
    if (Number(Blood_Pressure) < 50 || Number(Blood_Pressure) > 180) {
      alert("Error you must enter valid input in (Blood_Pressure) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //Specific_Gravity
    let Specific_Gravity = document.forms["k"]["Specific_Gravity"].value;
    if (Number(Specific_Gravity) != 1.005 && Number(Specific_Gravity) != 1.010 && Number(Specific_Gravity) != 1.015 && Number(Specific_Gravity) != 1.020 && Number(Specific_Gravity) != 1.025) {
      alert("Error you must enter valid input in (Specific_Gravity) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //Albumin
  let Albumin = document.forms["k"]["Albumin"].value;
  if (Number(Albumin) < 0 || Number(Albumin) > 5) {
    alert("Error you must enter valid input in (Albumin) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Sugar
  let Sugar = document.forms["k"]["Sugar"].value;
  if (Number(Sugar) < 0 || Number(Sugar) > 5) {
    alert("Error you must enter valid input in (Sugar) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Pus_Cell
  let Pus_Cell = document.forms["k"]["Pus_Cell"].value;
  if (Pus_Cell != 'Yes' && Pus_Cell != 'No' ) {
    alert("Error you must enter valid input in (Pus_Cell) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Blood_Glucose_Random
  let Blood_Glucose_Random = document.forms["k"]["Blood_Glucose_Random"].value;
  if (Number(Blood_Glucose_Random) < 22 || Number(Blood_Glucose_Random) > 490) {
    alert("Error you must enter valid input in (Blood_Glucose_Random) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Blood_Urea
  let Blood_Urea = document.forms["k"]["Blood_Urea"].value;
  if (Number(Blood_Urea) < 1.5 || Number(Blood_Urea) > 391) {
    alert("Error you must enter valid input in (Blood_Urea) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Sodium
  let Sodium = document.forms["k"]["Sodium"].value;
  if (Number(Sodium) < 4.5 || Number(Sodium) > 163) {
    alert("Error you must enter valid input in (Sodium) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Hemoglobin
  let Hemoglobin = document.forms["k"]["Hemoglobin"].value;
  if (Number(Hemoglobin) < 3.1 || Number(Hemoglobin) > 17.8) {
    alert("Error you must enter valid input in (Hemoglobin) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Hypertension
  let Hypertension = document.forms["k"]["Hypertension"].value;
  if ( Hypertension != 'Yes' && Hypertension != 'No') {
    alert("Error you must enter valid input in (Hypertension) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Diabetes_Mellitus
  let Diabetes_Mellitus = document.forms["k"]["Diabetes_Mellitus"].value;
  if (Diabetes_Mellitus != 'Yes' && Diabetes_Mellitus != 'No') {
    alert("Error you must enter valid input in (Diabetes_Mellitus) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Appetite
  let Appetite = document.forms["k"]["Appetite"].value;
  if (Appetite != 'Good' && Appetite != 'Poor') {
    alert("Error you must enter valid input in (Appetite) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Pedal_Edema
    let Pedal_Edema = document.forms["k"]["Pedal_Edema"].value;
    if (Pedal_Edema != 'Yes' && Pedal_Edema != 'No') {
      alert("Error you must enter valid input in (Pedal_Edema) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
   //Anemia
  let Anemia = document.forms["k"]["Anemia"].value;
  if (Anemia != 'Yes' && Anemia != 'No') {
    alert("Error you must enter valid input in (Anemia) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  
}
