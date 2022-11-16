(function ($) {
  "use strict";
  
  $(document).ready(function () {
    function totaljaso(){
      let json = {};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/totalajaso/",
        data: json,
        dataType: 'json',
        success: function (data) {
          //alert(data[0].mezua);
          $("#total").html(data[0].total+"€");
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });

    }
    totaljaso();

    function ajaxkarritoupdate(id, funtzio){
      let contador = "#cont" + id;
      let contval=$(contador).val();
      let json = {id:id, cont:contval, funtz:funtzio};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/updatecarro/",
        data: json,
        dataType: 'json',
        success: function (data) {
          $("#total").html(data[0].total.toFixed(2)+"€");
          //aukeratutako produktuen kopurua jarri
          
          for (let i = 0; i < data[0].eskaerak.length; i++) {
            $("#contador"+data[0].eskaerak[i].produktuaid).val(data[0].eskaerak[i].kopurua)
          }
          if(data[0].mezua == "Ez dago stock-ik"){
            alert(data[0].mezua);
            //$(contador).val("0")
          }
          console.log(data)
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });
    }


    $(".gehiMariskada").click(function (e) {
      e.preventDefault();
      var id = $(this).val();
      let contador = "#cont" + id;
      let balio = parseInt($(contador).val()) + 1;
      $(contador).val(balio);
      ajaxkarritoupdate(id, 'gei');
      //totaljaso();

    });

    $(".kenMariskada").click(function (e) {
      e.preventDefault();

      var id = $(this).val();
      //alert(id);
      let contador = "#cont" + id;
      let balio = parseInt($(contador).val()) - 1;
      if (balio < 0) {
        balio = 0;
      }
      $(contador).val(balio);
      ajaxkarritoupdate(id, 'ken');
      //totaljaso();
    });


    $(".basura").click(function (e) {
      var id = $(this).attr('id');
      id = id.split("ra").pop();


      let json = {id:id};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/eskaeraezabatu/",
        data: json,
        dataType: 'json',
        success: function (data) {
          totaljaso();
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });

      $(this).parent().parent().remove();
      
    });

    $(".contador").on("input", function(){
      var id = $(this).attr('id');
      id = id.split("t").pop();
      ajaxkarritoupdate(id, 'ken');
      //totaljaso();
  });

  });

 
})(jQuery);
