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
    

    if (creditCardValidation($("#cardNumber").val()) && $("#owner").val().length != 0 && $("#cvv").val().length != 0) {
      let json = {};
      let csrftoken = "{{csrf_token}}";
      let text = "";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/ordainketaegin/",
        data: json,
        dataType: 'json',
        success: function (data) {
          if (confirm('Eskaera egin da!, Faktura gorde nahi duzu?')) {
            var doc = new jsPDF();
            text += 'Faktura '+data[0].eguna +" \r\n ";
            text += data[0].izena +" \r\n \r\n ";
            for (let i = 0; i < data[0].lista.length; i++) {
              text += data[0].lista[i].produktua + " unitateak: " + data[0].lista[i].kopurua + " " + data[0].lista[i].prezioa+"€ \r\n ";
            }
            text += '\r\n Guztira: '+data[0].total+"€";
            console.log(text);
            doc.text(text, 10, 10);
            doc.save('faktura'+data[0].eguna+'.pdf');
          }
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });
    } else {
      alert("Datu denak ondo sartu behar dira.");
    }
  });

  function creditCardValidation(creditCradNum) {
    var regEx =
    /^(?:4[0-9]{12}(?:[0-9]{3})?)$/;
    if (creditCradNum.match(regEx)) {
      return true;
    } else {
      alert("Kreditu txarteleko zenbakia ez da egokia");
      return false;
    }
  }
})(jQuery);
