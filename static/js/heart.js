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
    //age
    let age = document.forms["heart"]["age"].value;
    if (Number(age) <= 0 || Number(age) >= 100) {
      alert("Error you must enter valid input in (Age) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //gender
    let gender = document.forms["heart"]["sex"].value;
    if (gender != 'Male' && gender != 'Female') {
      alert("Error you must enter valid input in (Sex) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //Chest Pain Type (CP)
  let cp = document.forms["heart"]["Chest Pain Type (CP)"].value;
  if (Number(cp) < 0 || Number(cp) > 4) {
    alert("Error you must enter valid input in (Chest Pain Type (CP)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Resting Blood Pressure (trestbps)
  let trestbps = document.forms["heart"]["Resting Blood Pressure (trestbps)"].value;
  if (Number(trestbps) < 94 || Number(trestbps) > 200) {
    alert("Error you must enter valid input in (Resting Blood Pressure (trestbps)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Serum Cholestoral (chol) mg/dl
  let chol = document.forms["heart"]["Serum Cholestoral (chol) mg/dl"].value;
  if (Number(chol) < 126 || Number(chol) > 564) {
    alert("Error you must enter valid input in (Serum Cholestoral (chol) mg/dl) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Fasting Blood Sugar (fbs) > 120 mg/dl
  let fbs = document.forms["heart"]["Fasting Blood Sugar (fbs) > 120 mg/dl"].value;
  if (fbs != 'Yes' && fbs != 'No') {
    alert("Error you must enter valid input in (Fasting Blood Sugar (fbs) > 120 mg/dl) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Resting Electrocardiographic Results (restecg)
  let restecg = document.forms["heart"]["Resting Electrocardiographic Results (restecg)"].value;
  if (Number(restecg) < 0 || Number(restecg) > 3) {
    alert("Error you must enter valid input in (Resting Electrocardiographic Results (restecg)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Maximum Heart Rate Achieved (thalach)
  let thalach = document.forms["heart"]["Maximum Heart Rate Achieved (thalach)"].value;
  if (Number(thalach) < 71 || Number(thalach) > 202) {
    alert("Error you must enter valid input in (Maximum Heart Rate Achieved (thalach)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Exercise Induced Angina (exang)
  let exang = document.forms["heart"]["Exercise Induced Angina (exang)"].value;
  if ( exang != 'Yes' && exang != 'No' ) {
    alert("Error you must enter valid input in (Exercise Induced Angina (exang)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //ST depression (oldpeak)
  let oldpeak = document.forms["heart"]["ST depression (oldpeak)"].value;
  if (Number(oldpeak) < 0 || Number(oldpeak) > 6.2) {
    alert("Error you must enter valid input in (ST depression (oldpeak)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Slope of the ST Segment (slope)
  let slope = document.forms["heart"]["Slope of the ST Segment (slope)"].value;
  if (Number(slope) < 1 || Number(slope) > 3) {
    alert("Error you must enter valid input in (Slope of the ST Segment (slope)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Number of Major Vessels (ca)
  let ca = document.forms["heart"]["Number of Major Vessels (ca)"].value;
  if (Number(ca) < 0 || Number(ca) > 3) {
    alert("Error you must enter valid input in (Number of Major Vessels (ca)) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Thal
  let Thal = document.forms["heart"]["Thal"].value;
  if (Number(Thal) != 3 && Number(Thal) != 6 &&  Number(Thal) != 7) {
    alert("Error you must enter valid input in (Thal) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }

  
 }