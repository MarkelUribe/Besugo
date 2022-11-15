(function ($) {
  "use strict";

  $(document).ready(function () {
    $("#pay").hide();
    $("input[name='radio']").change(function () {
      if ($("#tarjeta").is(":checked", true)) {
        $("#tarjetadiv").slideDown();
        $("#pay").hide();
      } else if ($("#paypal").is(":checked", true)) {
        $("#tarjetadiv").slideUp();
        $("#pay").show();
      }
    });
  });

  $("#confirmar").click(function () {
    var doc = new jsPDF();

    doc.text(20, 20, "Hola mundo");
    doc.text(20, 30, "Vamos a generar un pdf desde el lado del cliente");

    // Add new page
    doc.addPage();
    doc.text(20, 20, "Visita programacion.net");

    // Save the PDF
    doc.save("documento.pdf");
    alert("hsbcj");

    if (creditCardValidation($("#cardNumber").val())) {
      alert("ondo");
    } else {
      alert("gaizki");
    }
  });

  function creditCardValidation(creditCradNum) {
    var regEx =
      /^5[1-5][0-9]{14}$|^2(?:2(?:2[1-9]|[3-9][0-9])|[3-6][0-9][0-9]|7(?:[01][0-9]|20))[0-9]{12}$/;
    if (creditCradNum.value.match(regEx)) {
      return true;
    } else {
      alert("Kreditu txarteleko zenbakia ez da egokia");
      return false;
    }
  }
})(jQuery);
