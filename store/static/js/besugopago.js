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
    if ($("#tarjeta").is(":checked", true)) {
      if (
        creditCardValidation($("#cardNumber").val()) &&
        $("#owner").val().length != 0 &&
        $("#cvv").val().length != 0
      ) {
        let json = { mota: $("#cardNumber").val() };
        let csrftoken = "{{csrf_token}}";
        let text = "";
        $.ajax({
          type: "POST",
          headers: { "X-CSRFToken": csrftoken },
          url: "/ordainketamota/",
          data: json,
          dataType: "json",
          success: function (data) {
            window.location.href = '/carro';
          },
          error: function (e) {
            alert("errorea: " + e);
            console.log(e);
          },
        });
      } else {
        alert("Datu denak ondo sartu behar dira.");
      }
    } if ($("#paypal").is(":checked", true)) {
      let json = { mota: "paypal" };
      let csrftoken = "{{csrf_token}}";
      let text = "";
      $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: "/ordainketamota/",
        data: json,
        dataType: "json",
        success: function (data) {
          window.location.href = '/carro';
        },
        error: function (e) {
          alert("errorea: " + e);
          console.log(e);
        },
      });
    }
  });

  function creditCardValidation(creditCradNum) {
    var regEx = /^(?:4[0-9]{12}(?:[0-9]{3})?)$/;
    if (creditCradNum.match(regEx)) {
      return true;
    } else {
      alert("Kreditu txarteleko zenbakia ez da egokia");
      return false;
    }
  }
})(jQuery);
