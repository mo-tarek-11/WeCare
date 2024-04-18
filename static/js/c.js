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
    let age = document.forms["C"]["Age"].value;
    if (Number(age) <= 0 || Number(age) >= 100) {
      alert("Error you must enter valid input in (Age) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  //gender
    let gender = document.forms["C"]["Sex"].value;
    if (gender != 'Male' && gender != 'Female') {
      alert("Error you must enter valid input in (Sex) area try again to get an accurate result");
      returnToPreviousPage();
      return false;
    }
  // //Albumin Blood Test (ALB) g/L
  // let ALB = document.forms["C"]["Albumin Blood Test (ALB) g/L"].value;
  // if (Number(ALB) < 15 || Number(ALB) > 82) {
  //   alert("Error you must enter valid input in (Albumin Blood Test (ALB) g/L) area try again to get an accurate result");
  //   returnToPreviousPage();
  //   return false;
  // }
  //Alkaline Phosphatase Test (ALP) IU/L
  let ALP = document.forms["C"]["Alkaline Phosphatase Test (ALP) IU/L"].value;
  if (Number(ALP) < 11.3 || Number(ALP) > 416.6) {
    alert("Error you must enter valid input in (Alkaline Phosphatase Test (ALP) IU/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Alanine Transaminase Test (ALT) U/L
  let ALT = document.forms["C"]["Alanine Transaminase Test (ALT) U/L"].value;
  if (Number(ALT) < 1 || Number(ALT) > 325.3) {
    alert("Error you must enter valid input in (Alanine Transaminase Test (ALT) U/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Aspartate Transaminase Test (AST) U/L
  let AST = document.forms["C"]["Aspartate Transaminase Test (AST) U/L"].value;
  if (Number(AST) < 10.6 || Number(AST) > 324) {
    alert("Error you must enter valid input in (Aspartate Transaminase Test (AST) U/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Bilirubin Blood Test (BIL) µmol/L
  let BIL = document.forms["C"]["Bilirubin Blood Test (BIL) µmol/L"].value;
  if (Number(BIL) < 0.8 || Number(BIL) > 254) {
    alert("Error you must enter valid input in (Bilirubin Blood Test (BIL) µmol/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Cholinesterase (CHE) kU/L
  let CHE = document.forms["C"]["Cholinesterase (CHE) kU/L"].value;
  if (Number(CHE) < 1.42 || Number(CHE) > 16.41) {
    alert("Error you must enter valid input in (Cholinesterase (CHE) kU/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Cholesterol (CHOL) mmol/L
  let CHOL = document.forms["C"]["Cholesterol (CHOL) mmol/L"].value;
  if (Number(CHOL) < 1.43 || Number(CHOL) > 9.67) {
    alert("Error you must enter valid input in (Cholesterol (CHOL) mmol/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Creatinine Blod Test (CREA) µmol/L
  let CREA = document.forms["C"]["Creatinine Blod Test (CREA) µmol/L"].value;
  if (Number(CREA) < 8 || Number(CREA) > 1079) {
    alert("Error you must enter valid input in (Creatinine Blod Test (CREA) µmol/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Gamma-Glutamyl Transpeptidase Test (GGT) U/L
  let GGT = document.forms["C"]["Gamma-Glutamyl Transpeptidase Test (GGT) U/L"].value;
  if (Number(GGT) < 4.5 || Number(GGT) > 650.9) {
    alert("Error you must enter valid input in (Gamma-Glutamyl Transpeptidase Test (GGT) U/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  //Protein Blood Test (PROT) g/L
  let PROT = document.forms["C"]["Protein Blood Test (PROT) g/L"].value;
  if (Number(PROT) < 44.8 || Number(PROT) > 90) {
    alert("Error you must enter valid input in (Protein Blood Test (PROT) g/L) area try again to get an accurate result");
    returnToPreviousPage();
    return false;
  }
  
}
