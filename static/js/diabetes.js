let vedio2 = document.getElementById('svedio');
window.addEventListener('scroll' , function()
{
    let val2 = 1 + window.scrollY/-600;
    vedio2.style.opacity = val2;
})  
function returnToPreviousPage() {
  // window.history.back();
  location.reload();
}
// form:
function validateForm() {
  //gender
    let gender = document.forms["diabetes"]["gender"].value;
    if (gender != 'Male' && gender != 'Female') {
      alert("Error you must enter valid input in (Gender) area try again to get an accurate result");
      returnToPreviousPage();
      return false;}
  //age
    let age = document.forms["diabetes"]["age"].value;
    if (Number(age) <= 0 || Number(age) >= 100) {
      alert("Error you must enter valid input in (Age) area try again to get an accurate result");
      returnToPreviousPage();
      return false;}
  //hypertension
  let hypertension = document.forms["diabetes"]["hypertension"].value;
  if (hypertension != 'Yes' && hypertension != 'No') {
    alert("Error you must enter valid input in (Hypertension) area try again to get an accurate result");
    returnToPreviousPage();
    return false;}
  //Heart Disease
  let heart_disease = document.forms["diabetes"]["heart_disease"].value;
  if (heart_disease != 'Yes' && heart_disease != 'No') {
    alert("Error you must enter valid input in (Heart Disease) area try again to get an accurate result");
    returnToPreviousPage();
    return false;}
  //bmi
  let bmi = document.forms["diabetes"]["bmi"].value;
  if (Number(bmi) < 10 || Number(bmi) > 95) {
    alert("Error you must enter valid input in (BMI) area try again to get an accurate result");
    returnToPreviousPage();
    return false;}
  //HbA1c_level
  let HbA1c_level = document.forms["diabetes"]["HbA1c_level"].value;
  if (Number(HbA1c_level) < 3.5 || Number(HbA1c_level) > 9) {
    alert("Error you must enter valid input in (Glycated Haemoglobin (HbA1c) Level) area try again to get an accurate result");
    returnToPreviousPage();
    return false;}
  //blood_glucose_level
  let blood_glucose_level = document.forms["diabetes"]["blood_glucose_level"].value;
  if (Number(blood_glucose_level) < 80 || Number(blood_glucose_level) > 300) {
    alert("Error you must enter valid input in (Blood Glucose Level) area try again to get an accurate result");
    returnToPreviousPage();
    return false;}
  }